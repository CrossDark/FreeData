"""
FreeStrange install entry
"""
import os


with open('/home/pi/.bashrc', 'r+') as path:
    path.seek(0, 2)
    path.write('\n')
    path.write('# FreeStrange\n')
    path.write("alias FreeData='python " + os.path.split(__file__)[0] + "/FreeStrange/API/__init__.py'\n")
os.system('source ~/.bashrc')
