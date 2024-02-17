# -*- coding: utf-8 -*-

block_cipher = None

a = Analysis(['programa_bluetooth_gui.py'],
             pathex=['.'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             name='programa_bluetooth_gui',
             version='0.1',
             description='Programa para conectar a dispositivos Bluetooth',
             author='Bard',
             console=True)
pyz = PYZ(a.pure, a.zipped_data)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='programa_bluetooth_gui.exe',
          debug=False,
          strip=False,
          upx=True,
          console=True)