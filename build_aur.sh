#!/bin/bash

# Build script for CaptureTextAi AUR package
# This script helps you test and build the package locally

echo "Building CaptureTextAi AUR package..."

# Check if we're in the right directory
if [[ ! -f "PKGBUILD" ]]; then
    echo "Error: PKGBUILD not found. Make sure you're in the project directory."
    exit 1
fi

# Clean previous builds
echo "Cleaning previous builds..."
rm -rf src/ pkg/ *.pkg.tar.* *.log

# Install dependencies if needed
echo "Checking dependencies..."
missing_deps=()
deps=("python" "python-pyqt6" "python-pytesseract" "python-pillow" "python-opencv" "python-numpy" "tesseract" "tesseract-data-eng")

for dep in "${deps[@]}"; do
    if ! pacman -Qi "$dep" &> /dev/null; then
        missing_deps+=("$dep")
    fi
done

if [[ ${#missing_deps[@]} -gt 0 ]]; then
    echo "Missing dependencies: ${missing_deps[*]}"
    echo "Install them with: sudo pacman -S ${missing_deps[*]}"
    read -p "Do you want to install them now? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        sudo pacman -S "${missing_deps[@]}"
    else
        echo "Please install missing dependencies before building."
        exit 1
    fi
fi

# Build the package
echo "Building package..."
makepkg -sf

if [[ $? -eq 0 ]]; then
    echo "Package built successfully!"
    echo "Install with: sudo pacman -U capture-text-ai-*.pkg.tar.*"
    
    # Offer to install
    read -p "Do you want to install the package now? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        sudo pacman -U capture-text-ai-*.pkg.tar.*
    fi
else
    echo "Build failed! Check the errors above."
    exit 1
fi