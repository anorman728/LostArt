# Bustling town

# Import modules.
import os
import sys

# Import classes from other files.
sys.path.insert(0, './src')
from Composition import Composition
from Voice import Voice

# Source common settings.
exec(open("./default_settings.py").read())

# Script below.

comp = Composition(2, 110)

guitar = comp.buildVoice(25, 'Guitar')
violin = comp.buildVoice(41, 'Violin')
flute = comp.buildVoice(74, 'Flute')
perc = comp.buildVoice(116, 'Woodblock')

violin.adjustPitchOffset(-12)
violin.setVolume(127)


comp.setKey(58)

# Functions
def stacEighth(voice, note):
    '''Staccato eighth note.'''
    voice.scaledNote(note, .25)
    voice.rest(.25)

def guitarBackground(voice):
    voice.scaledChord([-1, -5], .5)
    voice.scaledChord([2, -1], .5)
    voice.rest(.5)
    voice.scaledChord([2, -2], .5)

def percBackground(voice):
    for x in range(0,4):
        voice.scaledNote(5, .5)

def part01(voice, useChord = False):
    def part01Dum(voice):
        stacEighth(voice, 6)
        stacEighth(voice, 9)
        stacEighth(voice, 12)
        stacEighth(voice, 13)
        stacEighth(voice, 12)
        stacEighth(voice, 9)
        stacEighth(voice, 12)
        stacEighth(voice, 6)
        stacEighth(voice, 9)

    def chordDum(voice):
        if useChord:
            voice.scaledChord([9,6], 1.5)
        else:
            voice.scaledNote(9, 1.5)

    part01Dum(voice)
    voice.scaledChord([9], .25)
    voice.scaledChord([11], .25)
    voice.scaledChord([9], .25)
    voice.scaledChord([8], .5)
    chordDum(voice)

    voice.rest(.75)
    part01Dum(voice)
    voice.scaledChord([2], .25)
    voice.scaledChord([6], .25)
    voice.scaledChord([7], .25)
    voice.scaledChord([8], .25)
    chordDum(voice)

def part02(voice, useChord = False):
    def part02Dum(voice):
        voice.scaledNote(19, .25)
        voice.rest(.25)
        voice.scaledNote(16, .25)
        voice.scaledNote(18, .25)
        voice.scaledNote(19, .25)
        voice.rest(.25)
        voice.scaledNote(16, .25)
        voice.rest(.25)
        voice.scaledNote(18, .083)
        voice.scaledNote(19, .083)
        voice.scaledNote(18, .334)
        voice.scaledNote(16, .25)
        voice.scaledNote(15, .25)
        voice.scaledNote(16,.25)
        voice.rest(.75)

        voice.scaledNote(19, .25)
        voice.rest(.25)
        voice.scaledNote(16, .25)
        voice.scaledNote(18, .25)
        voice.scaledNote(19, .25)
        voice.rest(.25)
        voice.scaledNote(16, .25)
        voice.rest(.25)

    part02Dum(voice)
    if useChord:
        voice.scaledChromaticChord([35, 30], 1)
    else:
        voice.scaledNote(20, 1)
    voice.rest(1)

    part02Dum(voice)

def guitarBackground2(voice):
    def guitarBackground2Dum(voice):
        voice.scaledChord([-5, -8], 2)
        voice.scaledChord([-6, -9], 2)
        voice.scaledChord([-5, -8], 2)

    guitarBackground2Dum(voice)
    voice.scaledChromaticChord([-6, -13], 2)
    guitarBackground2Dum(voice)

# Start.

#comp.stop()#dmz1

# Solo guitar intro.

for x in range(0,4):
    guitarBackground(guitar)

for voice in [violin, flute]:
    # First part.
    voice.catchUp(guitar.whereAreWe()+.5)
    for x in range(0,8):
        guitarBackground(guitar)
    if voice == violin:
        part01(voice, True)
    else:
        part01(voice)

    # Add percussion.
    perc.catchUp(guitar.whereAreWe())
    for x in range(0,4):
        guitarBackground(guitar)
        percBackground(perc)

    # Second part.
    voice.catchUp(guitar.whereAreWe())

    fluteOffset = 12
    if voice == flute:
        voice.adjustPitchOffset(-fluteOffset) # Otherwise this part sounds like a piccolo

    guitarBackground2(guitar)
    if voice == violin:
        part02(voice, True)
    else:
        part02(voice)
    perc.catchUp(guitar.whereAreWe())
    for x in range(0,4):
        guitarBackground(guitar)
        percBackground(perc)
    if voice == violin:
        voice.scaledChord([9, 6], 4)
    else:
        voice.scaledNote(9, 4)

    if voice == flute:
        voice.adjustPitchOffset(fluteOffset) # Back to normal.


# For fadeout (in-game, this will be on repeat).
for x in range(0,4):
    guitarBackground(guitar)
    percBackground(perc)



filename = 'Output/' + __file__[:-2] + 'mid'
comp.writeToFile(filename)
os.system('fluidsynth -a alsa -g 1.5 ' + SETTING__SOUND_FONT + ' ./' + filename)
