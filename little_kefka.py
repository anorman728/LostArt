# "Little Kefka"
# A combination of Kefka's theme, but incorporating Bach's Little Fugue, and as
# a string quartet.

# Import modules.
import os
import sys

# Import classes from other files.
sys.path.insert(0, './src')
from Composition import Composition
from Voice import Voice
from ScaledNote import ScaledNote
SC = ScaledNote

# Source common settings.
exec(open("./default_settings.py").read())

# Script below.

comp = Composition(2, 160)

violin1 = comp.buildVoice(41, 'Violin 1')
violin2 = comp.buildVoice(41, 'Violin 2')

viola = comp.buildVoice(42, 'Viola')
viola.adjustPitchOffset(-12)

cello = comp.buildVoice(43, 'Cello')
cello.adjustPitchOffset(-24)


baseKey = 70
comp.setKey(baseKey)

#comp.setScale(Voice.NATURAL_MINOR)

# Functions.

def stacNote(voice, note):
    voice.scaledNote(note, .5)
    voice.rest(.5)

def mainTheme(voice):
    for x in [0,1,2,3,4,2]:
        stacNote(voice, x)
    voice.scaledNote(5, 1)
    voice.scaledNote(4, .5)
    voice.scaledNote(3, .5)
    for x in [4,2,1,3,2,0,-1,1]:
        stacNote(voice, x)
    voice.scaledNote(0, 5)
    for x in [-1, -2, -1]:
        stacNote(voice, x)
    voice.scaledNote(0, 5)

def altTheme01(voice):
    for x in [0,1,2,3]:
        stacNote(voice, x)
    voice.scaledNote(4, 1)
    voice.scaledNote(3, .5)
    voice.scaledNote(2, .5)
    stacNote(voice, 3)
    stacNote(voice, 0)

    voice.scaledNote(3, 1)
    voice.scaledNote(2, .5)
    voice.scaledNote(1, .5)
    stacNote(voice, 2)
    stacNote(voice, -3)
    voice.scaledNote(0, 5)

def altTheme01Cont(voice, offset = 0):
    for x in [5, 4, 3, 1, 4, 3, 2, 0, 1]:
        voice.scaledNote(x + offset, .5)
    voice.scaledNote(2 + offset, 2)


# Script.

mainTheme(viola)
viola.rest(3)
comp.catchUpAll()

def dummyFunc(tf = False):
    cello.setVolume(127)
    mainTheme(cello)
    violin1.rest(4)
    altTheme01(violin1)
    violin1.rest(3)
    violin2.catchUp(violin1.whereAreWe())
    altTheme01Cont(violin1)
    altTheme01Cont(violin2, -2)

    if tf:
        viola.scaledNote(0, 2)
        viola.scaledNote(1, 2)
        viola.scaledNote(2, 2)
        viola.scaledNote(1, 2)
        viola.scaledNote(3, 2)
        viola.scaledNote(1, 2)
        viola.scaledNote(0, 2)
        viola.scaledNote(-1, 2)
        viola.scaledNote(0, 4)

dummyFunc()
cello.rest(1)
comp.setScale([0,2,3,5,7,8,11])
comp.catchUpAll()
#dummyFunc()
#cello.rest(1)
#comp.catchUpAll()
dummyFunc(True)


# End script.

filename = 'Output/' + __file__[:-2] + 'mid'
comp.writeToFile(filename)
os.system('fluidsynth -a alsa -g 1.5 ' + SETTING__SOUND_FONT + ' ./' + filename)
