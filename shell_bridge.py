#!/usr/bin/env python3
"""
Advanced Mini Bash - Shell Bridge Module
Communication bridge between Python voice module and C shell
"""

import os
import sys
import subprocess
import threading
import time
import json
from typing import Optional, Dict, List

class ShellBridge:
    def __init__(self, shell_path: str = "./mini-bash"):
        """Initialize the shell bridge"""
        self.shell_path = shell_path
        self.shell_process = None
        self.is_running = False
        
        # Check if shell exists
        if not os.path.exists(shell_path):
            raise FileNotFoundError(f"Shell executable not found: {shell_path}")
    
    def start_shell(self) -> bool:
        """Start the Mini Bash shell process"""
        try:
            self.shell_process = subprocess.Popen(
                [self.shell_path],
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=0
            )
            self.is_running = True
            return True
        except Exception as e:
            print(f"❌ Failed to start shell: {e}")
            return False
    
    def stop_shell(self) -> None:
        """Stop the shell process"""
        if self.shell_process and self.is_running:
            try:
                self.shell_process.stdin.write("exit\n")
                self.shell_process.stdin.flush()
                self.shell_process.terminate()
                self.shell_process.wait(timeout=5)
            except:
                self.shell_process.kill()
            finally:
                self.is_running = False
    
    def execute_command(self, command: str) -> Dict[str, str]:
        """Execute a command in the shell and return results"""
        if not self.is_running or not self.shell_process:
            return {"error": "Shell not running"}
        
        try:
            # Send command to shell
            self.shell_process.stdin.write(f"{command}\n")
            self.shell_process.stdin.flush()
            
            # Read output with timeout
            output_lines = []
            error_lines = []
            
            # Give the shell time to process
            time.sleep(0.1)
            
            # Try to read available output
            try:
                # Non-blocking read
                import select
                if sys.platform != "win32":  # Unix-like systems
                    ready, _, _ = select.select([self.shell_process.stdout], [], [], 1.0)
                    if ready:
                        output = self.shell_process.stdout.read(4096)
                        if output:
                            output_lines = output.strip().split('\n')
            except:
                pass
            
            return {
                "command": command,
                "output": "\n".join(output_lines),
                "error": "\n".join(error_lines),
                "success": True
            }
            
        except Exception as e:
            return {
                "command": command,
                "output": "",
                "error": str(e),
                "success": False
            }
    
    def execute_commands_batch(self, commands: List[str]) -> List[Dict[str, str]]:
        """Execute multiple commands in sequence"""
        results = []
        for command in commands:
            result = self.execute_command(command)
            results.append(result)
            time.sleep(0.1)  # Small delay between commands
        return results
    
    def get_shell_status(self) -> Dict[str, any]:
        """Get current shell status"""
        return {
            "is_running": self.is_running,
            "shell_path": self.shell_path,
            "pid": self.shell_process.pid if self.shell_process else None
        }

class VoiceCommandProcessor:
    def __init__(self, shell_bridge: ShellBridge):
        """Initialize voice command processor"""
        self.shell_bridge = shell_bridge
        self.command_history = []
        
        # Enhanced command mappings
        self.command_mappings = {
            # Hindi to English mappings
            "hindi": {
                "फोल्डर खोलो": "ls",
                "फोल्डर दिखाओ": "ls -la",
                "वर्तमान फोल्डर": "pwd",
                "ऊपर जाओ": "cd ..",
                "घर जाओ": "cd ~",
                "बाहर निकलो": "exit",
                "फाइल बनाओ": "touch newfile.txt",
                "फोल्डर बनाओ": "mkdir newfolder",
                "फाइल हटाओ": "rm file.txt",
                "फोल्डर हटाओ": "rmdir folder",
                "सिस्टम जानकारी": "uname -a",
                "मेमोरी दिखाओ": "free -h",
                "डिस्क स्पेस": "df -h",
                "प्रोसेस दिखाओ": "ps aux",
                "गिट स्टेटस": "git status",
                "गिट कमिट": "git commit -m 'voice commit'",
                "गिट पुश": "git push",
                "गिट पुल": "git pull",
                "इंटरनेट जांचो": "ping -c 3 google.com",
                "नेटवर्क जानकारी": "ifconfig",
                "क्या हो रहा है": "ps aux | head -10",
                "सब कुछ साफ करो": "clear",
                "समय दिखाओ": "date",
                "कैलेंडर दिखाओ": "cal",
                "हिस्ट्री दिखाओ": "history",
                "जॉब्स दिखाओ": "jobs"
            },
            # English command mappings
            "english": {
                "list files": "ls",
                "show directory": "ls -la",
                "current directory": "pwd",
                "go up": "cd ..",
                "go home": "cd ~",
                "exit": "exit",
                "create file": "touch newfile.txt",
                "create folder": "mkdir newfolder",
                "delete file": "rm file.txt",
                "delete folder": "rmdir folder",
                "system info": "uname -a",
                "show memory": "free -h",
                "disk space": "df -h",
                "show processes": "ps aux",
                "git status": "git status",
                "git commit": "git commit -m 'voice commit'",
                "git push": "git push",
                "git pull": "git pull",
                "check internet": "ping -c 3 google.com",
                "network info": "ifconfig",
                "what's running": "ps aux | head -10",
                "clear screen": "clear",
                "show time": "date",
                "show calendar": "cal",
                "show history": "history",
                "show jobs": "jobs"
            }
        }
    
    def process_voice_command(self, voice_text: str, language: str = "auto") -> Dict[str, str]:
        """Process voice command and return execution result"""
        # Detect language if auto
        if language == "auto":
            language = self.detect_language(voice_text)
        
        # Map command
        mapped_command = self.map_command(voice_text, language)
        
        # Execute command
        result = self.shell_bridge.execute_command(mapped_command)
        
        # Add to history
        self.command_history.append({
            "voice_text": voice_text,
            "mapped_command": mapped_command,
            "language": language,
            "timestamp": time.time(),
            "result": result
        })
        
        return result
    
    def detect_language(self, text: str) -> str:
        """Detect if text is Hindi or English"""
        # Simple detection based on character sets
        hindi_chars = set("अआइईउऊऋएऐओऔकखगघङचछजझञटठडढणतथदधनपफबभमयरलवशषसह")
        text_chars = set(text)
        
        if text_chars.intersection(hindi_chars):
            return "hindi"
        else:
            return "english"
    
    def map_command(self, text: str, language: str) -> str:
        """Map voice text to shell command"""
        text_lower = text.lower().strip()
        
        # Check direct mappings
        if language in self.command_mappings:
            if text_lower in self.command_mappings[language]:
                return self.command_mappings[language][text_lower]
            
            # Fuzzy matching
            for voice_cmd, shell_cmd in self.command_mappings[language].items():
                if voice_cmd in text_lower or text_lower in voice_cmd:
                    return shell_cmd
        
        # If no mapping found, return original text
        return text
    
    def get_command_history(self) -> List[Dict[str, any]]:
        """Get command execution history"""
        return self.command_history
    
    def clear_history(self) -> None:
        """Clear command history"""
        self.command_history.clear()

def main():
    """Test the shell bridge"""
    print("🔗 Testing Shell Bridge...")
    
    try:
        # Initialize bridge
        bridge = ShellBridge()
        
        # Start shell
        if bridge.start_shell():
            print("✅ Shell started successfully")
            
            # Test commands
            test_commands = [
                "pwd",
                "ls",
                "echo 'Hello from bridge!'",
                "history"
            ]
            
            processor = VoiceCommandProcessor(bridge)
            
            for cmd in test_commands:
                print(f"\n🚀 Testing: {cmd}")
                result = processor.process_voice_command(cmd, "english")
                print(f"📤 Output: {result['output']}")
                if result['error']:
                    print(f"⚠️  Error: {result['error']}")
            
            # Stop shell
            bridge.stop_shell()
            print("\n✅ Shell stopped")
            
        else:
            print("❌ Failed to start shell")
    
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
