# 🎯 MINI BASH SHELL PROJECT - TEAM ROLES & DOCUMENTATION

## 👥 Project Team

Ye project 4 talented developers ne milkar banaya hai. Har ek ne apne expertise ke hisaab se different components handle kiye hain.

---

## 📚 Individual Role Documentation

### 1. [ABHISHEK - Shell Core & Main Loop Lead](./ABHISHEK_ROLE.md)

**Role:** Shell Core Architecture & Main Loop Developer  
**Components:**

- Main loop implementation (`main.c`)
- Shell initialization aur cleanup
- Signal handling (Ctrl+C, Ctrl+Z)
- Job management data structures
- Shell lifecycle management

**Key Files:** `main.c`, `headers/shell.h`

---

### 2. [KRISHNA - Parser & Command Processing Lead](./KRISHNA_ROLE.md)

**Role:** Parser & Tokenization Architect  
**Components:**

- Command parsing (`parser.c`)
- Tokenization logic
- Redirection handling (`<`, `>`, `>>`, `2>`)
- Pipeline detection
- Background execution parsing

**Key Files:** `parser.c`, `headers/parser.h`

---

### 3. [VEDANSH - Executor & Pipeline Manager Lead](./VEDANSH_ROLE.md)

**Role:** Command Execution & Pipeline Architecture Expert  
**Components:**

- Command execution (`executor.c`)
- Pipeline implementation (`pipeline.c`)
- Builtin commands (`builtin.c`)
- Process management (fork, exec, wait)
- I/O redirection setup
- Job control (fg, bg)

**Key Files:** `executor.c`, `pipeline.c`, `builtin.c`, `jobs.c`, `history.c`

---

### 4. [PANKAJ - Backend & AI Integration Lead](./PANKAJ_ROLE.md)

**Role:** Full-Stack Backend Architect & AI Integration Expert  
**Components:**

- Flask backend API (`backend/app.py`)
- Gemini AI integration
- Natural language processing
- WebSocket communication
- React frontend (`frontend/src/App.js`)
- File system search
- Command history tracking

**Key Files:** `backend/app.py`, `frontend/src/App.js`, `frontend/src/components/*`

---

## 🎓 Viva Preparation

Har role file mein 15 comprehensive viva questions hain:

- **5 Basic Level** ⭐ - Fundamentals samajhne ke liye
- **5 Intermediate Level** ⭐⭐ - Deep understanding check karne ke liye
- **5 Advanced Level** ⭐⭐⭐ - Expert level knowledge ke liye

### Topics Covered:

#### Abhishek's Questions:

- Signal handling
- Main loop architecture
- Shell lifecycle
- Memory management
- Job control basics

#### Krishna's Questions:

- Parsing algorithms
- Tokenization
- Redirection precedence
- Pipeline splitting
- Memory-safe string operations

#### Vedansh's Questions:

- Process management (fork, exec, wait)
- Pipeline IPC (Inter-Process Communication)
- File descriptors & I/O
- Builtin vs external commands
- Job control (fg, bg)

#### Pankaj's Questions:

- Flask REST API
- WebSocket communication
- AI prompt engineering
- React lifecycle
- Full-stack architecture

---

## 📊 Project Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                     USER INTERFACE                          │
│                   (React Frontend)                          │
│                   - Terminal Display                        │
│                   - Command Input                           │
│                   - Status Bar                              │
└──────────────────────┬──────────────────────────────────────┘
                       │ HTTP / WebSocket
                       │
┌──────────────────────▼──────────────────────────────────────┐
│                   BACKEND SERVER                            │
│                   (Flask + SocketIO)                        │
│                                                             │
│  ┌─────────────────────────────────────────────────────┐  │
│  │  Gemini AI Integration                              │  │
│  │  - Natural Language → Command                       │  │
│  │  - Intelligent Suggestions                          │  │
│  └─────────────────────────────────────────────────────┘  │
│                       │                                     │
│  ┌────────────────────▼────────────────────────────────┐  │
│  │  Command Processor                                   │  │
│  │  - File Search                                       │  │
│  │  - Executor Selection                                │  │
│  └────────────────────┬────────────────────────────────┘  │
└─────────────────────────┼───────────────────────────────────┘
                          │
            ┌─────────────┴──────────────┐
            │                            │
┌───────────▼──────────┐    ┌───────────▼──────────┐
│   Mini-Bash Shell    │    │  System Terminal     │
│   (C Implementation) │    │  (macOS/Linux)       │
│                      │    │                      │
│  ┌────────────────┐ │    │  Native Commands     │
│  │ Parser         │ │    │  Full OS Access      │
│  └────────────────┘ │    │                      │
│  ┌────────────────┐ │    └──────────────────────┘
│  │ Executor       │ │
│  └────────────────┘ │
│  ┌────────────────┐ │
│  │ Pipeline       │ │
│  └────────────────┘ │
│  ┌────────────────┐ │
│  │ Builtin Cmds   │ │
│  └────────────────┘ │
└──────────────────────┘
```

---

## 🔥 Key Features Implemented

### Core Shell (Abhishek + Krishna + Vedansh):

- ✅ Command parsing with tokenization
- ✅ Pipeline support (`cmd1 | cmd2 | cmd3`)
- ✅ I/O Redirection (`<`, `>`, `>>`, `2>`)
- ✅ Background execution (`&`)
- ✅ 8+ builtin commands (cd, pwd, echo, history, jobs, fg, bg, exit)
- ✅ Signal handling (Ctrl+C, Ctrl+Z)
- ✅ Job control
- ✅ Command history with file persistence

### AI-Powered Backend (Pankaj):

- ✅ Natural language command conversion
- ✅ Gemini AI integration
- ✅ Smart file search across system
- ✅ Fallback mechanism (AI → Hardcoded → System)
- ✅ WebSocket real-time updates
- ✅ RESTful API with 6+ endpoints
- ✅ React frontend with modern UI

---

## 🛠️ Technologies Used

### C Programming (Core Shell):

- System calls: fork, exec, pipe, dup2, waitpid, chdir, getcwd
- Signal handling: signal(), SIGINT, SIGTSTP, SIGCHLD
- File operations: open, close, read, write
- Memory management: malloc, free, strdup
- String manipulation: strtok, strstr, strcmp

### Python (Backend):

- Flask (Web framework)
- Flask-CORS (Cross-origin requests)
- Flask-SocketIO (WebSocket)
- Google Generative AI (Gemini API)
- subprocess (Command execution)
- dotenv (Environment variables)

### JavaScript/React (Frontend):

- React 18 with Hooks (useState, useEffect)
- WebSocket (socket.io-client)
- Fetch API (HTTP requests)
- Modern CSS3

---

## 📖 How to Use This Documentation

### For Students:

1. **Apna role file padho** - Apne assigned components ko deeply samjho
2. **Code line-by-line samjho** - Hinglish explanations diye hain
3. **Viva questions practice karo** - Sabhi 15 questions aur answers revise karo
4. **Cross-reference karo** - Dusre team members ke roles bhi samjho integration ke liye

### For Viva Preparation:

1. **Basic questions** (5) - Must know for everyone
2. **Intermediate questions** (5) - Your expertise area
3. **Advanced questions** (5) - Deep dive topics

### For Project Understanding:

- **Architecture diagram** dekho upar
- **Data flow** samjho frontend se backend tak
- **Component interaction** understand karo

---

## 🎯 Quick Reference

### Command Examples:

```bash
# Basic commands
ls -la
pwd
cd /home/user
echo "Hello World"

# Redirection
cat file.txt > output.txt
grep error < input.txt 2> errors.txt
echo "test" >> append.txt

# Pipeline
ls -la | grep txt | wc -l
cat file.txt | grep error | sort | uniq

# Background jobs
sleep 10 &
jobs
fg 1
bg 1

# History
history
history 10
```

### Natural Language Examples:

```
"show me all python files"          → find . -name '*.py'
"list files in current directory"   → ls -la
"go to home directory"              → cd ~
"open myfile.c in vscode"           → code /path/to/myfile.c
"search for main.c"                 → find . -name main.c
```

---

## 📞 Contact & Support

Agar koi doubt ho ya clarification chahiye to apne team members se discuss karo. Har ek ka apna expertise area hai aur woh help kar sakte hain.

---

## 🏆 Project Achievements

Ye project ek complete, production-ready terminal application hai jo:

- ✅ Real bash shell ki tarah kaam karta hai
- ✅ AI-powered natural language support hai
- ✅ Modern web interface hai
- ✅ Scalable architecture hai
- ✅ Proper error handling hai
- ✅ Memory-safe implementation hai

**Congratulations team! 🎉**

---

**Last Updated:** October 30, 2025  
**Version:** 1.0  
**Project Status:** Complete ✅
