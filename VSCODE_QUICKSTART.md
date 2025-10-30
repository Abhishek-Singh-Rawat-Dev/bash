# 🚀 VS Code Quick Start - AI Terminal

## 📂 Step 1: Open Project in VS Code

### Method A: Drag & Drop (Easiest)
1. Open VS Code
2. Drag the `bash` folder into VS Code window
3. Done! ✅

### Method B: File Menu
1. Open VS Code
2. Click `File` → `Open Folder...`
3. Navigate to: `/Users/abhisheksinghrawat/Desktop/bash`
4. Click `Open`

### Method C: Terminal Command (if installed)
```bash
code /Users/abhisheksinghrawat/Desktop/bash
```

**Note:** If `code` command doesn't work:
1. Open VS Code
2. Press `Cmd+Shift+P`
3. Type: "Shell Command: Install 'code' command in PATH"
4. Click it and restart terminal

---

## ⚡ Step 2: Run the Project

### Easiest Way
Press **`Cmd+Shift+B`** (or `Ctrl+Shift+B` on Windows)

This automatically starts both backend and frontend servers!

### Alternative Ways

**Option A: Command Palette**
1. Press `Cmd+Shift+P`
2. Type: `Tasks: Run Task`
3. Select: **🚀 Start Full Stack (All Servers)**

**Option B: Terminal Menu**
1. Click `Terminal` → `Run Task...`
2. Select: **🚀 Start Full Stack (All Servers)**

**Option C: Integrated Terminal**
1. Press `` Ctrl+` `` to open terminal
2. Type: `./start_fullstack.sh`
3. Press Enter

---

## 🎯 Step 3: Access the App

Once servers start (takes ~10 seconds):

- **Frontend (Main App):** http://localhost:3000
- **Backend (API):** http://localhost:5002

Your browser should open automatically to http://localhost:3000

---

## 🛑 Stop the Project

### When You're Done:

**Option A: Stop Task**
1. Press `Cmd+Shift+P`
2. Type: `Tasks: Run Task`
3. Select: **🛑 Stop All Servers**

**Option B: Terminal**
1. Click in the terminal running the servers
2. Press `Ctrl+C`

---

## 🎨 Available VS Code Tasks

Press `Cmd+Shift+P` → `Tasks: Run Task` to see all:

### Main Tasks
- **🚀 Start Full Stack** - Start everything (default: `Cmd+Shift+B`)
- **🔧 Start Backend Only** - Just Flask server
- **🎨 Start Frontend Only** - Just React app
- **🛑 Stop All Servers** - Stop everything

### Development Tasks
- **🔨 Build Mini-Bash** - Compile C code
- **🧪 Test Mini-Bash** - Run tests
- **📦 Install Backend Dependencies** - Install Python packages
- **📦 Install Frontend Dependencies** - Install npm packages

### Monitoring Tasks
- **📄 View Backend Logs** - Live backend logs
- **📄 View Frontend Logs** - Live frontend logs

---

## 🐛 Debugging in VS Code

### Debug Backend (Python)
1. Open `backend/app.py`
2. Click left of line number to set breakpoint (red dot appears)
3. Press `F5`
4. Select: **🐍 Debug Backend (Flask)**
5. Use debug controls at top

### Debug Mini-Bash (C)
1. Open any `.c` file
2. Set breakpoints
3. Press `F5`
4. Select: **🔧 Debug Mini-Bash**

---

## 💡 Helpful Keyboard Shortcuts

| Action | Mac | Windows/Linux |
|--------|-----|---------------|
| **Start Project** | `Cmd+Shift+B` | `Ctrl+Shift+B` |
| **Command Palette** | `Cmd+Shift+P` | `Ctrl+Shift+P` |
| **Open File** | `Cmd+P` | `Ctrl+P` |
| **Terminal** | `` Ctrl+` `` | `` Ctrl+` `` |
| **New Terminal** | `` Ctrl+Shift+` `` | `` Ctrl+Shift+` `` |
| **Split Terminal** | `Cmd+\` | `Ctrl+\` |
| **Debug** | `F5` | `F5` |
| **Format Code** | `Shift+Opt+F` | `Shift+Alt+F` |

---

## 📦 Recommended Extensions

First time opening? VS Code will suggest extensions. Click **"Install All"**.

Essential extensions:
- ✅ **Python** - Python support
- ✅ **Pylance** - Python IntelliSense
- ✅ **C/C++** - C/C++ support
- ✅ **ESLint** - JavaScript linting
- ✅ **Prettier** - Code formatting

To manually install:
1. Click Extensions icon (or `Cmd+Shift+X`)
2. Search for extension name
3. Click Install

---

## 📁 Project Structure Overview

```
bash/
├── .vscode/              ← VS Code config (auto-created)
│   ├── tasks.json        ← Run/build tasks
│   ├── launch.json       ← Debug configs
│   └── settings.json     ← Project settings
│
├── backend/              ← Flask API
│   ├── app.py           ← Main server file
│   ├── venv/            ← Python environment
│   └── .env             ← API keys (add yours!)
│
├── frontend/             ← React UI
│   ├── src/
│   │   ├── App.js       ← Main app
│   │   └── components/
│   └── package.json
│
├── *.c, *.h              ← C source files
├── mini-bash            ← Compiled shell
└── start_fullstack.sh   ← Startup script
```

---

## 🔧 Common Tasks in VS Code

### Edit Backend Code
1. Open `backend/app.py`
2. Make changes
3. Save (`Cmd+S`)
4. Backend auto-reloads ✨

### Edit Frontend Code
1. Open `frontend/src/App.js`
2. Make changes
3. Save (`Cmd+S`)
4. Browser auto-refreshes ✨

### Edit C Code
1. Open any `.c` file in main folder
2. Make changes
3. Save (`Cmd+S`)
4. Run task: **🔨 Build Mini-Bash**
5. Test: `./mini-bash`

### View Logs
**Live logs:**
- Task: **📄 View Backend Logs**
- Task: **📄 View Frontend Logs**

**Static logs:**
- Open `backend.log`
- Open `frontend.log`

---

## 🆘 Troubleshooting

### "Tasks not found"
- Close and reopen VS Code
- Make sure you opened the `bash` folder (not Desktop)

### "Python interpreter not found"
1. `Cmd+Shift+P`
2. Type: "Python: Select Interpreter"
3. Select: `./backend/venv/bin/python`

### "npm command not found"
- Open terminal
- Run: `cd frontend && npm install`

### Servers won't start
1. Stop existing servers: Task **🛑 Stop All Servers**
2. Wait 5 seconds
3. Try again: `Cmd+Shift+B`

### Port already in use
Run this in terminal:
```bash
lsof -ti:5002 | xargs kill -9
lsof -ti:3000 | xargs kill -9
```
Then start again.

---

## 📚 Full Documentation

For detailed information, see:
- **VS_CODE_GUIDE.md** - Complete VS Code guide (this folder)
- **HOW_TO_START.md** - General startup guide
- **README.md** - Project overview

---

## 🎉 Ready to Code!

### Your 3-Step Workflow:

1. **Open VS Code** → Open `bash` folder
2. **Press** → `Cmd+Shift+B`
3. **Browse** → http://localhost:3000

**That's it! Happy coding! 🚀**

---

## 💡 Pro Tips

1. **Split View:** `Cmd+\` to edit backend and frontend side-by-side
2. **Multi-Cursor:** `Opt+Click` to add cursors, edit multiple places at once
3. **Quick File:** `Cmd+P` then type filename (fuzzy search works!)
4. **Zen Mode:** `Cmd+K Z` for distraction-free coding
5. **Format on Save:** Already enabled in this workspace! ✨

---

## 🎯 What's Next?

### Try These Commands in Your Running App:
- "show me all python files"
- "list files with details"
- "open app.py in vscode"
- Click 🎤 and say: "list all files"

### Explore the Code:
- **Backend AI Logic:** `backend/app.py`
- **Frontend UI:** `frontend/src/App.js`
- **Shell Core:** `main.c`, `executor.c`

### Read Documentation:
- VS_CODE_GUIDE.md (comprehensive guide)
- FULLSTACK_SETUP.md (architecture details)
- USAGE_GUIDE.md (user manual)

---

**Questions? Check the guide or logs! Happy Hacking! 💻✨**

