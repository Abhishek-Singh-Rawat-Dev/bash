# 🎯 ABHISHEK - Shell Core & Main Loop Lead

## 📋 Role Assignment
**Position:** Shell Core Architecture & Main Loop Developer  
**Primary Responsibility:** Shell initialization, main loop, signal handling, aur shell lifecycle management

---

## 🔥 Main Contributions

### 1️⃣ Main.c - Shell Ka Heart (154 lines)

#### **Lines 1-7: Header Files Include Karna**
```c
#include "headers/shell.h"
#include "headers/parser.h"
#include "headers/executor.h"
#include "headers/builtin.h"
#include "headers/history.h"
#include "headers/jobs.h"
#include "headers/utils.h"
```
**Hinglish Explanation:**
- Sabse pehle humne saare important header files include kiye hain
- Ye headers main shell ke different components ko link karte hain
- Jaise `shell.h` shell ke basic structures hai, `parser.h` commands ko parse karne ke liye
- `executor.h` commands execute karne ke liye, `builtin.h` built-in commands ke liye

#### **Lines 10-13: Global Variables Declaration**
```c
job_t jobs[MAX_JOBS];
int job_count = 0;
int current_job_id = 0;
char *history_file = ".history";
```
**Hinglish Explanation:**
- `jobs[]` array background jobs ko track karne ke liye - jaise `ls &`
- `job_count` batata hai kitne jobs currently running hain
- `current_job_id` har new job ko unique ID deta hai
- `history_file` commands ka history store karta hai ek hidden file mein

#### **Lines 16-26: Signal Handler Function**
```c
void signal_handler(int sig) {
    if (sig == SIGINT) {
        printf("\n");
        print_prompt();
        fflush(stdout);
    } else if (sig == SIGTSTP) {
        printf("\n");
        print_prompt();
        fflush(stdout);
    }
}
```
**Hinglish Explanation:**
- Ye function handle karta hai jab user **Ctrl+C** (SIGINT) ya **Ctrl+Z** (SIGTSTP) press kare
- SIGINT matlab "interrupt" - command ko cancel kar do
- SIGTSTP matlab "stop" - command ko pause kar do
- Signal aane par hum naya prompt print karte hain taaki user phir se command type kar sake
- `fflush(stdout)` immediately output dikhata hai screen par

#### **Lines 29-49: Shell Initialization**
```c
void init_shell(void) {
    // Set up signal handlers
    signal(SIGINT, signal_handler);
    signal(SIGTSTP, signal_handler);
    signal(SIGCHLD, SIG_IGN);
    
    // Initialize history
    init_history();
    
    // Clear job array
    for (int i = 0; i < MAX_JOBS; i++) {
        jobs[i].pid = 0;
        jobs[i].job_id = 0;
        jobs[i].command = NULL;
        jobs[i].status = 0;
        jobs[i].start_time = 0;
    }
    
    printf("Advanced Mini Bash Shell v2.0\n");
    printf("Type 'exit' to quit, 'help' for built-in commands\n");
}
```
**Hinglish Explanation:**
- **signal() setup:** Pehle teen signals ko handle karne ke liye register kiya
  - SIGINT aur SIGTSTP ko apne handler function se handle karenge
  - SIGCHLD ko ignore karte hain (child process ke signals)
- **init_history():** Purani command history ko file se load karte hain
- **jobs array clear:** Loop chalake sabhi job slots ko reset kar diya - sab NULL/0
- Last mein welcome message print kiya - version number aur basic instructions

#### **Lines 52-66: Shell Cleanup Function**
```c
void cleanup_shell(void) {
    // Clean up completed jobs
    cleanup_completed_jobs();
    
    // Save history
    save_history();
    
    // Free job memory
    for (int i = 0; i < MAX_JOBS; i++) {
        if (jobs[i].command) {
            free(jobs[i].command);
            jobs[i].command = NULL;
        }
    }
}
```
**Hinglish Explanation:**
- Jab shell exit ho raha hai to ye cleanup karta hai
- Pehle pending jobs ko clean karta hai
- History ko file mein save karta hai (`.history` file mein)
- Sabhi allocated memory ko free karta hai - memory leak nahi hone dete
- Har job ke command string ko free karte hain

#### **Lines 69-77: Prompt Display Function**
```c
void print_prompt(void) {
    char cwd[1024];
    if (getcwd(cwd, sizeof(cwd)) != NULL) {
        printf("mini-bash:%s$ ", cwd);
    } else {
        printf("mini-bash$ ");
    }
    fflush(stdout);
}
```
**Hinglish Explanation:**
- Ye function terminal prompt print karta hai
- `getcwd()` current directory ka path nikalta hai
- Agar path mil gaya to format: `mini-bash:/home/user$`
- Agar error aaya to simple: `mini-bash$`
- `fflush()` turant output show karta hai

#### **Lines 80-94: Command Input Reading**
```c
int read_command(char *cmd) {
    if (fgets(cmd, MAX_CMD_LEN, stdin) == NULL) {
        return 0; // EOF
    }
    
    // Remove newline
    cmd[strcspn(cmd, "\n")] = 0;
    
    // Skip empty commands
    if (strlen(cmd) == 0) {
        return 1;
    }
    
    return 1;
}
```
**Hinglish Explanation:**
- User se command input lete hain `fgets()` se
- Agar NULL aaya (Ctrl+D) to 0 return karte hain (EOF = End of File)
- `strcspn()` se newline character ko 0 se replace kar diya (string terminate)
- Empty commands ko skip karte hain
- Success par 1 return karte hain

#### **Lines 97-118: Command Execution Logic**
```c
void execute_command(char *cmd) {
    // Add to history
    add_to_history(cmd);
    
    // Check if it's a pipeline
    if (is_pipeline(cmd)) {
        int count;
        char **commands = split_pipeline(cmd, &count);
        if (commands) {
            execute_pipeline(commands, count);
            free_string_array(commands, count);
        }
        return;
    }
    
    // Parse single command
    command_t *parsed_cmd = parse_command(cmd);
    if (parsed_cmd) {
        execute_single_command(parsed_cmd);
        free_command(parsed_cmd);
    }
}
```
**Hinglish Explanation:**
- Sabse pehle command ko history mein add karte hain
- Check karte hain ki command mein pipe (`|`) hai kya - jaise `ls | grep txt`
- Agar pipeline hai to:
  - Commands ko split karte hain pipe se
  - Pipeline executor call karte hain
  - Memory free karte hain
- Agar normal command hai to:
  - Parse karte hain (tokenize + redirection detect)
  - Single command executor call karte hain
  - Memory cleanup

#### **Lines 121-153: Main Function - Shell Ka Boss**
```c
int main(int argc, char *argv[]) {
    (void)argc;
    (void)argv;
    char cmd[MAX_CMD_LEN];
    
    // Initialize shell
    init_shell();
    
    // Main command loop
    while (1) {
        print_prompt();
        
        if (!read_command(cmd)) {
            printf("\n");
            break; // EOF
        }
        
        // Skip empty commands
        if (strlen(cmd) == 0) {
            continue;
        }
        
        // Execute command
        execute_command(cmd);
        
        // Clean up completed background jobs
        cleanup_completed_jobs();
    }
    
    // Cleanup and exit
    cleanup_shell();
    return 0;
}
```
**Hinglish Explanation:**
- **Entry Point:** Ye shell ka main entry point hai - jahan se execution start hota hai
- **init_shell():** Shell initialize karte hain - signals, history, jobs setup
- **Infinite Loop (while 1):**
  - Prompt print karte hain
  - User se command read karte hain
  - Agar EOF (Ctrl+D) to loop break karke exit
  - Empty commands ko skip karte hain
  - Command execute karte hain
  - Background jobs cleanup karte hain
- **cleanup_shell():** Exit karne se pehle cleanup
- **return 0:** Success status return karke program end

---

## 🎓 VIVA QUESTIONS (Abhishek Ke Liye)

### Basic Level (Easy) ⭐

**Q1: Signal handler kya hota hai aur tumne kaun kaun se signals handle kiye?**
<details>
<summary>Answer</summary>
Signal handler ek function hota hai jo special events (like Ctrl+C) ko handle karta hai. Maine teen signals handle kiye:
- SIGINT (Ctrl+C) - Interrupt signal
- SIGTSTP (Ctrl+Z) - Stop signal  
- SIGCHLD - Child process termination (ignored)
</details>

**Q2: `fflush(stdout)` kyu use kiya?**
<details>
<summary>Answer</summary>
Output buffer ko immediately flush karne ke liye. Bina iske output delay se show hota hai. Prompt turant display karne ke liye zaruri hai.
</details>

**Q3: Main loop infinite kyu hai (while 1)?**
<details>
<summary>Answer</summary>
Kyunki shell continuously user input lena chahta hai. Jab tak user `exit` command ya Ctrl+D nahi press karta, tab tak shell running rehna chahiye.
</details>

**Q4: `getcwd()` function ka kya kaam hai?**
<details>
<summary>Answer</summary>
Current Working Directory (CWD) ka path return karta hai. Prompt mein directory show karne ke liye use kiya.
</details>

**Q5: History file ka naam kya hai aur kahan save hota hai?**
<details>
<summary>Answer</summary>
File ka naam `.history` hai (dot se start hota hai matlab hidden file). Current directory mein save hota hai.
</details>

### Intermediate Level (Medium) ⭐⭐

**Q6: Signal handling mein `signal()` vs `sigaction()` - tumne kaun use kiya aur kyu?**
<details>
<summary>Answer</summary>
Maine `signal()` use kiya kyunki ye simple aur portable hai. `sigaction()` zyada powerful hai but complex. For basic signal handling, `signal()` sufficient hai. SIGINT aur SIGTSTP ko apne custom handler se handle karne ke liye.
</details>

**Q7: Job control ke liye kaun se data structures use kiye aur kyu?**
<details>
<summary>Answer</summary>
- `jobs[]` array - Fixed size MAX_JOBS slots
- `job_t` structure with: pid, job_id, command, status, start_time
- Array use kiya because job count predictable hai aur fast access chahiye
- job_count aur current_job_id tracking ke liye
</details>

**Q8: `strcspn()` function kya karta hai aur kahan use kiya?**
<details>
<summary>Answer</summary>
`strcspn()` string mein specified characters ka position return karta hai. Maine newline character (\n) find karne ke liye use kiya taaki input string ko terminate kar sakein. Formula: `cmd[strcspn(cmd, "\n")] = 0;`
</details>

**Q9: Pipeline detection kaise kiya aur kya logic hai?**
<details>
<summary>Answer</summary>
`is_pipeline()` function check karta hai ki command mein pipe character `|` hai ya nahi. Agar hai to commands ko split karke separate execute karna padta hai. Example: `ls | grep txt` - do commands hain jo pipe se connected hain.
</details>

**Q10: Memory leak prevent karne ke liye kya measures liye?**
<details>
<summary>Answer</summary>
- `free_command()` call parse ke baad
- `free_string_array()` pipeline commands ke baad
- `cleanup_shell()` mein sabhi job commands free
- Har malloc ke baad free ensure kiya
- `free()` ke baad pointer NULL set kiya
</details>

### Advanced Level (Hard) ⭐⭐⭐

**Q11: Race condition kya hai aur signal handler mein kaise avoid kiya?**
<details>
<summary>Answer</summary>
Race condition tab hota hai jab multiple processes/signals simultaneously same resource access karte hain. Signal handler mein sirf reentrant functions use karne chahiye (printf technically unsafe hai but simple cases mein OK). Better approach hota signal flag set karna aur main loop mein check karna. SIGCHLD ko ignore kiya race conditions avoid karne ke liye.
</details>

**Q12: Shell initialization order important kyu hai? Galat order se kya problem hoga?**
<details>
<summary>Answer</summary>
Order critical hai:
1. **Signals pehle** - Kyunki baad ke operations ko interrupt ho sakta hai
2. **History next** - Commands execute hone se pehle ready hona chahiye
3. **Jobs array** - Background processes ke liye ready
4. **Welcome message last** - Sab setup hone ke baad

Galat order: History load se pehle command execute karne se history mein nahi aayega.
</details>

**Q13: `fgets()` vs `scanf()` - tumne fgets kyu choose kiya input ke liye?**
<details>
<summary>Answer</summary>
`fgets()` better hai kyunki:
- Buffer overflow protection hai (MAX_CMD_LEN)
- Spaces aur special characters handle karta hai
- Newline character include karta hai (jo hum remove kar sakte hain)
- `scanf()` whitespace par break karta hai

Shell ke liye `fgets()` ideal hai kyunki commands mein spaces hote hain.
</details>

**Q14: EOF (End of File) detection kaise kaam karta hai aur kyu important hai?**
<details>
<summary>Answer</summary>
EOF detection `fgets()` return value check karke hota hai:
- Normal input: valid string pointer return
- EOF (Ctrl+D): NULL return

Importance:
- Graceful exit mechanism provide karta hai
- `exit` command bina bhi shell close kar sakte hain
- Script files ke liye important (file end par auto-exit)
- Return 0 se check karte hain loop break karne ke liye
</details>

**Q15: Shell lifecycle explain karo - start se end tak kya hota hai?**
<details>
<summary>Answer</summary>
**Complete Lifecycle:**

1. **Startup Phase:**
   - `main()` execute starts
   - `init_shell()` call
   - Signal handlers register
   - History load from `.history` file
   - Jobs array initialize (all slots empty)
   - Welcome message display

2. **Running Phase (Loop):**
   - Print prompt with current directory
   - Wait for user input (`read_command()`)
   - Trim input, check empty
   - Add to history
   - Detect pipeline vs single command
   - Parse command (tokenize + redirection)
   - Execute command (builtin/external/pipeline)
   - Cleanup completed background jobs
   - Repeat

3. **Exit Phase:**
   - User types `exit` or presses Ctrl+D
   - `cleanup_shell()` call
   - Save history to file
   - Free all allocated memory
   - Exit with status code 0

4. **Signal Handling (Async):**
   - Can happen anytime during running phase
   - Ctrl+C → SIGINT → print newline + prompt
   - Ctrl+Z → SIGTSTP → print newline + prompt
   - Child dies → SIGCHLD → ignored
</details>

---

## 🏆 Key Achievements
1. ✅ Shell ka complete lifecycle management
2. ✅ Robust signal handling implementation
3. ✅ Main loop ka clean architecture
4. ✅ Memory management aur cleanup
5. ✅ User-friendly prompt aur error handling

## 📚 Technologies Used
- C Programming
- Unix System Calls (signal, getcwd, fgets)
- Process Management
- Signal Handling
- Memory Management

---

**Note:** Abhishek ne shell ka backbone design kiya - initialization se lekar main loop, signal handling, aur cleanup tak sab kuch. Shell ka core logic aur flow control unka main contribution hai.

