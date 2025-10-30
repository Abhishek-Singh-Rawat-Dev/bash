# 🎯 VS Code Guide - AI Terminal Project

Complete guide to running and developing the AI Terminal project in Visual Studio Code.

## 📋 Table of Contents
1. [Quick Start](#quick-start)
2. [Running the Project](#running-the-project)
3. [Using VS Code Tasks](#using-vs-code-tasks)
4. [Debugging](#debugging)
5. [Recommended Extensions](#recommended-extensions)
6. [Keyboard Shortcuts](#keyboard-shortcuts)
7. [Tips & Tricks](#tips--tricks)

---

## 🚀 Quick Start

### 1. Open Project in VS Code

**Option A: From Terminal**
```bash
cd /Users/abhisheksinghrawat/Desktop/bash
code .
```

**Option B: From VS Code**
- Open VS Code
- `File` → `Open Folder...`
- Navigate to `/Users/abhisheksinghrawat/Desktop/bash`
- Click `Open`

### 2. Install Recommended Extensions

When you open the project, VS Code will prompt you to install recommended extensions. Click **"Install All"**.

Or manually install:
- **Python** (ms-python.python)
- **Pylance** (ms-python.vscode-pylance)
- **C/C++** (ms-vscode.cpptools)
- **ESLint** (dbaeumer.vscode-eslint)
- **Prettier** (esbenp.prettier-vscode)

### 3. Trust the Workspace

VS Code will ask if you trust the folder. Click **"Yes, I trust the authors"** to enable all features.

---

## 🎮 Running the Project

### Method 1: Using VS Code Tasks (Recommended)

#### Quick Launch
1. Press **`Cmd + Shift + B`** (or `Ctrl + Shift + B` on Windows/Linux)
2. This will run the default task: **"🚀 Start Full Stack (All Servers)"**
3. Watch the integrated terminal as it starts both backend and frontend

#### Using Command Palette
1. Press **`Cmd + Shift + P`** (or `Ctrl + Shift + P`)
2. Type: `Tasks: Run Task`
3. Select from available tasks:
   - **🚀 Start Full Stack (All Servers)** - Start everything at once
   - **🔧 Start Backend Only** - Just Flask server
   - **🎨 Start Frontend Only** - Just React app
   - **🛑 Stop All Servers** - Stop all running servers
   - **🔨 Build Mini-Bash** - Compile C code
   - **🧪 Test Mini-Bash** - Run shell tests

### Method 2: Using Integrated Terminal

1. Open terminal in VS Code: **`Ctrl + `** (backtick) or `Terminal` → `New Terminal`
2. Run the startup script:
```bash
./start_fullstack.sh
```

### Method 3: Split Terminals (Advanced)

For separate backend and frontend terminals:

**Terminal 1 (Backend):**
```bash
cd backend
source venv/bin/activate
python app.py
```

**Terminal 2 (Frontend):**
```bash
cd frontend
npm start
```

To split terminal: Click the **split terminal** icon (⊞) or press **`Cmd + \`**

---

## 📌 Using VS Code Tasks

### Available Tasks

#### Core Tasks
| Task | Shortcut | Description |
|------|----------|-------------|
| 🚀 Start Full Stack | `Cmd+Shift+B` | Start backend + frontend |
| 🛑 Stop All Servers | Task menu | Kill all running servers |
| 🔨 Build Mini-Bash | Task menu | Compile C code |

#### Development Tasks
| Task | Description |
|------|-------------|
| 🧪 Test Mini-Bash | Run shell integration tests |
| 📦 Install Backend Dependencies | Install Python packages |
| 📦 Install Frontend Dependencies | Install npm packages |
| 🧹 Clean Build | Remove compiled files |

#### Debugging Tasks
| Task | Description |
|------|-------------|
| 📄 View Backend Logs | Tail backend.log |
| 📄 View Frontend Logs | Tail frontend.log |

### How to Run Tasks

**Keyboard:**
1. `Cmd + Shift + P` → `Tasks: Run Task`
2. Select task from list

**Mouse:**
1. `Terminal` menu → `Run Task...`
2. Select task from list

**Quick:**
- Default build task: `Cmd + Shift + B`

---

## 🐛 Debugging

### Debug Backend (Flask)

1. Set breakpoints in Python files (click left of line number)
2. Press **`F5`** or `Run` → `Start Debugging`
3. Select: **"🐍 Debug Backend (Flask)"**
4. Backend starts in debug mode
5. Use debug controls:
   - **Continue** (`F5`)
   - **Step Over** (`F10`)
   - **Step Into** (`F11`)
   - **Step Out** (`Shift + F11`)

### Debug Mini-Bash (C)

1. Set breakpoints in C files
2. Press **`F5`**
3. Select: **"🔧 Debug Mini-Bash"**
4. Mini-bash compiles and starts in debugger

### Debug Console

View debug output in:
- **Debug Console** tab (appears when debugging)
- **Terminal** tab for stdout/stderr
- **Problems** tab for errors

### Useful Debug Features

**Watch Variables:**
1. `Run` → `Add Watch Expression`
2. Enter variable name

**Call Stack:**
- View in Debug sidebar (left panel)
- Shows function call hierarchy

**Variables:**
- Auto-displays all variables in current scope

---

## 🔌 Recommended Extensions

### Essential (Auto-suggested)

1. **Python** (`ms-python.python`)
   - Python IntelliSense, linting, debugging

2. **Pylance** (`ms-python.vscode-pylance`)
   - Fast Python language server

3. **C/C++** (`ms-vscode.cpptools`)
   - C/C++ IntelliSense and debugging

4. **ESLint** (`dbaeumer.vscode-eslint`)
   - JavaScript/React linting

5. **Prettier** (`esbenp.prettier-vscode`)
   - Code formatting

### Useful Optional Extensions

6. **React Code Snippets** (`dsznajder.es7-react-js-snippets`)
   - React shortcuts

7. **GitLens** (`eamodio.gitlens`)
   - Enhanced Git features

8. **Code Runner** (`formulahendry.code-runner`)
   - Quick code execution

9. **Markdown All in One** (`yzhang.markdown-all-in-one`)
   - Markdown preview and editing

### Install Extensions

**Via Command Palette:**
1. `Cmd + Shift + P` → `Extensions: Install Extensions`
2. Search by name or ID
3. Click **Install**

**Via Terminal:**
```bash
code --install-extension ms-python.python
code --install-extension ms-vscode.cpptools
code --install-extension dbaeumer.vscode-eslint
```

---

## ⌨️ Keyboard Shortcuts

### Essential Shortcuts

| Action | Mac | Windows/Linux |
|--------|-----|---------------|
| Command Palette | `Cmd+Shift+P` | `Ctrl+Shift+P` |
| Quick Open File | `Cmd+P` | `Ctrl+P` |
| Toggle Terminal | `Ctrl+`\` | `Ctrl+`\` |
| New Terminal | `Ctrl+Shift+`\` | `Ctrl+Shift+`\` |
| Split Terminal | `Cmd+\` | `Ctrl+\` |
| Build/Run | `Cmd+Shift+B` | `Ctrl+Shift+B` |
| Start Debugging | `F5` | `F5` |
| Toggle Sidebar | `Cmd+B` | `Ctrl+B` |

### Editor Shortcuts

| Action | Mac | Windows/Linux |
|--------|-----|---------------|
| Go to Definition | `F12` | `F12` |
| Peek Definition | `Opt+F12` | `Alt+F12` |
| Find References | `Shift+F12` | `Shift+F12` |
| Rename Symbol | `F2` | `F2` |
| Format Document | `Shift+Opt+F` | `Shift+Alt+F` |
| Comment Line | `Cmd+/` | `Ctrl+/` |

### Navigation

| Action | Mac | Windows/Linux |
|--------|-----|---------------|
| Go to Line | `Ctrl+G` | `Ctrl+G` |
| Navigate Back | `Ctrl+-` | `Alt+Left` |
| Navigate Forward | `Ctrl+Shift+-` | `Alt+Right` |
| Find in Files | `Cmd+Shift+F` | `Ctrl+Shift+F` |
| Replace in Files | `Cmd+Shift+H` | `Ctrl+Shift+H` |

---

## 💡 Tips & Tricks

### 1. Multi-Cursor Editing
- **Add cursor:** `Opt+Click` (Mac) or `Alt+Click` (Windows)
- **Select next occurrence:** `Cmd+D` / `Ctrl+D`
- **Select all occurrences:** `Cmd+Shift+L` / `Ctrl+Shift+L`

### 2. Split Editor View
- **Split editor:** `Cmd+\` / `Ctrl+\`
- Useful for viewing backend and frontend code simultaneously

### 3. Zen Mode
- **Enter Zen Mode:** `Cmd+K Z` / `Ctrl+K Z`
- Distraction-free coding

### 4. Integrated Terminal Tips
- **Multiple terminals:** Create separate terminals for backend/frontend
- **Rename terminal:** Right-click terminal tab → Rename
- **Terminal history:** Use `↑`/`↓` arrow keys

### 5. Quick File Search
- `Cmd+P` then type filename
- Use fuzzy search: e.g., "apjs" finds "app.js"

### 6. Workspace Settings
Project-specific settings are in `.vscode/settings.json`:
- Python interpreter auto-selected
- C++ include paths configured
- Auto-formatting enabled

### 7. Problem Panel
- View all errors/warnings: `Cmd+Shift+M` / `Ctrl+Shift+M`
- Includes linter errors, compile errors, etc.

### 8. Source Control
- Open Git panel: `Ctrl+Shift+G`
- Stage files, commit, push/pull
- View file changes inline

---

## 🔧 Workspace Configuration

### Python Setup

The workspace is configured to use the backend virtual environment:
```json
"python.defaultInterpreterPath": "${workspaceFolder}/backend/venv/bin/python"
```

To manually select interpreter:
1. `Cmd+Shift+P` → `Python: Select Interpreter`
2. Choose `./backend/venv/bin/python`

### C/C++ Setup

Headers are automatically recognized:
```json
"C_Cpp.default.includePath": ["${workspaceFolder}/headers"]
```

### ESLint (React)

Auto-fixes on save enabled for JavaScript/React files.

---

## 🔍 Troubleshooting in VS Code

### "Python interpreter not found"
1. `Cmd+Shift+P` → `Python: Select Interpreter`
2. Select: `./backend/venv/bin/python`

### "Cannot find module 'react-scripts'"
1. Open terminal: `Ctrl+`\`
2. Run: `cd frontend && npm install`

### "Task 'Start Full Stack' not found"
1. Close and reopen VS Code
2. Make sure `.vscode/tasks.json` exists
3. Try: `Cmd+Shift+P` → `Tasks: Run Task`

### Terminal won't activate virtualenv
1. Open new terminal
2. Manually activate: `source backend/venv/bin/activate`

### Debugging not working
1. Install Python extension
2. Install C/C++ extension
3. Try: `Cmd+Shift+P` → `Debug: Start Debugging`

---

## 📚 Quick Reference

### Starting the Project in VS Code

**3 Simple Steps:**
1. Open project: `code /Users/abhisheksinghrawat/Desktop/bash`
2. Press: `Cmd+Shift+B`
3. Wait for servers to start

**Access:**
- Frontend: http://localhost:3000
- Backend: http://localhost:5002

**Stop Servers:**
1. `Cmd+Shift+P` → `Tasks: Run Task`
2. Select: **🛑 Stop All Servers**
3. Or press `Ctrl+C` in terminal

### File Structure Overview

```
bash/
├── .vscode/              # VS Code configuration
│   ├── tasks.json        # Build/run tasks
│   ├── launch.json       # Debug configurations
│   ├── settings.json     # Workspace settings
│   └── extensions.json   # Recommended extensions
├── backend/              # Flask backend
│   ├── app.py           # Main server
│   ├── venv/            # Python virtual env
│   └── requirements.txt
├── frontend/             # React frontend
│   ├── src/
│   ├── public/
│   └── package.json
├── headers/              # C header files
├── *.c                   # C source files
├── mini-bash            # Compiled shell
└── start_fullstack.sh   # Startup script
```

---

## 🎯 Workflow Examples

### Daily Development Workflow

1. **Open VS Code**
   ```bash
   cd /Users/abhisheksinghrawat/Desktop/bash
   code .
   ```

2. **Start Servers**
   - Press `Cmd+Shift+B`
   - Or use integrated terminal: `./start_fullstack.sh`

3. **Edit Code**
   - Backend: `backend/app.py`
   - Frontend: `frontend/src/App.js`
   - Mini-bash: `*.c` files

4. **See Changes**
   - Backend: Auto-reloads on save
   - Frontend: Hot-reloads in browser
   - Mini-bash: Rebuild with `make`

5. **Stop Servers**
   - Task: **🛑 Stop All Servers**
   - Or `Ctrl+C` in terminal

### Debugging Workflow

1. **Set Breakpoints**
   - Click left of line numbers

2. **Start Debug**
   - Press `F5`
   - Select debug configuration

3. **Inspect**
   - Hover over variables
   - Check Debug Console
   - View Call Stack

4. **Step Through**
   - Use `F10` (step over), `F11` (step into)

---

## 📞 Need Help?

### In VS Code
- **Command Palette:** `Cmd+Shift+P` → Type your question
- **Help Menu:** `Help` → `Welcome`, `Documentation`

### Project Documentation
- `README.md` - Project overview
- `HOW_TO_START.md` - Getting started
- `FULLSTACK_SETUP.md` - Detailed setup

### Logs
- Backend: `backend.log`
- Frontend: `frontend.log`
- VS Code output: `Output` panel

---

## 🎉 You're Ready!

Your VS Code is now fully configured for the AI Terminal project. Press **`Cmd+Shift+B`** and start coding! 🚀

**Pro Tips:**
- Learn keyboard shortcuts to code faster
- Use split editors to view multiple files
- Enable auto-save: `File` → `Auto Save`
- Customize your theme: `Code` → `Preferences` → `Color Theme`

Happy Coding! 💻✨

