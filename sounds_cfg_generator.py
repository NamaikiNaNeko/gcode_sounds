"""
           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
                   Version 2, December 2004
 
Copyright (C) 2004 Sam Hocevar <sam@hocevar.net>

Everyone is permitted to copy and distribute verbatim or modified
copies of this license document, and changing it is allowed as long
as the name is changed.
 
           DO WHAT THE FUCK YOU WANT TO PUBLIC LICENSE
  TERMS AND CONDITIONS FOR COPYING, DISTRIBUTION AND MODIFICATION

 0. You just DO WHAT THE FUCK YOU WANT TO.
 """

#this script will run through a directory of your choosing, and will generate a cfg file containing appropriate macros to play either wav files or mp3 files.
#either call this from the command line and supply optional arguments:
# --indir - provides a directory. Example: --indir=wav to select a directory named wav in the same directory as where the script is called from
# --out - provide the output file name. Default is to create or overwrite a file named gcode_sounds.cfg
#By default, this script will select between playing wav files with aplay or mp3 files with mpg321.
#Avoid having the same file name in both wav and mp3; you will end up with duplicate macros generated.
#Change the sound_dir variable below if you plan on placing the sound files on the device where klipper is being ran in a different location.

import argparse
import os
from tkinter import Tk
from tkinter.filedialog import askdirectory
import sys
from librosa import get_duration

timeout_buffer = 10
sound_dir = "/home/pi/gcode_sounds/"

parser = argparse.ArgumentParser()
parser.add_argument("--indir", type=str, help="Input directory holding .mp3 or .wav files", nargs='?', default=None, const=None)
parser.add_argument("--out", type=str, help="Output file name", nargs='?', default="gcode_sounds.cfg", const="gcode_sounds.cfg")
args = parser.parse_args()

#if you're doing this on a headless machine, you'll need to put in the directory 
if args.indir is None:
    path = askdirectory()
else:
    path = args.indir
files = []
durations = []
for f in os.listdir(path):
    if f.endswith(".wav") or f.endswith(".mp3"):
        files.append(f)
        durations.append(get_duration(path=(path + "/" + f)))

timeout = int(max(durations) + timeout_buffer)

f = open("gcode_sounds.cfg", "w")
f.write("[gcode_shell_command play_mp3_file]\ncommand: mpg321\ntimeout: " + str(timeout) + ".\nverbose: False\n\n")
f.write("[gcode_shell_command play_wav_file]\ncommand: aplay\ntimeout: " + str(timeout) + ".\nverbose: False\n\n")

for file in files:
    name, ext = os.path.splitext(file)
    f.write("[gcode_macro _gs_play_" + name.replace(" ","_") + "]\n")
    f.write("gcode: RUN_SHELL_COMMAND CMD=play_" + ext.replace('.','') + "_file PARAMS=" + sound_dir + file + "\n\n")


# default header:    
# gcode_sounds.cfg

# This is the defaullt config file for gcode sounds. You can generate your own file using the python script provided
# if you want to add or change sounds.
# - have aplay and/or mpg321 installed on the klipper device for .wav/.mp3 files respectively
# - install gcode shell commands capability using KIAUH under advanced options
# - run raspi-config and select the appropriate audio output if you're on a raspberry pi
# - copy the contents of one of the sound directories to the klipper device (wav or mp3) to /home/pi/gcode_sounds
# add [gcode_sounds.cfg] to your main config
# add voice macros to whatever you want; for example adding in _gs_play_filament_change_requested to your M600 macros