# 🎯 KRISHNA - Parser & Command Processing Lead

## 📋 Role Assignment
**Position:** Parser & Tokenization Architect  
**Primary Responsibility:** Command parsing, tokenization, redirection handling, aur pipeline detection

---

## 🔥 Main Contributions

### 1️⃣ Parser.c - Command Ka Brain (206 lines)

#### **Lines 1-2: Header Files Include**
```c
#include "headers/parser.h"
#include "headers/utils.h"
```
**Hinglish Explanation:**
- `parser.h` mein parsing functions ke declarations hain
- `utils.h` mein helper functions hain jaise error printing, memory management

#### **Lines 5-83: Main Parse Command Function**
```c
command_t* parse_command(char *cmd) {
    command_t *parsed_cmd = malloc(sizeof(command_t));
    if (!parsed_cmd) {
        print_error("Memory allocation failed");
        return NULL;
    }
    
    // Initialize command structure
    parsed_cmd->args = NULL;
    parsed_cmd->argc = 0;
    parsed_cmd->input_file = NULL;
    parsed_cmd->output_file = NULL;
    parsed_cmd->error_file = NULL;
    parsed_cmd->append_output = 0;
    parsed_cmd->background = 0;
```
**Hinglish Explanation:**
- **malloc():** Heap memory mein command structure ke liye space allocate kiya
- Agar memory nahi mili to NULL return kar dete hain
- **Initialization:** Sabhi fields ko default values set kiye:
  - `args` = NULL (abhi arguments nahi parse kiye)
  - `argc` = 0 (argument count zero)
  - Files = NULL (koi redirection nahi abhi)
  - `append_output` = 0 (normal output, append nahi)
  - `background` = 0 (foreground execution default)

#### **Lines 22-35: Background Execution Detection**
```c
    char *cmd_copy = strdup(cmd);
    if (!cmd_copy) {
        free(parsed_cmd);
        return NULL;
    }
    
    trim_whitespace(cmd_copy);
    
    // Check for background execution
    if (cmd_copy[strlen(cmd_copy) - 1] == '&') {
        parsed_cmd->background = 1;
        cmd_copy[strlen(cmd_copy) - 1] = '\0';
        trim_whitespace(cmd_copy);
    }
```
**Hinglish Explanation:**
- **strdup():** Command string ka copy banaya (original modify nahi karna)
- **trim_whitespace():** Extra spaces remove kiye starting aur ending se
- **Background check:** Last character `&` hai to:
  - `background` flag 1 set kar diya
  - `&` character ko NULL (`\0`) se replace kar diya
  - Phir se spaces trim kiye
- Example: `"ls -la &"` → background = 1, command = `"ls -la"`

#### **Lines 38-76: Redirection Parsing (Critical Section)**
```c
    // Parse redirection
    char *input_redir = strstr(cmd_copy, " < ");
    char *output_redir = strstr(cmd_copy, " > ");
    char *append_redir = strstr(cmd_copy, " >> ");
    char *error_redir = strstr(cmd_copy, " 2> ");
    
    // Handle input redirection
    if (input_redir) {
        *input_redir = '\0';
        char *input_file = input_redir + 3;
        trim_whitespace(input_file);
        parsed_cmd->input_file = strdup(input_file);
        trim_whitespace(cmd_copy);
    }
    
    // Handle output redirection (check append first)
    if (append_redir) {
        *append_redir = '\0';
        char *output_file = append_redir + 4;
        trim_whitespace(output_file);
        parsed_cmd->output_file = strdup(output_file);
        parsed_cmd->append_output = 1;
        trim_whitespace(cmd_copy);
    } else if (output_redir) {
        *output_redir = '\0';
        char *output_file = output_redir + 3;
        trim_whitespace(output_file);
        parsed_cmd->output_file = strdup(output_file);
        parsed_cmd->append_output = 0;
        trim_whitespace(cmd_copy);
    }
    
    // Handle error redirection
    if (error_redir) {
        *error_redir = '\0';
        char *error_file = error_redir + 4;
        trim_whitespace(error_file);
        parsed_cmd->error_file = strdup(error_file);
        trim_whitespace(cmd_copy);
    }
```
**Hinglish Explanation:**

**Input Redirection (`<`):**
- `strstr()` se " < " dhoondte hain command mein
- Agar mila to us position ko NULL kar diya (string split ho gaya)
- 3 characters aage (+3) file name start hota hai (skip " < ")
- File name ko trim karke `input_file` mein store kiya

**Output Redirection (`>` and `>>`):**
- **Pehle `>>` check karte hain** (append mode)
  - Agar mila to append_output = 1 set kiya
  - 4 characters aage (+4) file name hai (skip " >> ")
- **Else normal `>` check** (overwrite mode)
  - append_output = 0 rehta hai
  - 3 characters aage (+3) file name

**Error Redirection (`2>`):**
- stderr ko separate file mein redirect karne ke liye
- 4 characters aage (+4) file name

**Example:** `"ls -la > output.txt 2> error.txt"`
- output_file = "output.txt"
- error_file = "error.txt"

#### **Lines 78-82: Final Tokenization**
```c
    // Tokenize the remaining command
    parsed_cmd->args = tokenize(cmd_copy, &parsed_cmd->argc);
    
    free(cmd_copy);
    return parsed_cmd;
}
```
**Hinglish Explanation:**
- Ab redirection symbols remove ho chuke hain
- Bacha hua command string ko tokenize karte hain
- `tokenize()` function spaces se split karke array banata hai
- `argc` mein total arguments count store hota hai
- `cmd_copy` free kiya memory leak avoid karne ke liye
- Final parsed command structure return kar diya

#### **Lines 86-102: Free Command Memory**
```c
void free_command(command_t *cmd) {
    if (!cmd) return;
    
    if (cmd->args) {
        free_string_array(cmd->args, cmd->argc);
    }
    if (cmd->input_file) {
        free(cmd->input_file);
    }
    if (cmd->output_file) {
        free(cmd->output_file);
    }
    if (cmd->error_file) {
        free(cmd->error_file);
    }
    free(cmd);
}
```
**Hinglish Explanation:**
- Command use hone ke baad memory cleanup zaruri hai
- **NULL check:** Pehle check karo cmd NULL to nahi
- **args array:** Sabhi arguments free karo
- **File names:** Teeno file names (input, output, error) free karo
- **Command structure:** Finally structure khud ko free karo
- Proper cleanup se memory leaks nahi hote

#### **Lines 105-128: Builtin Command Detection**
```c
int is_builtin(char *cmd) {
    if (!cmd) return 0;
    
    char *cmd_copy = strdup(cmd);
    if (!cmd_copy) return 0;
    
    char *first_token = strtok(cmd_copy, " \t");
    if (!first_token) {
        free(cmd_copy);
        return 0;
    }
    
    int result = (strcmp(first_token, "cd") == 0 ||
                  strcmp(first_token, "pwd") == 0 ||
                  strcmp(first_token, "echo") == 0 ||
                  strcmp(first_token, "exit") == 0 ||
                  strcmp(first_token, "history") == 0 ||
                  strcmp(first_token, "jobs") == 0 ||
                  strcmp(first_token, "fg") == 0 ||
                  strcmp(first_token, "bg") == 0);
    
    free(cmd_copy);
    return result;
}
```
**Hinglish Explanation:**
- Check karta hai command built-in hai ya external
- **strdup():** Command ka copy banaya (original safe)
- **strtok():** First word/token nikala (command name)
- **strcmp():** Har built-in command se compare kiya:
  - cd, pwd, echo, exit (basic)
  - history, jobs, fg, bg (advanced)
- **Return 1** agar match mila (builtin hai)
- **Return 0** agar nahi mila (external command hai)
- Memory free karna mat bhoolna!

#### **Lines 131-133: Pipeline Detection**
```c
int is_pipeline(char *cmd) {
    return strstr(cmd, "|") != NULL;
}
```
**Hinglish Explanation:**
- Ekdum simple function!
- `strstr()` pipe character `|` dhoondhta hai
- Agar mila to 1 return (pipeline hai)
- Nahi mila to 0 return (normal command)
- Example: `"ls | grep txt"` → returns 1

#### **Lines 136-155: Pipeline Splitting**
```c
char** split_pipeline(char *cmd, int *count) {
    *count = 0;
    char **commands = malloc(MAX_ARGS * sizeof(char*));
    if (!commands) {
        print_error("Memory allocation failed");
        return NULL;
    }
    
    char *token = strtok(cmd, "|");
    while (token != NULL && *count < MAX_ARGS) {
        trim_whitespace(token);
        if (strlen(token) > 0) {
            commands[*count] = strdup(token);
            (*count)++;
        }
        token = strtok(NULL, "|");
    }
    
    return commands;
}
```
**Hinglish Explanation:**
- Pipeline ko individual commands mein split karta hai
- **Memory allocate:** Array of string pointers ke liye
- **strtok():** Pipe `|` delimiter se split kiya
- **Loop:**
  - Har token (command) ko trim karte hain
  - Empty strings skip karte hain
  - Valid commands ko array mein store karte hain
  - Count increment karte hain
- **Example:** `"ls | grep txt | wc -l"` → 3 commands

#### **Lines 158-182: Tokenize Function**
```c
char** tokenize(char *str, int *count) {
    *count = 0;
    char **tokens = malloc(MAX_ARGS * sizeof(char*));
    if (!tokens) {
        print_error("Memory allocation failed");
        return NULL;
    }
    
    // Make a copy since strtok modifies the original string
    char *str_copy = strdup(str);
    if (!str_copy) {
        free(tokens);
        return NULL;
    }
    
    char *token = strtok(str_copy, " \t");
    while (token != NULL && *count < MAX_ARGS) {
        tokens[*count] = strdup(token);
        (*count)++;
        token = strtok(NULL, " \t");
    }
    
    free(str_copy);
    return tokens;
}
```
**Hinglish Explanation:**
- Command string ko words (tokens) mein split karta hai
- **malloc():** Token pointers array ke liye memory
- **strdup():** Original string ka copy (strtok modify karta hai)
- **strtok():** Space aur tab se split karta hai
- **Loop:**
  - Har word ko array mein store
  - Count increment
  - Next token lao
- **Example:** `"ls -la /home"` → ["ls", "-la", "/home"]
- **Cleanup:** String copy free karo

#### **Lines 185-205: Trim Whitespace Function**
```c
void trim_whitespace(char *str) {
    if (!str) return;
    
    // Remove leading whitespace
    char *start = str;
    while (*start && (*start == ' ' || *start == '\t' || *start == '\n' || *start == '\r')) {
        start++;
    }
    
    // Remove trailing whitespace
    char *end = start + strlen(start) - 1;
    while (end > start && (*end == ' ' || *end == '\t' || *end == '\n' || *end == '\r')) {
        end--;
    }
    
    // Move string to beginning and null terminate
    if (start != str) {
        memmove(str, start, end - start + 1);
    }
    str[end - start + 1] = '\0';
}
```
**Hinglish Explanation:**
- String ke starting aur ending se extra spaces remove karta hai
- **Leading whitespace:**
  - `start` pointer ko aage move karo jab tak space/tab milta rahe
  - Spaces skip karke actual content pe pohoncho
- **Trailing whitespace:**
  - `end` pointer ko peeche move karo from last character
  - Spaces ko skip karke last valid character pe aao
- **memmove():** Clean string ko original position pe move karo
- **NULL terminate:** String ko properly end karo
- **Example:** `"  ls -la  \n"` → `"ls -la"`

---

## 🎓 VIVA QUESTIONS (Krishna Ke Liye)

### Basic Level (Easy) ⭐

**Q1: Parser ka main kaam kya hai shell mein?**
<details>
<summary>Answer</summary>
Parser command string ko analyze karke structured format mein convert karta hai. Ye detect karta hai:
- Command aur arguments
- Redirection symbols (<, >, >>)
- Background execution (&)
- Pipeline operations (|)
</details>

**Q2: `strdup()` function kya karta hai aur kyu important hai?**
<details>
<summary>Answer</summary>
`strdup()` string ka duplicate copy banata hai heap memory mein. Important hai kyunki:
- Original string modify nahi hoti
- `strtok()` jaise functions string modify karte hain
- Har copy ko separately free kar sakte hain
</details>

**Q3: Redirection symbols kaun kaun se hain?**
<details>
<summary>Answer</summary>
- `<` - Input redirection (stdin)
- `>` - Output redirection (stdout, overwrite)
- `>>` - Output append (stdout, add to end)
- `2>` - Error redirection (stderr)
</details>

**Q4: Background execution ka symbol kya hai?**
<details>
<summary>Answer</summary>
Ampersand `&` symbol command ke end mein. Example: `sleep 10 &` - command background mein execute hoga.
</details>

**Q5: `strtok()` function ka kya use hai?**
<details>
<summary>Answer</summary>
String ko tokens (words) mein split karta hai delimiter ke basis par. First call mein string pass karo, next calls mein NULL. Delimiter characters pe string break hota hai.
</details>

### Intermediate Level (Medium) ⭐⭐

**Q6: `>>` ko pehle kyu check karte hain `>` se?**
<details>
<summary>Answer</summary>
Kyunki `>>` mein `>` include hai. Agar pehle `>` check karenge to `>>` ka second `>` bhi match ho jayega aur galat parsing hoga. Order important hai:
1. Pehle `>>` check (4 characters)
2. Else `>` check (3 characters)
</details>

**Q7: `trim_whitespace()` mein `memmove()` vs `strcpy()` - kaun better hai?**
<details>
<summary>Answer</summary>
`memmove()` better hai kyunki:
- Overlapping memory regions handle kar sakta hai
- Source aur destination same string ke parts ho sakte hain
- `strcpy()` overlap mein undefined behavior deta hai
- Safety aur correctness ke liye `memmove()` use kiya
</details>

**Q8: Tokenization mein `" \t"` delimiter kyu use kiya?**
<details>
<summary>Answer</summary>
Space (' ') aur tab (\t) dono standard whitespace hain commands mein. User space ya tab dono se arguments separate kar sakta hai. Dono ko delimiter banane se flexible parsing hoti hai.
</details>

**Q9: Memory leak kahan ho sakta hai parsing mein?**
<details>
<summary>Answer</summary>
- `strdup()` ke baad free na karna
- `malloc()` ke baad free na karna
- Redirection file names free na karna
- `tokenize()` ka array free na karna
- `free_command()` call na karna parse ke baad
</details>

**Q10: `command_t` structure mein kaun kaun se fields hain?**
<details>
<summary>Answer</summary>
```c
char **args;           // Arguments array
int argc;              // Argument count
char *input_file;      // Input redirection
char *output_file;     // Output redirection
char *error_file;      // Error redirection
int append_output;     // Append mode flag
int background;        // Background flag
```
</details>

### Advanced Level (Hard) ⭐⭐⭐

**Q11: Complex command parse karo: `"cat < input.txt | grep error > output.txt &"`**
<details>
<summary>Answer</summary>
**Step-by-step parsing:**

1. **Background detection:**
   - Last character '&' → background = 1
   - Remove '&': `"cat < input.txt | grep error > output.txt"`

2. **Pipeline detection:**
   - '|' present → is_pipeline = true
   - Split into: ["cat < input.txt", "grep error > output.txt"]

3. **First command parse:**
   - Input redir: input_file = "input.txt"
   - Command: ["cat"]

4. **Second command parse:**
   - Output redir: output_file = "output.txt"
   - Command: ["grep", "error"]

5. **Result:**
   - Two commands in pipeline
   - First reads from input.txt
   - Second writes to output.txt
   - Whole pipeline runs in background
</details>

**Q12: `strtok()` thread-safe hai kya? Agar nahi to alternative kya hai?**
<details>
<summary>Answer</summary>
**NO, thread-safe nahi hai** kyunki internal static variable use karta hai.

**Problems:**
- Multiple threads parallel use nahi kar sakte
- Nested strtok() calls interfere karte hain

**Alternative: `strtok_r()` (reentrant version)**
```c
char *saveptr;
char *token = strtok_r(str, delim, &saveptr);
while (token) {
    // process token
    token = strtok_r(NULL, delim, &saveptr);
}
```

Hamare single-threaded shell mein `strtok()` OK hai.
</details>

**Q13: Redirection precedence aur error handling explain karo**
<details>
<summary>Answer</summary>
**Precedence Order:**
1. Input redirection (`<`) - stdin setup
2. Output redirection (`>` / `>>`) - stdout setup
3. Error redirection (`2>`) - stderr setup

**Error Scenarios:**
- File not found for input: Error, command fail
- Permission denied for output: Error, command fail
- Disk full: Error during execution
- Invalid file names: Parsing error

**Handling:**
```c
if (input_redir) {
    if (!file_exists(input_file)) {
        print_error("File not found");
        return NULL;
    }
}
```

**Multiple redirections:**
```bash
cmd < in.txt > out.txt 2> err.txt
```
All three work simultaneously - different file descriptors.
</details>

**Q14: Parser optimization techniques - kya improve kar sakte hain?**
<details>
<summary>Answer</summary>
**Current Approach Issues:**
- Multiple string copies (`strdup()`)
- Sequential `strstr()` calls
- Multiple passes over string

**Optimization Techniques:**

1. **Single Pass Parsing:**
   - Ek hi loop mein sab detect karo
   - State machine use karo

2. **In-place Parsing:**
   - String modify karo copy na banao
   - NULL characters se split karo

3. **Pre-allocation:**
   - Token array pre-allocate karo
   - Realloc avoid karo

4. **Regex/Lexer:**
   - Proper lexical analyzer use karo
   - Token patterns define karo

**Trade-off:** Current code simple aur maintainable hai, optimization se complexity badhegi.
</details>

**Q15: Parsing edge cases aur error scenarios handle karo**
<details>
<summary>Answer</summary>
**Edge Cases:**

1. **Empty Commands:**
```c
if (strlen(cmd) == 0) return NULL;
```

2. **Only Whitespace:**
```c
trim_whitespace(cmd);
if (strlen(cmd) == 0) return NULL;
```

3. **Multiple Redirections:**
```bash
cmd > file1 > file2  # Last one wins
```

4. **Unclosed Quotes:**
```bash
echo "hello world  # Error: missing closing quote
```

5. **Trailing Pipe:**
```bash
ls | grep txt |  # Error: incomplete pipeline
```

6. **Invalid File Names:**
```bash
cmd > /invalid/path/file  # Permission/path error
```

**Error Handling Strategy:**
- NULL checks at every malloc
- Validate parsed structure before execution
- Set error flags in command_t
- Return NULL on critical errors
- Print helpful error messages

**Example Validation:**
```c
if (parsed_cmd->args == NULL || parsed_cmd->argc == 0) {
    free_command(parsed_cmd);
    return NULL;
}
```
</details>

---

## 🏆 Key Achievements
1. ✅ Robust command parsing with all bash features
2. ✅ Complete redirection handling (input/output/error)
3. ✅ Pipeline detection aur splitting
4. ✅ Background execution support
5. ✅ Memory-safe tokenization aur cleanup

## 📚 Technologies Used
- C Programming
- String Manipulation (strtok, strstr, strcpy)
- Memory Management (malloc, free, strdup)
- Pointer Arithmetic
- Data Structures (command_t)

---

**Note:** Krishna ne parser ka complete implementation kiya - command tokenization se lekar complex redirections tak. Shell mein user input ko machine-understandable format mein convert karna unka main contribution hai.

