from setuptools import setup, find_packages
import os

def read_file(file_path):
    """Read a file and return its contents."""
    with open(file_path, 'r') as file:
        return file.read()

def get_data_files():
    """Specify additional data files to include in the package."""
    data_files = [
        ('/usr/local/share/capture-text-ai/Icon', ['Icon/Icon.png', 'Icon/screenshot_icon.png', 'Icon/screenshot_icon._dark.png']),
    ]
    return data_files

setup(
    name='capture-text-ai',
    version='1.0',
    description='Capture image and extract text',
    long_description=read_file('README.md'),  # Ensure you have a README.md file
    long_description_content_type='text/markdown',
    author='Dulitha Bandaranayake',
    author_email='dubudeveloper@gmail.com',
    packages=find_packages(),  # Automatically find packages
    install_requires=[
        'PyQt6',         # GUI framework
        'pytesseract',   # OCR library
        'Pillow',        # Image processing
        'opencv-python'  # Computer vision
    ],
    scripts=['CaptureTextAi.py'],
    entry_points={
        'console_scripts': [
            'capture-text-ai=CaptureTextAi:main',  # Entry point for the command-line script
        ],
    },
    data_files=get_data_files(),  # Include additional data files
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
