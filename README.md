# Advanced Mini Bash Shell (Phase 2)

A comprehensive, modular C implementation of a UNIX-like shell with advanced features including pipelines, redirection, background execution, job control, and command history.

## 🚀 Features

### ✅ Core Functionality
- **Command Execution**: Execute system commands like `ls`, `cat`, `ps`, etc.
- **Built-in Commands**: `cd`, `pwd`, `echo`, `exit`, `history`, `jobs`, `fg`, `bg`
- **I/O Redirection**: Input (`<`), Output (`>`), Append (`>>`), Error (`2>`)
- **Pipelines**: Command chaining with `|` operator
- **Background Processes**: Commands ending with `&` run in background
- **Job Control**: Manage background jobs with `jobs`, `fg`, `bg`
- **Command History**: Persistent history stored in `.history` file
- **Signal Handling**: Graceful handling of Ctrl+C and Ctrl+Z

### 🏗️ Architecture

The shell is built with a modular architecture:

```
mini-bash/
├── headers/           # Header files
│   ├── shell.h       # Main shell definitions
│   ├── parser.h      # Command parsing
│   ├── executor.h    # Command execution
│   ├── builtin.h     # Built-in commands
│   ├── redirection.h # I/O redirection
│   ├── pipeline.h    # Pipeline handling
│   ├── jobs.h        # Job management
│   ├── history.h     # Command history
│   └── utils.h       # Utility functions
├── main.c            # Entry point and main loop
├── parser.c          # Command parsing and tokenization
├── executor.c        # Command execution logic
├── builtin.c         # Built-in command implementations
├── redirection.c     # I/O redirection handling
├── pipeline.c        # Pipeline command execution
├── jobs.c            # Background job management
├── history.c         # Command history management
├── utils.c           # Helper utilities
└── Makefile          # Build configuration
```

## 🛠️ Building and Running

### Prerequisites
- GCC compiler
- Make
- POSIX-compliant system (Linux, macOS, etc.)

### Build
```bash
make clean && make
```

### Run
```bash
./mini-bash
```

### Available Make Targets
- `make` - Build the shell
- `make clean` - Remove build artifacts
- `make debug` - Build with debug symbols
- `make release` - Build optimized release version
- `make run` - Build and run the shell
- `make test` - Run basic tests
- `make install` - Install to /usr/local/bin/
- `make uninstall` - Remove from /usr/local/bin/

## 📖 Usage Examples

### Basic Commands
```bash
mini-bash$ pwd
/Users/username/project

mini-bash$ ls -la
total 48
drwxr-xr-x  8 username  staff   256 Dec 10 10:30 .
drwxr-xr-x  3 username  staff    96 Dec 10 10:29 ..
-rw-r--r--  1 username  staff  1234 Dec 10 10:30 README.md
...

mini-bash$ echo "Hello, World!"
Hello, World!
```

### I/O Redirection
```bash
# Output redirection
mini-bash$ echo "Hello" > output.txt
mini-bash$ cat output.txt
Hello

# Input redirection
mini-bash$ sort < input.txt

# Append redirection
mini-bash$ echo "World" >> output.txt
mini-bash$ cat output.txt
Hello
World

# Error redirection
mini-bash$ ls nonexistent 2> error.log
```

### Pipelines
```bash
# Simple pipeline
mini-bash$ ls | grep .c
main.c
parser.c
executor.c

# Complex pipeline
mini-bash$ cat file.txt | sort | uniq | wc -l
42
```

### Background Jobs
```bash
# Run command in background
mini-bash$ sleep 10 &
[1] 12345

# List background jobs
mini-bash$ jobs
Job ID  PID     Status  Command
------  ---     ------  -------
[1]     12345   Running sleep 10

# Bring job to foreground
mini-bash$ fg 1

# Resume job in background
mini-bash$ bg 1
```

### Command History
```bash
# View command history
mini-bash$ history
1       pwd
2       ls -la
3       echo "Hello"
4       history

# View last 5 commands
mini-bash$ history 5
```

## 🔧 Built-in Commands

| Command | Description | Usage |
|---------|-------------|-------|
| `cd` | Change directory | `cd [directory]` |
| `pwd` | Print working directory | `pwd` |
| `echo` | Print text | `echo [text]` |
| `exit` | Exit shell | `exit [code]` |
| `history` | Show command history | `history [count]` |
| `jobs` | List background jobs | `jobs` |
| `fg` | Bring job to foreground | `fg [job_id]` |
| `bg` | Resume job in background | `bg [job_id]` |

## 🏗️ Technical Implementation

### Key System Calls Used
- `fork()` - Create child processes
- `execvp()` - Execute external commands
- `waitpid()` - Wait for child processes
- `pipe()` - Create pipes for pipelines
- `dup2()` - Redirect file descriptors
- `open()`, `close()` - File operations
- `signal()` - Signal handling

### Data Structures
- `command_t` - Command structure with args, redirection info
- `job_t` - Background job tracking
- Dynamic arrays for command history and job management

### Memory Management
- Dynamic memory allocation with proper cleanup
- String duplication for safe manipulation
- Array management for tokens and commands

## 🧪 Testing

The shell includes comprehensive testing capabilities:

```bash
# Run basic tests
make test

# Test specific features
echo "ls | grep .c" | ./mini-bash
echo "echo 'test' > file.txt" | ./mini-bash
echo "jobs" | ./mini-bash
```

## 🐛 Known Issues

1. **Redirection Parsing**: Some edge cases in redirection parsing may need refinement
2. **Signal Handling**: Advanced signal handling could be enhanced
3. **Error Recovery**: Some error conditions could have better recovery mechanisms

## 🔮 Future Enhancements

- Tab completion
- Command aliases
- Environment variable expansion
- Advanced job control (job suspension/resumption)
- Custom prompt configuration
- Script execution support

## 📝 License

This project is created for educational purposes. Feel free to use and modify as needed.

## 🤝 Contributing

This is a learning project, but suggestions and improvements are welcome!

---

**Advanced Mini Bash Shell v2.0** - A comprehensive C implementation of a UNIX-like shell with modern features.
# bash
