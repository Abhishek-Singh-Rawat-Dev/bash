# 🎯 VEDANSH - Executor & Pipeline Manager Lead

## 📋 Role Assignment
**Position:** Command Execution & Pipeline Architecture Expert  
**Primary Responsibility:** Command execution, pipeline management, builtin commands, aur process control

---

## 🔥 Main Contributions

### 1️⃣ Executor.c - Command Execution Engine (152 lines)

#### **Lines 1-5: Header Includes**
```c
#include "headers/executor.h"
#include "headers/builtin.h"
#include "headers/pipeline.h"
#include "headers/jobs.h"
#include "headers/utils.h"
```
**Hinglish Explanation:**
- `executor.h` - Command execution ke functions
- `builtin.h` - Built-in commands (cd, pwd, etc.)
- `pipeline.h` - Pipeline operations ke liye
- `jobs.h` - Background job management
- `utils.h` - Helper utilities

#### **Lines 8-19: Execute Single Command**
```c
int execute_single_command(command_t *cmd) {
    if (!cmd || !cmd->args || cmd->argc == 0) {
        return 1;
    }
    
    // Check if it's a built-in command
    if (is_builtin(cmd->args[0])) {
        return execute_builtin(cmd);
    } else {
        return execute_external(cmd);
    }
}
```
**Hinglish Explanation:**
- **NULL checks:** Pehle validate karo command valid hai
- **Builtin check:** Command builtin hai (cd, pwd) ya external (ls, grep)?
- **Routing:**
  - Builtin → internal function call (no fork)
  - External → fork + exec mechanism
- Return value: 0 = success, 1 = failure

#### **Lines 22-38: Pipeline Executor Wrapper**
```c
int execute_pipeline(char **commands, int count) {
    if (count <= 0) return 1;
    
    // If only one command, execute normally
    if (count == 1) {
        command_t *cmd = parse_command(commands[0]);
        if (cmd) {
            int result = execute_single_command(cmd);
            free_command(cmd);
            return result;
        }
        return 1;
    }
    
    // Execute pipeline
    return execute_pipeline_commands(commands, count);
}
```
**Hinglish Explanation:**
- **Validation:** Command count check
- **Single command optimization:**
  - Agar sirf ek command to pipeline logic skip karo
  - Normal execution use karo (faster)
- **Multi-command pipeline:**
  - `execute_pipeline_commands()` call karo
  - Ye complex pipe setup karega
- Example: `"ls | grep txt"` → count=2 → pipeline execution

#### **Lines 41-67: Builtin Command Router**
```c
int execute_builtin(command_t *cmd) {
    if (!cmd || !cmd->args || cmd->argc == 0) {
        return 1;
    }
    
    char *command = cmd->args[0];
    
    if (strcmp(command, "cd") == 0) {
        return builtin_cd(cmd);
    } else if (strcmp(command, "pwd") == 0) {
        return builtin_pwd(cmd);
    } else if (strcmp(command, "echo") == 0) {
        return builtin_echo(cmd);
    } else if (strcmp(command, "exit") == 0) {
        return builtin_exit(cmd);
    } else if (strcmp(command, "history") == 0) {
        return builtin_history(cmd);
    } else if (strcmp(command, "jobs") == 0) {
        return builtin_jobs(cmd);
    } else if (strcmp(command, "fg") == 0) {
        return builtin_fg(cmd);
    } else if (strcmp(command, "bg") == 0) {
        return builtin_bg(cmd);
    }
    
    return 1;
}
```
**Hinglish Explanation:**
- **Command routing:** Har builtin command ko uske handler pe route karta hai
- **strcmp():** Command name compare karke decide karta hai
- **Built-in commands:**
  - **Basic:** cd, pwd, echo, exit
  - **Advanced:** history, jobs, fg, bg
- **Why no fork?** Builtins shell ke state change karte hain (cd changes directory)
- Return har function ka result

#### **Lines 70-106: External Command Execution (Critical)**
```c
int execute_external(command_t *cmd) {
    if (!cmd || !cmd->args || cmd->argc == 0) {
        return 1;
    }
    
    pid_t pid = fork();
    
    if (pid == 0) {
        // Child process
        // Set up redirection
        setup_redirection(cmd);
        
        // Execute command
        if (execvp(cmd->args[0], cmd->args) == -1) {
            print_error_with_errno("Command not found");
            exit(1);
        }
    } else if (pid > 0) {
        // Parent process
        if (cmd->background) {
            // Background job
            add_job(pid, cmd->args[0]);
            printf("[%d] %d\n", current_job_id, pid);
        } else {
            // Foreground job
            int status;
            waitpid(pid, &status, 0);
            return WEXITSTATUS(status);
        }
    } else {
        // Fork failed
        print_error_with_errno("Fork failed");
        return 1;
    }
    
    return 0;
}
```
**Hinglish Explanation:**

**fork() - Process Creation:**
- New child process banata hai (exact copy of parent)
- Returns: 0 in child, child's PID in parent, -1 on error

**Child Process Block (pid == 0):**
- **setup_redirection():** Input/output files configure
- **execvp():** Current process ko new program se replace kar do
  - `cmd->args[0]` - Program name (e.g., "ls")
  - `cmd->args` - Complete arguments array
  - PATH environment variable mein search hota hai
- Agar exec fail to error print karke exit

**Parent Process Block (pid > 0):**
- **Background execution:**
  - Job list mein add karo
  - Job ID aur PID print karo
  - Continue without waiting
- **Foreground execution:**
  - `waitpid()` se wait karo child complete hone tak
  - Exit status return karo

**Fork Failed (pid < 0):**
- Error print karo aur return 1

#### **Lines 109-151: Redirection Setup (File I/O)**
```c
void setup_redirection(command_t *cmd) {
    if (!cmd) return;
    
    // Input redirection
    if (cmd->input_file) {
        int fd = open(cmd->input_file, O_RDONLY);
        if (fd == -1) {
            print_error_with_errno("Cannot open input file");
            exit(1);
        }
        dup2(fd, STDIN_FILENO);
        close(fd);
    }
    
    // Output redirection
    if (cmd->output_file) {
        int flags = O_WRONLY | O_CREAT;
        if (cmd->append_output) {
            flags |= O_APPEND;
        } else {
            flags |= O_TRUNC;
        }
        
        int fd = open(cmd->output_file, flags, 0644);
        if (fd == -1) {
            print_error_with_errno("Cannot open output file");
            exit(1);
        }
        dup2(fd, STDOUT_FILENO);
        close(fd);
    }
    
    // Error redirection
    if (cmd->error_file) {
        int fd = open(cmd->error_file, O_WRONLY | O_CREAT | O_TRUNC, 0644);
        if (fd == -1) {
            print_error_with_errno("Cannot open error file");
            exit(1);
        }
        dup2(fd, STDERR_FILENO);
        close(fd);
    }
}
```
**Hinglish Explanation:**

**Input Redirection (<):**
- `open()` file ko read mode mein kholo
- `dup2(fd, STDIN_FILENO)` - stdin ko file se replace karo
- Ab command file se read karega instead of keyboard
- Original fd close kar do (duplicate ban gaya)

**Output Redirection (> and >>):**
- **Flags setup:**
  - O_WRONLY - Write only mode
  - O_CREAT - File create kar do agar exist nahi
  - O_APPEND - End mein add karo (>>)
  - O_TRUNC - File overwrite karo (>)
- **0644 permissions:** Owner read/write, others read only
- `dup2(fd, STDOUT_FILENO)` - stdout ko file se replace
- Output file mein jayega ab

**Error Redirection (2>):**
- Similar to output but STDERR_FILENO use
- Error messages separate file mein ja sakte hain

**Example:** `cmd < in.txt > out.txt 2> err.txt`
- stdin ← in.txt
- stdout → out.txt
- stderr → err.txt

---

### 2️⃣ Pipeline.c - Inter-Process Communication (135 lines)

#### **Lines 7-102: Complete Pipeline Execution**
```c
int execute_pipeline_commands(char **commands, int count) {
    if (count <= 0) return 1;
    
    pid_t *pids = malloc(count * sizeof(pid_t));
    int **pipes = malloc((count - 1) * sizeof(int*));
    
    if (!pids || !pipes) {
        print_error("Memory allocation failed");
        if (pids) free(pids);
        if (pipes) free(pipes);
        return 1;
    }
```
**Hinglish Explanation:**
- **pids array:** Har command ke process ID store karne ke liye
- **pipes array:** Commands ke beech data transfer ke liye
- N commands → (N-1) pipes chahiye
- Example: `cmd1 | cmd2 | cmd3` → 3 commands, 2 pipes

#### **Lines 20-32: Pipe Creation Loop**
```c
    // Create pipes
    for (int i = 0; i < count - 1; i++) {
        pipes[i] = malloc(2 * sizeof(int));
        if (!pipes[i] || pipe(pipes[i]) == -1) {
            print_error_with_errno("Pipe creation failed");
            for (int j = 0; j <= i; j++) {
                if (pipes[j]) free(pipes[j]);
            }
            free(pipes);
            free(pids);
            return 1;
        }
    }
```
**Hinglish Explanation:**
- **pipe():** Creates two file descriptors
  - `pipes[i][0]` - Read end (data nikalna)
  - `pipes[i][1]` - Write end (data daalna)
- Har pipe 2 adjacent commands ko connect karta hai
- **Error handling:** Agar ek bhi pipe fail to sab cleanup

#### **Lines 35-80: Fork Loop aur Process Setup**
```c
    // Fork processes for each command
    for (int i = 0; i < count; i++) {
        pids[i] = fork();
        
        if (pids[i] == 0) {
            // Child process
            // Set up input pipe (except for first command)
            if (i > 0) {
                dup2(pipes[i-1][0], STDIN_FILENO);
            }
            
            // Set up output pipe (except for last command)
            if (i < count - 1) {
                dup2(pipes[i][1], STDOUT_FILENO);
            }
            
            // Close all pipes in child
            for (int j = 0; j < count - 1; j++) {
                close(pipes[j][0]);
                close(pipes[j][1]);
            }
            
            // Parse and execute command
            command_t *cmd = parse_command(commands[i]);
            if (cmd) {
                if (is_builtin(cmd->args[0])) {
                    execute_builtin(cmd);
                } else {
                    execvp(cmd->args[0], cmd->args);
                    print_error_with_errno("Command not found");
                }
                free_command(cmd);
            }
            exit(1);
        }
    }
```
**Hinglish Explanation:**

**Pipeline Flow:** cmd1 → pipe1 → cmd2 → pipe2 → cmd3

**For each command i:**

**Input Setup (i > 0):**
- First command ko skip (keyboard se input)
- Baaki commands previous pipe se input lete hain
- `dup2(pipes[i-1][0], STDIN_FILENO)`

**Output Setup (i < count-1):**
- Last command ko skip (screen pe output)
- Baaki commands next pipe mein output dete hain
- `dup2(pipes[i][1], STDOUT_FILENO)`

**Close all pipes:**
- Child mein sab pipe fds close karo
- Kyunki dup2 ne copies bana liye

**Execute:**
- Command parse karo
- Builtin ya external execute karo
- Exit (child process end)

#### **Lines 82-100: Parent Process Cleanup aur Wait**
```c
    // Close all pipes in parent
    for (int i = 0; i < count - 1; i++) {
        close(pipes[i][0]);
        close(pipes[i][1]);
        free(pipes[i]);
    }
    free(pipes);
    
    // Wait for all processes
    int status;
    int exit_code = 0;
    for (int i = 0; i < count; i++) {
        waitpid(pids[i], &status, 0);
        if (i == count - 1) { // Last command's exit code
            exit_code = WEXITSTATUS(status);
        }
    }
    
    free(pids);
    return exit_code;
}
```
**Hinglish Explanation:**
- **Parent mein pipes close:** Children use kar rahe hain
- **Memory free:** Pipes array cleanup
- **Wait loop:** Sabhi children complete hone tak wait
- **Exit code:** Last command ka status return (pipeline convention)
- **Cleanup:** PIDs array free

---

### 3️⃣ Builtin.c - Internal Commands (269 lines)

#### **Lines 7-36: CD Command (Change Directory)**
```c
int builtin_cd(command_t *cmd) {
    char *dir = NULL;
    
    if (cmd->argc > 1) {
        dir = cmd->args[1];
    } else {
        // Default to home directory
        dir = getenv("HOME");
        if (!dir) {
            print_error("cd: HOME not set");
            return 1;
        }
    }
    
    // Expand tilde if present
    char *expanded_dir = expand_tilde(dir);
    if (!expanded_dir) {
        print_error("cd: Memory allocation failed");
        return 1;
    }
    
    if (chdir(expanded_dir) == -1) {
        print_error_with_errno("cd");
        free(expanded_dir);
        return 1;
    }
    
    free(expanded_dir);
    return 0;
}
```
**Hinglish Explanation:**
- **No argument:** HOME directory mein jao
- **With argument:** Specified directory mein jao
- **Tilde expansion:** `~` ko `/home/user` se replace
- **chdir():** System call directory change karne ke liye
- **Why builtin?** Kyunki child process mein cd karne se parent effect nahi hoga

#### **Lines 39-49: PWD Command**
```c
int builtin_pwd(command_t *cmd) {
    (void)cmd;
    char cwd[1024];
    if (getcwd(cwd, sizeof(cwd)) != NULL) {
        printf("%s\n", cwd);
        return 0;
    } else {
        print_error_with_errno("pwd");
        return 1;
    }
}
```
**Hinglish Explanation:**
- `getcwd()` - Current working directory ka path
- Buffer mein path store hota hai
- Success par print kar do
- Simple command, direct implementation

#### **Lines 52-61: Echo Command**
```c
int builtin_echo(command_t *cmd) {
    for (int i = 1; i < cmd->argc; i++) {
        printf("%s", cmd->args[i]);
        if (i < cmd->argc - 1) {
            printf(" ");
        }
    }
    printf("\n");
    return 0;
}
```
**Hinglish Explanation:**
- Loop through all arguments
- Print each with space between
- Last mein newline
- Example: `echo hello world` → "hello world\n"

#### **Lines 100-113: FG Command (Foreground)**
```c
int builtin_fg(command_t *cmd) {
    if (cmd->argc < 2) {
        print_error("fg: job number required");
        return 1;
    }
    
    int job_id = atoi(cmd->args[1]);
    if (job_id <= 0) {
        print_error("fg: Invalid job number");
        return 1;
    }
    
    return resume_job(job_id, 1); // 1 for foreground
}
```
**Hinglish Explanation:**
- Background job ko foreground mein laata hai
- Job number argument mein hota hai
- `atoi()` string ko integer mein convert
- `resume_job()` call with foreground flag

---

## 🎓 VIVA QUESTIONS (Vedansh Ke Liye)

### Basic Level (Easy) ⭐

**Q1: fork() function kya karta hai?**
<details>
<summary>Answer</summary>
fork() current process ka exact copy (child process) create karta hai. Return values:
- 0 in child process
- Child's PID in parent process
- -1 on error
</details>

**Q2: execvp() aur exec() family explain karo**
<details>
<summary>Answer</summary>
execvp() current process ko new program se replace karta hai:
- 'v' - vector/array of arguments
- 'p' - PATH environment variable mein search
- Successful exec() ke baad code return nahi hota
</details>

**Q3: dup2() function ka kya use hai?**
<details>
<summary>Answer</summary>
dup2(oldfd, newfd) oldfd ko newfd se replace karta hai. Redirection ke liye use hota hai:
- stdin (0), stdout (1), stderr (2) ko files se replace
- Example: `dup2(file_fd, STDOUT_FILENO)` - output file mein jayega
</details>

**Q4: Pipe kya hai aur kaise kaam karta hai?**
<details>
<summary>Answer</summary>
Pipe ek communication channel hai do processes ke beech:
- `pipe()` creates two file descriptors
- pipes[0] - read end
- pipes[1] - write end
- Ek process write kare, doosra read kare
</details>

**Q5: Builtin vs External command mein kya difference hai?**
<details>
<summary>Answer</summary>
**Builtin:** Shell ke andar implement (cd, pwd, exit)
- No fork required
- Shell state change kar sakte hain
- Faster execution

**External:** Separate programs (ls, grep, cat)
- fork + exec required
- Separate process mein run
</details>

### Intermediate Level (Medium) ⭐⭐

**Q6: Zombie process kya hai aur kaise avoid karte hain?**
<details>
<summary>Answer</summary>
**Zombie:** Child process terminate ho gaya but parent ne `wait()` nahi kiya. Entry process table mein rehti hai.

**Avoidance:**
- Parent mein `waitpid()` call
- SIGCHLD handler set karo
- Periodic cleanup_completed_jobs()

Code:
```c
waitpid(pid, &status, WNOHANG);
```
</details>

**Q7: File descriptors 0, 1, 2 ka kya significance hai?**
<details>
<summary>Answer</summary>
- **0 (STDIN_FILENO):** Standard Input - keyboard
- **1 (STDOUT_FILENO):** Standard Output - screen
- **2 (STDERR_FILENO):** Standard Error - error messages

Redirection mein ye replace hote hain files se.
</details>

**Q8: Pipeline mein sabhi pipes parent aur child dono mein close kyu karte hain?**
<details>
<summary>Answer</summary>
**Pipe ka rule:** Read end tab tak block hota hai jab tak write end open hai.

**Problem without closing:**
- Commands complete ho gaye but pipes open
- Read operations hang ho jayenge
- EOF signal nahi milega

**Solution:**
- Children: Unused pipes close
- Parent: Sabhi pipes close (children ke copies hain)
</details>

**Q9: Background vs Foreground job execution mein kya difference hai?**
<details>
<summary>Answer</summary>
**Foreground:**
- Shell wait karta hai (`waitpid()`)
- User input block hota hai
- Output directly terminal pe
- Ctrl+C signal jaata hai

**Background:**
- Shell wait nahi karta
- Job list mein add hota hai
- Prompt turant wapas aata hai
- Output terminal pe (async)
- Symbol: `&`
</details>

**Q10: cd command builtin kyu hai, external kyu nahi?**
<details>
<summary>Answer</summary>
**Reason:** Directory change parent shell mein hona chahiye.

**Agar external hota:**
```c
fork();
if (child) {
    chdir("/home");  // Only child's directory changes
    exit();
}
// Parent's directory unchanged!
```

Builtin: No fork, direct `chdir()` in parent process.
</details>

### Advanced Level (Hard) ⭐⭐⭐

**Q11: Complex pipeline execute karo: `cat file.txt | grep error | wc -l > count.txt`**
<details>
<summary>Answer</summary>
**Complete Execution Flow:**

**Setup Phase:**
- 3 commands → 2 pipes needed
- pipe1: cat → grep
- pipe2: grep → wc

**Process 0 (cat file.txt):**
```c
// No input redirection (first command)
dup2(pipe1[1], STDOUT_FILENO);  // Output to pipe1
close all pipe fds
execvp("cat", ["cat", "file.txt"])
```

**Process 1 (grep error):**
```c
dup2(pipe1[0], STDIN_FILENO);   // Input from pipe1
dup2(pipe2[1], STDOUT_FILENO);  // Output to pipe2
close all pipe fds
execvp("grep", ["grep", "error"])
```

**Process 2 (wc -l > count.txt):**
```c
dup2(pipe2[0], STDIN_FILENO);   // Input from pipe2
// Output redirection handled by setup_redirection()
open("count.txt", O_WRONLY | O_CREAT | O_TRUNC)
dup2(fd, STDOUT_FILENO);
close all pipe fds
execvp("wc", ["wc", "-l"])
```

**Parent Process:**
- Close all pipes (children using them)
- waitpid() for all 3 processes
- Return exit code of last command (wc)

**Data Flow:**
file.txt → cat → pipe1 → grep → pipe2 → wc → count.txt
</details>

**Q12: Race conditions pipeline execution mein kahan ho sakte hain?**
<details>
<summary>Answer</summary>
**Potential Race Conditions:**

1. **Pipe closing order:**
```c
// BAD: Close before fork
close(pipes[i][0]);
fork();

// GOOD: Close after all forks
fork();
// ... all children created
close(pipes[i][0]);
```

2. **Signal handling:**
- SIGCHLD during fork loop
- Use SIGCHLD ignore or proper handler

3. **File descriptor leaks:**
- Child inherits all parent fds
- Close unnecessary fds in child

4. **Waitpid order:**
- Wait for all children
- Don't leave zombies

**Prevention:**
- Proper fd management
- Signal blocking during critical sections
- Consistent error handling
</details>

**Q13: execvp() failure handling aur error recovery explain karo**
<details>
<summary>Answer</summary>
**Execution Flow:**

```c
if (execvp(cmd->args[0], cmd->args) == -1) {
    // Only reaches here if exec fails
    print_error_with_errno("Command not found");
    exit(1);  // MUST exit child
}
// Never reached on success
```

**Common Errors:**
1. **ENOENT:** Command not found in PATH
2. **EACCES:** Permission denied
3. **ENOEXEC:** Not executable

**Why exit(1)?**
- exec failed means child still running as shell copy
- Continuing will run parent code twice
- MUST terminate child immediately

**Error Recovery:**
- Print descriptive message
- Exit with non-zero status
- Parent detects failure via WEXITSTATUS()

**Better Error Handling:**
```c
switch (errno) {
    case ENOENT:
        fprintf(stderr, "%s: command not found\n", cmd->args[0]);
        break;
    case EACCES:
        fprintf(stderr, "%s: permission denied\n", cmd->args[0]);
        break;
}
exit(127);  // Standard shell convention
```
</details>

**Q14: Memory leaks pipeline execution mein kaise prevent karte hain?**
<details>
<summary>Answer</summary>
**Memory Allocation Points:**

1. **PIDs array:**
```c
pid_t *pids = malloc(count * sizeof(pid_t));
// ... use ...
free(pids);  // End mein
```

2. **Pipes array:**
```c
int **pipes = malloc((count-1) * sizeof(int*));
for (int i = 0; i < count-1; i++) {
    pipes[i] = malloc(2 * sizeof(int));
}
// ... use ...
for (int i = 0; i < count-1; i++) {
    free(pipes[i]);
}
free(pipes);
```

3. **Parsed commands:**
```c
command_t *cmd = parse_command(commands[i]);
// ... use ...
free_command(cmd);  // Must call before exit
```

**Child Process:**
- Inherited memory ko explicitly free
- exit() pe sab automatic free (OS cleans up)

**Parent Process:**
- Sabhi arrays free
- Loop error handling mein bhi free

**Valgrind Check:**
```bash
valgrind --leak-check=full ./mini-bash
```
</details>

**Q15: Process group aur terminal control explain karo (fg/bg commands)**
<details>
<summary>Answer</summary>
**Process Groups:**
- Har job ek process group hota hai
- Process Group ID (PGID) se identify
- Signals entire group ko bheji ja sakti hain

**Terminal Control:**
- Ek time pe ek foreground process group
- `tcsetpgrp()` control change karta hai

**FG Command Flow:**
```c
int builtin_fg(command_t *cmd) {
    job_t *job = find_job(job_id);
    
    // 1. Resume if stopped
    if (job->status == STOPPED) {
        kill(job->pid, SIGCONT);
    }
    
    // 2. Give terminal control
    tcsetpgrp(STDIN_FILENO, getpgid(job->pid));
    
    // 3. Wait for completion
    waitpid(job->pid, &status, WUNTRACED);
    
    // 4. Check if stopped again (Ctrl+Z)
    if (WIFSTOPPED(status)) {
        job->status = STOPPED;
    } else {
        remove_job(job->pid);
    }
    
    // 5. Restore shell control
    tcsetpgrp(STDIN_FILENO, getpgrp());
}
```

**BG Command:**
- Just send SIGCONT
- Don't wait
- Don't change terminal control

**Job States:**
- Running (foreground)
- Running (background)
- Stopped (Ctrl+Z)
- Completed
</details>

---

## 🏆 Key Achievements
1. ✅ Complete command execution engine (builtin + external)
2. ✅ Full pipeline implementation with IPC
3. ✅ Process management (fork, exec, wait)
4. ✅ I/O redirection (stdin, stdout, stderr)
5. ✅ Job control (background, foreground, stop, resume)
6. ✅ 8+ builtin commands implementation

## 📚 Technologies Used
- C Programming
- Unix System Calls (fork, exec, pipe, dup2, waitpid)
- Process Management & IPC
- File Descriptors & I/O Redirection
- Signal Handling (SIGCONT, SIGTSTP)
- Terminal Control (tcsetpgrp)

---

**Note:** Vedansh ne executor aur pipeline ka complete implementation kiya - simple command execution se lekar complex multi-process pipelines tak. Process management aur inter-process communication unka core expertise hai.

