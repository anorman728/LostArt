#!/bin/bash

# Simple helper script to convert midi file to wav using fluidsynth.
# This will only work on a Linux machine that has fluidsynth installed.

fluidsynth -F "${1}.wav" /usr/share/sounds/sf2/FluidR3_GM.sf2 ${1}
