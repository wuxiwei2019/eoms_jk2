# -*- mode: python -*-

block_cipher = None


a = Analysis(['eoms_gui.py'],
             pathex=['C:\\Windows\\System32\\downlevel', 'D:\\ShuXue\\picToExcel\\venv\\eoms'],
             binaries=[],
             datas=[],
             hiddenimports=['eoms_frame.py', 'eoms_model.py', 'get_zaitu_time.py', 'table_obj_model.py'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='eoms_gui',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False , icon='icon.ico')
