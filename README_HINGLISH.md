# 🧠⚡ AI-Powered Terminal (Hinglish README)

> Ye project aapke terminal ko smart banata hai! Normal English/Hinglish instructions likho ya bolo, aur system unko terminal commands me convert karke execute karta hai. Backend Flask + Gemini AI, Frontend React, aur ek custom mini-bash (C) shell use hota hai.

## ✨ Key Features (Kya-kya milta hai?)
- **AI Command Conversion:** "show me all python files" → `find . -name '*.py'`
- **Voice Support:** Mic dabao, bolo, kaam ho gaya
- **Smart File Search:** Pura system scan karke file dhundta hai, sahi app me open karta hai
- **Dual Execution:** Pehle mini-bash try karta hai, fail ho to system terminal
- **Real-time UI:** WebSocket se instant results

## 🏗️ Architecture (Upar se neeche flow)
```
React Frontend  →  Flask Backend (Gemini AI)  →  Mini-Bash (C) | System Terminal
```
- Frontend: Command input + live terminal UI
- Backend: AI se command nikalna, execute karna, results dena
- Mini-Bash: Humara khud ka shell (C me likha)
- Fallback: Agar mini-bash me support na ho to system terminal pe chala do

## 🚀 Quick Start (5-minute setup)

### 1) Prerequisites
- macOS/Linux
- Python 3.8+  |  Node.js 16+  |  GCC

### 2) Clone
```bash
git clone https://github.com/Abhishek-Singh-Rawat-Dev/bash.git
cd bash
```

### 3) Gemini API Key lao
- `https://makersuite.google.com/app/apikey` pe jao
- API key banao aur copy karo

### 4) Backend setup
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# .env me key daalo
echo "GEMINI_API_KEY=your_api_key_here" > .env
cd ..
```

### 5) Frontend setup
```bash
cd frontend
npm install
cd ..
```

### 6) Fullstack start
```bash
./start_fullstack.sh
# Frontend: http://localhost:3000
# Backend:  http://localhost:5002
```

Agar script permission error de:
```bash
chmod +x start_fullstack.sh start_backend.sh start_frontend.sh
```

## 🎮 Kaise use karein?
- Text: Input box me likho: "show me all python files"
- Voice: Mic button dabao, bolo: "open app.py in vscode"
- Examples pe click karke bhi try kar sakte ho

### Natural Language → Command Examples
```bash
"show me all python files"      → find . -name "*.py"
"go to downloads"               → cd ~/Downloads
"open package.json in vscode"   → code ./package.json
"search for main.c"             → find . -name main.c
```

## 🧩 Important Scripts
- `start_backend.sh`  → Flask server start
- `start_frontend.sh` → React app start
- `start_fullstack.sh`→ Dono ek sath start
- `make` / `make clean` → mini-bash build/clean

## 🧱 Tech Stack
- Frontend: React 18, WebSocket (socket.io), CSS
- Backend: Flask, Flask-SocketIO, Google Gemini, python-dotenv
- Shell: C (fork, exec, pipe, dup2, waitpid), custom mini-bash

## 🔌 API Endpoints (Short)
- `GET /api/health` → Status
- `POST /api/execute` → Command chalao
- `GET /api/history` → History
- `POST /api/search` → File search

## 🧪 Troubleshooting
- Port busy:
```bash
lsof -ti:5002 | xargs kill -9
lsof -ti:3000 | xargs kill -9
```
- Gemini key check:
```bash
cat backend/.env
curl http://localhost:5002/api/health
```
- mini-bash rebuild:
```bash
make clean && make
```

## 👥 Team & Roles (Short)
- Abhishek: Shell core, signals, main loop (`main.c`)
- Krishna: Parser, tokenization, redirections (`parser.c`)
- Vedansh: Executor, pipelines, builtins (`executor.c`, `pipeline.c`, `builtin.c`)
- Pankaj: Backend + AI + Frontend (`backend/app.py`, React)

Detailed docs + viva questions: `PHASE3_INDEX.md`

## 🔒 Security
- API keys `.env` me (git ignore)
- Timeouts enabled
- CORS configured (dev friendly)

## 📦 Project Structure (Short)
```
bash/
├─ backend/ (Flask + Gemini)
├─ frontend/ (React App)
├─ *.c, headers/ (mini-bash C source)
├─ mini-bash (compiled binary)
├─ start_* scripts
└─ README_HINGLISH.md (ye file)
```

## ⭐ Tips
- Voice off rakhna ho to frontend env me `REACT_APP_ENABLE_VOICE=false`
- System terminal pe force chahana ho to UI me executor dropdown se choose karo

## 📄 License
MIT – padhai, demo, ya production me use kar sakte ho.

Happy hacking! 🚀
