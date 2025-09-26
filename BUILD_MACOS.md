# Building macOS DMG for CaptureTextAi

## Prerequisites

You need to run this on **macOS** (physical Mac, VM, or CI/CD with macOS runner):

### Install Required Tools
```bash
# Install Homebrew if not already installed
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install create-dmg for professional DMG creation
brew install create-dmg

# Install Python dependencies
pip3 install pyinstaller pillow
```

## Build Process

### Option 1: Using the Build Script (Recommended)
```bash
# On macOS, run:
./build_macos.sh
```

### Option 2: Manual Build
```bash
# 1. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt
pip install pyinstaller

# 3. Convert icon to .icns format
# You'll need to manually create Icon.icns from Icon.png
# Use an online converter or macOS Preview app

# 4. Build with PyInstaller
pyinstaller CaptureTextAi.spec

# 5. Create DMG
create-dmg \
    --volname "CaptureTextAi Installer" \
    --window-pos 200 120 \
    --window-size 600 400 \
    --icon-size 100 \
    --icon "CaptureTextAi.app" 175 190 \
    --app-drop-link 425 190 \
    "CaptureTextAi.dmg" \
    "dist/"
```

## Alternative: GitHub Actions (Automated)

Create `.github/workflows/build-macos.yml` for automated builds:

```yaml
name: Build macOS DMG

on:
  push:
    tags:
      - 'v*'

jobs:
  build-macos:
    runs-on: macos-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pyinstaller
        brew install create-dmg
    
    - name: Build app
      run: |
        pyinstaller CaptureTextAi.spec
    
    - name: Create DMG
      run: |
        create-dmg \
          --volname "CaptureTextAi Installer" \
          --window-pos 200 120 \
          --window-size 600 400 \
          --icon-size 100 \
          --icon "CaptureTextAi.app" 175 190 \
          --app-drop-link 425 190 \
          "CaptureTextAi.dmg" \
          "dist/"
    
    - name: Upload DMG
      uses: actions/upload-artifact@v3
      with:
        name: CaptureTextAi-macOS
        path: "*.dmg"
```

## Testing the DMG

1. **Test on different macOS versions** (10.13+)
2. **Verify app permissions** for screen capture
3. **Test Gatekeeper warnings** and bypass instructions
4. **Check Tesseract bundling** or installation requirements

## Code Signing (Optional but Recommended)

For distribution without security warnings:

```bash
# Sign the app (requires Apple Developer account)
codesign --deep --force --verify --verbose --sign "Developer ID Application: Your Name" dist/CaptureTextAi.app

# Notarize (requires Apple Developer account)
xcrun notarytool submit CaptureTextAi.dmg --apple-id your@email.com --team-id YOUR_TEAM_ID --password APP_PASSWORD --wait
```

## File Structure After Build

```
dist/
├── CaptureTextAi.app/          # macOS app bundle
CaptureTextAi.dmg               # Installer DMG file
```