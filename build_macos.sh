#!/bin/bash

# macOS Build Script for CaptureTextAi
# This script should be run on macOS to create a .dmg file

echo "🍎 Building CaptureTextAi for macOS..."

# Check if we're on macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo "❌ Error: This script must be run on macOS"
    echo "Please run this script on a Mac or in a macOS virtual machine"
    exit 1
fi

# Create virtual environment
echo "📦 Setting up Python environment..."
python3 -m venv venv
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt
pip install pyinstaller

# Convert icon to .icns format (macOS format)
echo "🎨 Converting icon..."
if command -v iconutil &> /dev/null; then
    # Create iconset directory
    mkdir -p Icon.iconset
    
    # Copy and resize icon (you may need to manually create these sizes)
    sips -z 16 16     Icon/Icon.png --out Icon.iconset/icon_16x16.png
    sips -z 32 32     Icon/Icon.png --out Icon.iconset/icon_16x16@2x.png
    sips -z 32 32     Icon/Icon.png --out Icon.iconset/icon_32x32.png
    sips -z 64 64     Icon/Icon.png --out Icon.iconset/icon_32x32@2x.png
    sips -z 128 128   Icon/Icon.png --out Icon.iconset/icon_128x128.png
    sips -z 256 256   Icon/Icon.png --out Icon.iconset/icon_128x128@2x.png
    sips -z 256 256   Icon/Icon.png --out Icon.iconset/icon_256x256.png
    sips -z 512 512   Icon/Icon.png --out Icon.iconset/icon_256x256@2x.png
    sips -z 512 512   Icon/Icon.png --out Icon.iconset/icon_512x512.png
    sips -z 1024 1024 Icon/Icon.png --out Icon.iconset/icon_512x512@2x.png
    
    # Create .icns file
    iconutil -c icns Icon.iconset
    ICON_PATH="--icon=Icon.icns"
else
    echo "⚠️  Warning: iconutil not found. App will use default icon."
    ICON_PATH=""
fi

# Build the app using PyInstaller
echo "🔨 Building macOS app..."
pyinstaller \
    --onefile \
    --windowed \
    --name="CaptureTextAi" \
    $ICON_PATH \
    --add-data="Icon:Icon" \
    --hidden-import="PIL._tkinter_finder" \
    --collect-submodules="pytesseract" \
    CaptureTextAi.py

# Check if build was successful
if [ ! -d "dist/CaptureTextAi.app" ]; then
    echo "❌ Error: Build failed!"
    exit 1
fi

echo "✅ App built successfully!"

# Create DMG using create-dmg (install with: brew install create-dmg)
echo "📦 Creating DMG installer..."

if command -v create-dmg &> /dev/null; then
    create-dmg \
        --volname "CaptureTextAi Installer" \
        --volicon "Icon.icns" \
        --window-pos 200 120 \
        --window-size 600 400 \
        --icon-size 100 \
        --icon "CaptureTextAi.app" 175 190 \
        --hide-extension "CaptureTextAi.app" \
        --app-drop-link 425 190 \
        --background "dmg-background.png" \
        "CaptureTextAi-$(date +%Y%m%d).dmg" \
        "dist/"
    
    echo "✅ DMG created successfully!"
    echo "📁 Output: CaptureTextAi-$(date +%Y%m%d).dmg"
else
    echo "⚠️  Warning: create-dmg not found. Install with: brew install create-dmg"
    echo "📁 App bundle available at: dist/CaptureTextAi.app"
    
    # Alternative: Create simple DMG using hdiutil
    echo "🔧 Creating simple DMG with hdiutil..."
    mkdir -p dmg-contents
    cp -R "dist/CaptureTextAi.app" dmg-contents/
    ln -s /Applications dmg-contents/Applications
    
    hdiutil create -volname "CaptureTextAi" -srcfolder dmg-contents -ov -format UDZO "CaptureTextAi-$(date +%Y%m%d).dmg"
    
    echo "✅ Simple DMG created successfully!"
    rm -rf dmg-contents
fi

echo "🎉 macOS build complete!"
echo ""
echo "Next steps:"
echo "1. Test the .dmg file on different macOS versions"
echo "2. Optionally code-sign the app for distribution"
echo "3. Upload to GitHub releases"