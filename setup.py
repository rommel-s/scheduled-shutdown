import sys
from cx_Freeze import setup, Executable

build_exe_options = {"packages": ["os"], "includes": ["tkinter"]}

base = None
if sys.platform == "win32":
  base = "Win32GUI"

setup(
  name = "Desligamento Programado",
  version = "2.0",
  description = "Desliga PC automaticamente",
  options = {"build_exe": build_exe_options},
  executables = [Executable("DesligamentoProgramado.py", base=base)]
)