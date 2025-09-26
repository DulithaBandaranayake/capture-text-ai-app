# CaptureTextAI

A PyQt6-based screenshot tool that captures screen regions and extracts text using OCR (Optical Character Recognition).

## Features

- **Screenshot Capture**: Click and drag to select any area of your screen
- **OCR Text Extraction**: Automatically extract text from captured images using Tesseract
- **Clean Interface**: Simple and intuitive PyQt6 GUI
- **Cross-Platform**: Works on Linux systems
- **Desktop Integration**: Includes desktop file for easy launching

## Requirements

- Python 3.6+
- PyQt6
- OpenCV (cv2)
- Pillow (PIL)
- pytesseract
- tesseract-ocr

## Installation

### From AUR (Arch Linux)
```bash
yay -S capture-text-ai
```

### From Source
```bash
git clone https://github.com/dulithadabare/capture-text-ai-app.git
cd capture-text-ai-app
pip install -r requirements.txt
python setup.py install
```

## Usage

1. Launch the application from your application menu or run:
   ```bash
   capture-text-ai
   ```

2. Click the screenshot button in the main window

3. Click and drag to select the area you want to capture

4. The extracted text will be displayed in a new window

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

## Author

- **Dulitha Bandaranayake** - [dubudeveloper@gmail.com](mailto:dubudeveloper@gmail.com)

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
