from PyInstaller.__main__ import run
from datetime import datetime

# creates the EXE distributable file

starting_time = datetime.now()

script = 'main.py'
args = [script, '--onefile', '--noconsole', '-n MIDI Transposer', '--distpath=EXE/']

run(args)

print(f'--== BUILT EXE time elapsed {datetime.now() - starting_time} ==--')

