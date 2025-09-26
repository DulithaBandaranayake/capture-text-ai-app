# Capture Text Ai

<img src="https://github.com/user-attachments/assets/82f1dd90-5e1b-4092-a3ec-369d0fea680a" alt="Capture Text Ai Logo" width="200">

**Developed by DuBu**

Capture Text Ai is a simple, user-friendly application that allows you to capture an image and extract the text from it using OCR (Optical Character Recognition). It supports Windows, Linux, Arch Linux, and macOS, with setup guides for all platforms below.

## Features
- Capture screenshots and extract text from images.
- Easy-to-use interface.
- Cross-platform support (Windows, Linux, Arch Linux & macOS).

---

## Table of Contents
- [Features](#features)
- [Screenshots](#screenshots)
- [Installation](#installation)
  - [Windows](#windows)
  - [Linux](#linux)
  - [Arch Linux](#arch-linux)
  - [macOS](#macos)
- [Uninstallation](#uninstallation)
  - [Windows](#uninstall-on-windows)
  - [Linux](#uninstall-on-linux)
  - [Arch Linux](#uninstall-on-arch-linux)
  - [macOS](#uninstall-on-macos)
- [Tesseract Installation](#tesseract-installation)
  - [Windows](#tesseract-on-windows)
  - [Linux](#tesseract-on-linux)
  - [Arch Linux](#tesseract-on-arch-linux)
  - [macOS](#tesseract-on-macos)
- [License](#license)

---

## Screenshots

### Main Application Interface
<img width="1366" height="712" alt="Screenshot_20250926_124033" src="https://github.com/user-attachments/assets/4c0e4f75-77de-4994-9627-675d3aa2399f" />

### Text Extraction Results
<img width="1496" height="854" alt="Screenshot_20250926_124053" src="https://github.com/user-attachments/assets/c8e8e6f3-f6bc-426e-9878-a9dbb26fc696" />

### Home
<img width="374" height="257" alt="Screenshot_20250926_124008" src="https://github.com/user-attachments/assets/c1641350-a8f4-4d1e-9e97-e51134312e19" />

---

## Installation

### Windows

1. Download the installer from the [releases page](https://github.com/DulithaBandaranayake/CaptureTextAi/releases/tag/Windows).
2. Run the `CaptureTextAi_Setup.exe` file.
3. Follow the installation instructions.
   - **Note**: Tesseract is already bundled in the setup for Windows.
4. Launch the application from your Start Menu or Desktop.

### Linux

1. Download the `.deb` package for Linux from the [releases page](https://github.com/DulithaBandaranayake/CaptureTextAi/releases/tag/Linux).
2. Open a terminal and run the following command to install:
   ```bash
   sudo dpkg -i capture-text-ai-amd64.deb
   ```
3. If there are any dependency issues, run:
   ```bash
   sudo apt --fix-broken install
   ```

### Arch Linux

The easiest way to install on Arch Linux using AUR:

1. **Using yay (recommended)**:
   ```bash
   yay -S capture-text-ai
   ```

2. **Using paru**:
   ```bash
   paru -S capture-text-ai
   ```

3. **Manual AUR installation**:
   ```bash
   git clone https://aur.archlinux.org/capture-text-ai.git
   cd capture-text-ai
   makepkg -si
   ```

### macOS

1. **Download the macOS package** from the [releases page](https://github.com/DulithaBandaranayake/capture-text-ai-app/releases/tag/v1.3.3).
2. **Install using one of these methods**:

   **Option 1: Direct Installation**
   - Download `CaptureTextAi.dmg`
   - Double-click to mount the disk image
   - Drag CaptureTextAi to Applications folder
   - **Important**: On first run, right-click the app → "Open" to bypass security warnings

   **Option 2: Using Homebrew** (Recommended for developers)
   ```bash
   # Install Homebrew if you don't have it
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   
   # Install from source (when available)
   brew install capture-text-ai
   ```

   **Option 3: From Source**
   ```bash
   # Clone the repository
   git clone https://github.com/DulithaBandaranayake/capture-text-ai-app.git
   cd capture-text-ai-app
   
   # Install Python dependencies
   pip3 install -r requirements.txt
   
   # Run directly
   python3 CaptureTextAi.py
   ```

---

## Uninstallation

### Uninstall on Windows

1. Go to "Add or Remove Programs" in your Control Panel.
2. Find **Capture Text Ai** and click **Uninstall**.

### Uninstall on Linux

1. Run the following command in the terminal:
   ```bash
   sudo apt remove capture-text-ai
   ```

### Uninstall on Arch Linux

1. Using your AUR helper:
   ```bash
   yay -R capture-text-ai
   ```
   
   Or:
   ```bash
   paru -R capture-text-ai
   ```

2. Using pacman directly:
   ```bash
   sudo pacman -R capture-text-ai
   ```

### Uninstall on macOS

1. **If installed via .dmg**:
   - Open Finder → Applications
   - Find **Capture Text Ai** and drag to Trash
   - Empty Trash

2. **If installed via Homebrew**:
   ```bash
   brew uninstall capture-text-ai
   ```

3. **Remove settings** (optional):
   ```bash
   rm -rf ~/Library/Preferences/capture-text-ai/
   rm -rf ~/Library/Application\ Support/capture-text-ai/
   ```

---

## Tesseract Installation

Capture Text Ai uses Tesseract for Optical Character Recognition (OCR). Here's how to install it:

### Tesseract on Windows

- **No need to install**: Tesseract is bundled in the Windows installer.

### Tesseract on Linux

1. Install Tesseract by running the following command:
   ```bash
   sudo apt install tesseract-ocr
   ```

### Tesseract on Arch Linux

1. Install Tesseract using pacman:
   ```bash
   sudo pacman -S tesseract tesseract-data-eng
   ```

2. For additional languages (optional):
   ```bash
   sudo pacman -S tesseract-data-[language]
   ```

### Tesseract on macOS

1. **Using Homebrew** (recommended):
   ```bash
   brew install tesseract
   ```

2. **Using MacPorts**:
   ```bash
   sudo port install tesseract
   ```

3. **For additional languages**:
   ```bash
   # Homebrew
   brew install tesseract-lang
   
   # Or specific languages
   brew install tesseract --with-all-languages
   ```

---

## License

Capture Text Ai is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

### MIT License

Copyright (c) 2024 Dulitha Bandaranayake

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

Thank you for using Capture Text Ai! If you encounter any issues, feel free to [open an issue](https://github.com/DulithaBandaranayake/capture-text-ai-app/issues).

---
