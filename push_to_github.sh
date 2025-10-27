#!/bin/bash

# Advanced Mini Bash Shell - GitHub Push Script
# This script helps you push the project to GitHub

echo "🚀 Pushing Advanced Mini Bash Shell to GitHub"
echo "=============================================="
echo

# Check if git is configured
if ! git config user.name > /dev/null 2>&1; then
    echo "⚠️  Git user not configured"
    echo "Please run:"
    echo "  git config --global user.name \"Your Name\""
    echo "  git config --global user.email \"your.email@example.com\""
    echo
    exit 1
fi

# Check if we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "❌ Not in a git repository"
    exit 1
fi

# Show current status
echo "📊 Current Status:"
echo "=================="
git status --short
echo

# Show remote
echo "🌐 Remote Repository:"
echo "====================="
git remote -v
echo

# Check if there are commits to push
if git diff --quiet origin/main...HEAD 2>/dev/null; then
    echo "✅ Already up to date with remote"
    echo "Nothing to push"
    exit 0
fi

# Instructions for pushing
echo "📝 Instructions to Push:"
echo "========================"
echo
echo "Option 1: Push using HTTPS (requires GitHub username & password/token)"
echo "-----------------------------------------------------------------------"
echo "git push origin main"
echo
echo "If prompted, enter:"
echo "  Username: Your GitHub username"
echo "  Password: Your GitHub Personal Access Token (not password!)"
echo
echo "Option 2: Push using SSH (if you have SSH keys configured)"
echo "-----------------------------------------------------------"
echo "First, change remote to SSH:"
echo "git remote set-url origin git@github.com:Abhishek-Singh-Rawat-Dev/bash.git"
echo "Then push:"
echo "git push origin main"
echo
echo "Option 3: Get Personal Access Token"
echo "------------------------------------"
echo "1. Go to: https://github.com/settings/tokens"
echo "2. Click 'Generate new token (classic)'"
echo "3. Select scopes: 'repo' (full control)"
echo "4. Generate token and copy it"
echo "5. Use token as password when pushing"
echo
echo "🎯 Recommended: Use Personal Access Token (Option 3 + Option 1)"
echo

# Ask user if they want to push now
read -p "Do you want to push now? (y/n): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "🚀 Pushing to GitHub..."
    git push origin main
    
    if [ $? -eq 0 ]; then
        echo
        echo "✅ Successfully pushed to GitHub!"
        echo "🌐 View your repository at:"
        echo "   https://github.com/Abhishek-Singh-Rawat-Dev/bash"
        echo
        echo "🎉 Your Advanced Mini Bash Shell is now on GitHub!"
    else
        echo
        echo "❌ Push failed"
        echo "Please check the error message above and try again"
        echo "You may need to:"
        echo "  - Set up authentication (token or SSH)"
        echo "  - Check your internet connection"
        echo "  - Verify repository permissions"
    fi
else
    echo "⏸️  Push cancelled"
    echo "You can push later using: git push origin main"
fi
