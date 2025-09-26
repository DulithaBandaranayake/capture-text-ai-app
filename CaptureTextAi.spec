# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['CaptureTextAi.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('Icon/*.png', 'Icon'),
        ('Icon/*.ico', 'Icon'),
    ],
    hiddenimports=[
        'PIL._tkinter_finder',
        'pytesseract',
        'cv2',
        'numpy',
        'PyQt6.QtCore',
        'PyQt6.QtGui',
        'PyQt6.QtWidgets',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='CaptureTextAi',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='Icon/Icon.ico'
)

# macOS app bundle
app = BUNDLE(
    exe,
    name='CaptureTextAi.app',
    icon='Icon/Icon.icns',
    bundle_identifier='com.dubu.capturetextai',
    version='1.3.0',
    info_plist={
        'CFBundleDisplayName': 'Capture Text AI',
        'CFBundleName': 'CaptureTextAi',
        'CFBundleVersion': '1.3.0',
        'CFBundleShortVersionString': '1.3',
        'NSHighResolutionCapable': True,
        'NSRequiresAquaSystemAppearance': False,
        'LSMinimumSystemVersion': '10.13.0',
        'NSCameraUsageDescription': 'This app needs camera access to capture screenshots.',
        'NSScreenCaptureDescription': 'This app needs screen recording permission to capture screenshots.',
    },
)