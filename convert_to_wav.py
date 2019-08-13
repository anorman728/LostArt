#!/usr/bin/python3

import os
import sys

# Simple helper script to convert midi file to wav using fluidsynth, but uses
# the SETTING__SOUND_FONT in the default_settings.py file.

# Source common settings.
exec(open("./default_settings.py").read())

argv = sys.argv

os.system('fluidsynth -g 1.5 -F "' + argv[1] + '.wav" ' + SETTING__SOUND_FONT + ' ' + argv[1])
