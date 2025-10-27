# 🔥 Advanced Mini Bash Shell - Phase 3: AI Voice Control

**The world's first Hindi + English voice-controlled shell with Google Cloud AI integration!**

## 🎯 What's New in Phase 3?

### 🎤 **Voice Control Features**
- **Hindi Voice Commands** (हिंदी आवाज़ कमांड) - Speak in Hindi, execute in terminal
- **English Voice Commands** - Natural English speech recognition
- **Real-time Translation** - Hindi → English using Google Cloud Translation API
- **Voice Feedback** - Text-to-Speech responses in both languages
- **Smart Command Mapping** - Intelligent mapping of voice to shell commands

### 🤖 **AI Integration**
- **Google Cloud Speech-to-Text** - High-accuracy voice recognition
- **Google Cloud Translation** - Seamless Hindi-English translation
- **Google Cloud Text-to-Speech** - Natural voice responses
- **Confidence Scoring** - Only execute high-confidence commands
- **Language Auto-Detection** - Automatically detect Hindi vs English

## 🚀 Quick Start

### 1. **Setup Voice Control**
```bash
# Run the automated setup
make voice-setup

# Or manually install dependencies
pip3 install -r requirements.txt
```

### 2. **Get Google Cloud Credentials**
1. Go to [Google Cloud Console](https://console.cloud.google.com/apis/credentials)
2. Create a new project or select existing
3. Enable APIs:
   - Speech-to-Text API
   - Translation API
   - Text-to-Speech API
4. Create a service account and download JSON key
5. Rename to `credentials.json` and place in project directory

### 3. **Start Voice Control**
```bash
# Interactive demo
make voice-demo

# Direct voice control
make voice-run

# Or run directly
python3 voice_enhanced.py
```

## 🎤 Voice Commands

### 🇮🇳 **Hindi Commands (हिंदी)**
| Hindi Command | English Translation | Shell Command |
|---------------|-------------------|---------------|
| "फोल्डर खोलो" | "Open folder" | `ls` |
| "वर्तमान फोल्डर" | "Current folder" | `pwd` |
| "ऊपर जाओ" | "Go up" | `cd ..` |
| "घर जाओ" | "Go home" | `cd ~` |
| "फाइल बनाओ" | "Create file" | `touch newfile.txt` |
| "फोल्डर बनाओ" | "Create folder" | `mkdir newfolder` |
| "सिस्टम जानकारी" | "System info" | `uname -a` |
| "मेमोरी दिखाओ" | "Show memory" | `free -h` |
| "गिट स्टेटस" | "Git status" | `git status` |
| "इंटरनेट जांचो" | "Check internet" | `ping google.com` |
| "बाहर निकलो" | "Exit" | `exit` |

### 🇺🇸 **English Commands**
| English Command | Shell Command |
|----------------|---------------|
| "list files" | `ls` |
| "current directory" | `pwd` |
| "go up" | `cd ..` |
| "go home" | `cd ~` |
| "create file" | `touch newfile.txt` |
| "create folder" | `mkdir newfolder` |
| "system info" | `uname -a` |
| "show memory" | `free -h` |
| "git status" | `git status` |
| "check internet" | `ping google.com` |
| "exit" | `exit` |

## 🏗️ Architecture

### **Phase 3 Components**
```
voice_control/
├── voice_enhanced.py      # Main voice control module
├── shell_bridge.py        # Communication bridge
├── voice_module.py        # Basic voice module
├── voice_demo.py          # Interactive demo
├── setup_voice.sh         # Automated setup
├── voice_config.json      # Configuration
├── requirements.txt       # Python dependencies
└── hindi_commands.json    # Command mappings
```

### **Integration Flow**
```
🎤 Voice Input → 🧠 Speech-to-Text → 🌐 Translation → 🔄 Command Mapping → 💻 Shell Execution → 🔊 Voice Feedback
```

## 🛠️ Technical Details

### **Google Cloud APIs Used**
- **Speech-to-Text API v1** - Voice recognition with language detection
- **Translation API v2** - Hindi ↔ English translation
- **Text-to-Speech API v1** - Natural voice responses

### **Audio Processing**
- **Sample Rate**: 16kHz
- **Format**: 16-bit PCM
- **Channels**: Mono
- **Recording Duration**: 5 seconds (configurable)

### **Command Processing**
- **Confidence Threshold**: 70% (configurable)
- **Language Detection**: Automatic
- **Fuzzy Matching**: Partial command recognition
- **Error Handling**: Graceful fallbacks

## 📋 Configuration

### **voice_config.json**
```json
{
  "google_cloud_credentials": "credentials.json",
  "language_codes": ["hi-IN", "en-US"],
  "voice_feedback": true,
  "auto_translate": true,
  "recording_timeout": 5,
  "confidence_threshold": 0.7,
  "continuous_listening": false
}
```

### **Environment Variables**
```bash
export GOOGLE_APPLICATION_CREDENTIALS="credentials.json"
```

## 🧪 Testing

### **Test Voice Module**
```bash
make voice-test
# or
python3 test_voice.py
```

### **Interactive Demo**
```bash
make voice-demo
# or
python3 voice_demo.py
```

### **Simulated Testing**
The demo includes a simulation mode that tests commands without microphone input.

## 🎯 Usage Examples

### **Example 1: Hindi Commands**
```bash
🎤 User says: "फोल्डर खोलो"
🧠 AI detects: Hindi, confidence 95%
🌐 Translates: "Open folder"
🔄 Maps to: "ls"
💻 Executes: ls
📤 Output: file1.txt file2.txt folder1/
🔊 Feedback: "कमांड सफलतापूर्वक चलाया गया"
```

### **Example 2: English Commands**
```bash
🎤 User says: "show system info"
🧠 AI detects: English, confidence 92%
🔄 Maps to: "uname -a"
💻 Executes: uname -a
📤 Output: Darwin MacBook-Pro.local 21.6.0 Darwin Kernel Version 21.6.0
🔊 Feedback: "Command executed successfully"
```

## 🔧 Troubleshooting

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
   - Set GOOGLE_APPLICATION_CREDENTIALS environment variable

3. **"Command not found" errors**
   - Check if mini-bash is built: `make clean && make`
   - Verify executable permissions: `chmod +x mini-bash`

4. **Low confidence in voice recognition**
   - Speak clearly and slowly
   - Reduce background noise
   - Adjust confidence threshold in config

### **Debug Mode**
```bash
# Enable debug logging
export VOICE_DEBUG=1
python3 voice_enhanced.py
```

## 🚀 Advanced Features

### **Custom Command Mappings**
Edit `hindi_commands.json` to add your own voice commands:

```json
{
  "मेरी कमांड": "my_command",
  "स्पेशल टास्क": "special_task"
}
```

### **Voice Feedback Customization**
Modify feedback messages in `voice_config.json`:

```json
{
  "feedback_messages": {
    "success": "काम हो गया!",
    "error": "गलती हुई है",
    "listening": "सुन रहा हूं..."
  }
}
```

## 📊 Performance

### **Benchmarks**
- **Voice Recognition**: ~2-3 seconds
- **Translation**: ~0.5-1 second
- **Command Execution**: Variable (depends on command)
- **Voice Feedback**: ~1-2 seconds

### **Resource Usage**
- **Memory**: ~50-100MB
- **CPU**: Low (only during processing)
- **Network**: Minimal (API calls only)

## 🔮 Future Enhancements

### **Planned Features**
- [ ] **Multi-language Support** - Add more Indian languages
- [ ] **Voice Training** - Learn user's accent
- [ ] **Command History** - Voice-based history navigation
- [ ] **Smart Suggestions** - AI-powered command suggestions
- [ ] **Voice Shortcuts** - Custom voice shortcuts
- [ ] **Background Processing** - Continuous listening mode

### **Advanced AI Features**
- [ ] **Context Awareness** - Remember previous commands
- [ ] **Natural Language Processing** - Complex command understanding
- [ ] **Voice Cloning** - Custom voice responses
- [ ] **Emotion Detection** - Respond to user's tone

## 🤝 Contributing

### **Adding New Commands**
1. Edit `hindi_commands.json`
2. Add English equivalent
3. Test with voice recognition
4. Submit pull request

### **Improving Translations**
1. Update command mappings
2. Test with native speakers
3. Refine fuzzy matching
4. Document changes

## 📄 License

This project is created for educational purposes. Feel free to use and modify as needed.

## 🎉 Acknowledgments

- **Google Cloud** - For amazing AI APIs
- **Python Community** - For excellent libraries
- **Open Source** - For inspiration and tools

---

**🔥 Advanced Mini Bash Shell v3.0 - The Future of Terminal Interaction!**

*"Speak your commands, let AI understand, and watch the magic happen!"* 🎤✨
