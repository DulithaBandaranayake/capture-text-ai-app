#!/usr/bin/env python3
import sys
import tempfile
import pytesseract
import numpy as np
import cv2
import io
import os
from PIL import Image, ImageGrab
from PyQt6.QtWidgets import (QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QPushButton, QScrollArea, QTextEdit, QMessageBox, QStatusBar, QSpacerItem, QSizePolicy, QProgressBar)
from PyQt6.QtGui import QPixmap, QPainter, QMouseEvent, QIcon, QPalette
from PyQt6.QtCore import Qt, QRect, QBuffer, QIODevice, QTimer, pyqtSignal

# Configure the path to the tesseract executable
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract' if sys.platform != 'win32' else 'C:/Program Files/Tesseract-OCR/tesseract.exe'

class ScreenshotApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Capture Text Ai')
        self.setFixedSize(300, 150)
        self.setGeometry(100, 100, 300, 100)
        self.center()

        # Set the window icon with the correct path
        icon_path = os.path.join('/usr/local/share/capture-text-ai/Icon', 'Icon.png')
        self.setWindowIcon(QIcon(icon_path))

        self.setWindowFlags(Qt.WindowType.Window | Qt.WindowType.WindowCloseButtonHint)

        is_dark_mode = self.is_system_in_dark_mode()
        icon_path = os.path.join('/usr/local/share/capture-text-ai/Icon', 'screenshot_icon._dark.png' if is_dark_mode else 'screenshot_icon.png')

        self.take_screenshot_button = QPushButton(self)
        self.take_screenshot_button.setIcon(QIcon(icon_path))
        self.take_screenshot_button.setIconSize(self.take_screenshot_button.size())
        self.take_screenshot_button.clicked.connect(self.initiate_screenshot)
        self.take_screenshot_button.setFixedSize(100, 100)

        self.take_screenshot_button.setStyleSheet("""
            QPushButton {
                border: 2px solid blue;
                border-radius: 10px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #003366;
                color: white;
            }
        """)

        layout = QVBoxLayout()
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding))
        layout.addWidget(self.take_screenshot_button, alignment=Qt.AlignmentFlag.AlignCenter)
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Expanding))
        layout.setContentsMargins(10, 10, 10, 10)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)

        self.status_label = QLabel('Developed by Dubu')
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_bar.addWidget(self.status_label, stretch=1)

    def center(self):
        qr = self.frameGeometry()
        cp = QApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def is_system_in_dark_mode(self):
        palette = QApplication.palette()
        window_color = palette.color(QPalette.ColorRole.Window)
        light_threshold = 128
        return window_color.red() < light_threshold and window_color.green() < light_threshold and window_color.blue() < light_threshold
    
    def initiate_screenshot(self):
            # Minimize the window
            self.showMinimized()

            # Use QTimer to delay the screenshot capture
            QTimer.singleShot(200, self.take_screenshot)

    def take_screenshot(self):
        screenshot_path = self.capture_screenshot()
        if screenshot_path:
            self.open_image_window(screenshot_path)

    def capture_screenshot(self):
        try:
            
            # Capture the entire screen using ImageGrab
            screenshot = ImageGrab.grab()

            # Save the screenshot
            file_path = tempfile.mktemp(suffix='.png')
            screenshot.save(file_path)

        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to capture screenshot: {e}")
            # Ensure the application window is restored if an error occurs
            self.showNormal()
            return None

        return file_path

    def open_image_window(self, screenshot_path):
        if screenshot_path:
            self.image_window = ImageWindow(screenshot_path, self)
            self.image_window.show()
            self.image_window.window_closed.connect(self.restore_window)

    def restore_window(self):
        self.showNormal()
        self.activateWindow()

    def update_text_area(self, text):
        if self.image_window and self.image_window.text_area:
            self.image_window.text_area.setPlainText(text)
        else:
            QMessageBox.critical(self, "Error", "Text area not found in ImageWindow.")

class ImageWindow(QMainWindow):

    window_closed = pyqtSignal()

    def __init__(self, screenshot_path, parent):
        super().__init__()
        self.setWindowTitle('Capture Text Ai | DuBu')
        self.parent_app = parent

        # Set the window icon with the correct path
        icon_path = os.path.join('/usr/local/share/capture-text-ai/Icon', 'Icon.png')
        self.setWindowIcon(QIcon(icon_path))

        self.image_label = CroppingLabel(self)
        self.image_label.setPixmap(QPixmap(screenshot_path))
        self.image_label.set_app(self)
        self.image_label.set_parent_app(self.parent_app)

        scroll_area = QScrollArea(self)
        scroll_area.setWidget(self.image_label)
        scroll_area.setWidgetResizable(True)
        self.image_label.set_scroll_area(scroll_area)

        layout = QVBoxLayout()
        layout.addWidget(scroll_area)

        self.text_area = QTextEdit(self)
        self.text_area.setPlaceholderText('Select image need to convert text...')
        self.text_area.setStyleSheet("""
            QTextEdit {
                border: 2px solid blue;
                border-radius: 10px;
                padding: 5px;
            }
        """)

        layout.addWidget(self.text_area)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)
        layout.addWidget(self.progress_bar)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def closeEvent(self, event):
        super().closeEvent(event)
        self.window_closed.emit()

class CroppingLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setMouseTracking(True)
        self.start_pos = None
        self.end_pos = None
        self.selection_rect = QRect()
        self.temp_rect = QRect()
        self.image_pixmap = None
        self.scroll_area = None
        self.app = None
        self.parent_app = None

    def set_app(self, app):
        self.app = app

    def set_scroll_area(self, scroll_area):
        self.scroll_area = scroll_area

    def set_parent_app(self, app):
        self.parent_app = app

    def setPixmap(self, pixmap: QPixmap):
        super().setPixmap(pixmap)
        self.image_pixmap = pixmap
        self.selection_rect = QRect()
        self.temp_rect = QRect()
        self.update()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            self.start_pos = event.pos()
            self.end_pos = None
            self.temp_rect = QRect()
            self.update()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.start_pos:
            self.end_pos = event.pos()
            self.temp_rect = QRect(self.start_pos, self.end_pos).normalized()
            self.update()

            if self.scroll_area:
                viewport = self.scroll_area.viewport()
                scroll_bar = self.scroll_area.horizontalScrollBar()
                viewport_width = viewport.width()
                viewport_x = event.pos().x()

                if viewport_x > viewport_width - 30:
                    scroll_bar.setValue(scroll_bar.value() + 15)
                elif viewport_x < 30:
                    scroll_bar.setValue(scroll_bar.value() - 15)

                scroll_bar = self.scroll_area.verticalScrollBar()
                viewport_height = viewport.height()
                viewport_y = event.pos().y()

                if viewport_y > viewport_height - 30:
                    scroll_bar.setValue(scroll_bar.value() + 15)
                elif viewport_y < 30:
                    scroll_bar.setValue(scroll_bar.value() - 15)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.MouseButton.LeftButton:
            if self.start_pos and self.end_pos:
                self.selection_rect = QRect(self.start_pos, self.end_pos).normalized()
                self.start_pos = None
                self.end_pos = None
                self.temp_rect = QRect()
                self.update()
                self.extract_text_from_selection()

    def paintEvent(self, event):
        super().paintEvent(event)
        painter = QPainter(self)
        if not self.image_pixmap.isNull():
            painter.drawPixmap(self.rect(), self.image_pixmap)
            if not self.selection_rect.isNull():
                painter.setPen(Qt.GlobalColor.red)
                painter.drawRect(self.selection_rect)
            if not self.temp_rect.isNull():
                painter.setPen(Qt.GlobalColor.blue)
                painter.drawRect(self.temp_rect)

    def extract_text_from_selection(self):
        if self.image_pixmap and not self.selection_rect.isNull():
            # Show the progress bar
            if self.parent_app and self.parent_app.image_window:
                self.parent_app.image_window.progress_bar.setValue(0)
                self.parent_app.image_window.progress_bar.show()
                QApplication.processEvents()  # Ensure the UI updates immediately
            
            # Crop the QPixmap to the selected area
            cropped_pixmap = self.image_pixmap.copy(self.selection_rect)

            # Convert QPixmap to QImage
            image = cropped_pixmap.toImage()

            # Use QBuffer to store image data
            buffer = QBuffer()
            buffer.open(QIODevice.OpenModeFlag.WriteOnly)
            image.save(buffer, 'PNG')
            buffer.seek(0)

            # Convert QBuffer to PIL Image
            pil_image = Image.open(io.BytesIO(buffer.data()))

            # Convert the PIL image to OpenCV format
            opencv_image = np.array(pil_image)
            opencv_image = cv2.cvtColor(opencv_image, cv2.COLOR_RGB2BGR)  # Convert RGB to BGR for OpenCV

            # Extract text using pytesseract
            extracted_text = ""
            try:
                extracted_text = pytesseract.image_to_string(opencv_image)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to extract text: {e}")

            # Hide the progress bar and update its value to 100%
            if self.parent_app and self.parent_app.image_window:
                self.parent_app.image_window.progress_bar.setValue(100)
                self.parent_app.image_window.progress_bar.hide()
            
            # Display the extracted text or message if no text found
            if extracted_text.strip():
                if self.parent_app and self.parent_app.image_window:
                    self.parent_app.image_window.text_area.setPlainText(extracted_text)
                else:
                    QMessageBox.critical(self, "Error", "Text area not found in ImageWindow.")
            else:
                if self.parent_app and self.parent_app.image_window:
                    self.parent_app.image_window.text_area.setPlainText("No text detected in the selected area.")
                else:
                    QMessageBox.critical(self, "Error", "Text area not found in ImageWindow.")

            # Clear the selection rect after processing
            self.selection_rect = QRect()
            self.update()  # Refresh the widget

def main():
    app = QApplication(sys.argv)
    window = ScreenshotApp()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
