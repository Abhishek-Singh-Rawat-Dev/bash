# 🚀 Advanced Mini Bash Shell - Complete Usage Guide

## 📋 **Quick Start (No API Keys Required)**

### **Basic Shell Usage**
```bash
# 1. Build the shell
make clean && make

# 2. Start the shell
./mini-bash

# 3. Use basic commands
mini-bash$ pwd
mini-bash$ ls
mini-bash$ echo "Hello World"
mini-bash$ history
mini-bash$ exit
```

### **Install System-Wide (Optional)**
```bash
# Install for current user
./install.sh

# Add to PATH (add to ~/.bashrc or ~/.zshrc)
export PATH="$HOME/.local/bin:$PATH"

# Now you can use anywhere
mini-bash
mbash  # Short alias
```

## 🎤 **Voice Control Setup (Requires API Keys)**

### **Step 1: Get Google Cloud API Keys**

1. **Go to Google Cloud Console**
   - Visit: https://console.cloud.google.com/
   - Create a new project or select existing

2. **Enable Required APIs**
   - Go to "APIs & Services" > "Library"
   - Enable these APIs:
     - **Speech-to-Text API**
     - **Translation API**
     - **Text-to-Speech API**

3. **Create Service Account**
   - Go to "IAM & Admin" > "Service Accounts"
   - Click "Create Service Account"
   - Name: "mini-bash-voice"
   - Role: "Project Editor" (or create custom role with API access)

4. **Download Credentials**
   - Click on the service account
   - Go to "Keys" tab
   - Click "Add Key" > "Create New Key" > "JSON"
   - Download the JSON file
   - Rename to `credentials.json`
   - Place in the project directory

### **Step 2: Install Python Dependencies**

```bash
# Install voice control dependencies
pip3 install google-cloud-speech google-cloud-translate google-cloud-texttospeech pyaudio

# Or use the requirements file
pip3 install -r requirements.txt
```

### **Step 3: Start Voice Control**

```bash
# Start voice-controlled shell
python3 voice_enhanced.py

# Or use the wrapper (after installation)
mini-bash-voice
```

## 🎯 **Voice Commands**

### **Hindi Commands (हिंदी)**
| Hindi Command | English Translation | Shell Command |
|---------------|-------------------|---------------|
| "फोल्डर खोलो" | "Open folder" | `ls` |
| "वर्तमान फोल्डर" | "Current folder" | `pwd` |
| "ऊपर जाओ" | "Go up" | `cd ..` |
| "घर जाओ" | "Go home" | `cd ~` |
| "फाइल बनाओ" | "Create file" | `touch newfile.txt` |
| "सिस्टम जानकारी" | "System info" | `uname -a` |
| "गिट स्टेटस" | "Git status" | `git status` |
| "बाहर निकलो" | "Exit" | `exit` |

### **English Commands**
| English Command | Shell Command |
|----------------|---------------|
| "list files" | `ls` |
| "current directory" | `pwd` |
| "go up" | `cd ..` |
| "go home" | `cd ~` |
| "create file" | `touch newfile.txt` |
| "system info" | `uname -a` |
| "git status" | `git status` |
| "exit" | `exit` |

## 🔧 **Configuration**

### **Voice Control Settings**
Edit `voice_config.json`:
```json
{
  "voice_feedback": true,
  "confidence_threshold": 0.7,
  "recording_timeout": 5,
  "auto_translate": true
}
```

### **Command Mappings**
Edit `hindi_commands.json` to add custom commands:
```json
{
  "मेरी कमांड": "my_command",
  "स्पेशल टास्क": "special_task"
}
```

## 🧪 **Testing**

### **Test Basic Shell**
```bash
# Run production tests
./production_test.sh

# Test specific features
echo "ls | grep .c" | ./mini-bash
```

### **Test Voice Control**
```bash
# Test voice module
python3 test_voice.py

# Interactive demo
python3 voice_demo.py
```

## 💰 **API Costs (Google Cloud)**

### **Free Tier Limits**
- **Speech-to-Text**: 60 minutes/month free
- **Translation**: 500,000 characters/month free
- **Text-to-Speech**: 1 million characters/month free

### **Estimated Costs (Beyond Free Tier)**
- **Speech-to-Text**: ~$0.006 per 15 seconds
- **Translation**: ~$20 per 1M characters
- **Text-to-Speech**: ~$4 per 1M characters

*For typical usage, you'll likely stay within free limits*

## 🚨 **Troubleshooting**

### **Common Issues**

1. **"No audio devices found"**
   ```bash
   # macOS
   brew install portaudio
   
   # Linux
   sudo apt-get install portaudio19-dev
   ```

2. **"Google Cloud credentials not found"**
   - Download credentials.json from Google Cloud Console
   - Place in project directory
   - Set environment variable: `export GOOGLE_APPLICATION_CREDENTIALS="credentials.json"`

3. **"Command not found" errors**
   - Check if mini-bash is built: `make clean && make`
   - Verify executable permissions: `chmod +x mini-bash`

4. **Low confidence in voice recognition**
   - Speak clearly and slowly
   - Reduce background noise
   - Adjust confidence threshold in config

## 🎯 **Usage Examples**

### **Example 1: Basic Shell**
```bash
$ ./mini-bash
mini-bash:/Users/username$ pwd
/Users/username
mini-bash:/Users/username$ ls
file1.txt file2.txt
mini-bash:/Users/username$ echo "Hello"
Hello
mini-bash:/Users/username$ exit
```

### **Example 2: Voice Control**
```bash
$ python3 voice_enhanced.py
🎤 Listening... (Speak now!)
[User says: "फोल्डर खोलो"]
🎯 Detected: hi-IN
📝 Transcript: फोल्डर खोलो
🌐 Translated: Open folder
🔄 Mapped to: ls
💻 Executes: ls
📤 Output: file1.txt file2.txt
🔊 Feedback: "कमांड सफलतापूर्वक चलाया गया"
```

## 📚 **Documentation**

- **README.md** - Basic shell documentation
- **README_PHASE3.md** - Voice control documentation
- **PHASE3_SUMMARY.md** - Complete project summary
- **man mini-bash** - Manual page (after installation)

## 🆘 **Support**

If you encounter issues:
1. Check the troubleshooting section above
2. Run `./production_test.sh` to verify installation
3. Check Google Cloud Console for API issues
4. Verify all dependencies are installed

---

**🔥 Advanced Mini Bash Shell - Ready for Production Use! 🔥**
