# Sleep music.
# Having chronic insomnia, I thought I'd make some music that might help.
# Though all of individual chords are pleasant to listen to, the song itself is
# slow, uninteresting, not at all innovative, repetitive, no big volume changes.

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

comp = Composition(2, 100)

strings = comp.buildVoice(50, 'Strings')
cello = comp.buildVoice(43, 'Cello')

melodyVol = 100
backgroundVol = 60

cello.adjustPitchOffset(-12)


baseKey = 58
comp.setKey(baseKey)

comp.setScale(Voice.MAJOR)


# Functions

def motive01(voice):
    voice.scaledNote(0, 4)
    voice.scaledChord([0, 2, 4], 4)
    voice.scaledChord([0, 2, 5], 4)
    voice.scaledChord([-1, 1, 3], 4)
    voice.scaledChord([0, 2, 4], 4)

def motive02(voice, offset):
    for x in [0, 3, 2, 1, 2, 0]:
        voice.scaledNote(x + offset, 2)
    voice.scaledNote(1 + offset, 4)

def motive02_bk(voice, offset):
    voice.scaledChord([x + offset for x in [0, 2, 4]], 12)
    voice.scaledChord([x + offset for x in [1, 3]], 4)

def motive02_over(voice1, voice2):
    for x in [0, 1, 2]:
        motive02(voice1, x)
        motive02_bk(voice2, x)

    voice2.scaledChord([0, 2], 2)
    voice2.scaledNote(1, 2)
    voice2.scaledChord([1, 3], 4)

    voice1.scaledNote(2, 4)
    voice1.scaledNote(1, 4)

def motive03(voice, offset):
    for _ in range(0, 3):
        voice.scaledNote(offset, 2)
    voice.scaledNote(2 + offset, 4)

def motive03_bk(voice, offset):
    voice.scaledChord([x + offset for x in [0, 2]], 10)

def motive03_over(voice1, voice2):
    for x in [0, 1, 2]:
        motive03(voice1, x)
        motive03_bk(voice2, x)

    for x in [5, 4, 2]:
        voice1.scaledNote(x, 2)
    voice1.scaledNote(1, 6)

    voice2.scaledChord([5, 7], 6)
    voice2.scaledChord([1, 4], 2)
    voice2.scaledChord([1, SC(3, acc=1)], 4)

def motive03_over_alt(voice1, voice2):
    # Question
    voice1.setVolume(melodyVol)
    voice2.setVolume(backgroundVol)
    motive03(voice1, 0)
    motive03_bk(voice2, 0)

    # Answer
    voice1.setVolume(backgroundVol)
    voice2.setVolume(melodyVol)
    motive03(voice2, 1)
    motive03_bk(voice1, 1)

    # Question
    voice1.setVolume(melodyVol)
    voice2.setVolume(backgroundVol)
    motive03(voice1, 2)
    motive03_bk(voice2, 2)

    # Answer
    voice1.setVolume(backgroundVol)
    voice2.setVolume(melodyVol)
    for x in [5, 4, 2]:
        voice2.scaledNote(x, 2)
    voice2.scaledNote(1, 6)

    voice1.scaledChord([5, 7], 6)
    voice1.scaledChord([1, 4], 2)
    voice1.scaledChord([1, SC(3, acc=1)], 4)


def theme01(voice):
    voice.scaledNote(0, 2)
    voice.scaledNote(1, 2)

    voice.scaledNote(4, 2)
    voice.scaledNote(5, 2)

    voice.scaledNote(5, 2)
    voice.scaledNote(2, 2)

    voice.scaledNote(3, 2)
    voice.scaledNote(4, 2)

    voice.scaledNote(4, 4)

def theme02(voice):
    voice.scaledNote(0, 2)
    voice.scaledNote(1, 2)

    voice.scaledNote(4, 2)
    voice.scaledNote(5, 2)

    voice.scaledNote(3, 1)
    voice.scaledNote(1, 1)
    voice.scaledNote(2, 1)
    voice.scaledNote(3, 1)

    voice.scaledNote(2, 2)
    voice.scaledNote(1, 2)

def theme02_bk(voice):
    voice.scaledNote(0, 4)
    voice.scaledNote(4, 4)

    voice.scaledNote(3, 2)
    voice.scaledNote(2, 2)

    voice.scaledNote(2, 4)

def theme03(voice):
    voice.scaledNote(0, 2)
    voice.scaledNote(-1, 2)

    voice.scaledNote(1, 2)
    voice.scaledNote(0, 2)

    for x in [0, 1, 2]:
        voice.scaledNote(2 - x, 2)
        voice.scaledNote(1 - x, 2)

        voice.scaledNote(0 - x, 2)
        voice.scaledNote(-1 - x, 2)

    voice.scaledNote(-2, 2)
    voice.scaledNote(-1, 2)

    voice.scaledNote(0, 2)
    voice.scaledNote(1, 2)

    voice.scaledNote(2, 4)
    voice.scaledNote(1, 4)
    voice.scaledNote(1, 4)
    voice.scaledNote(0, 4)
    voice.scaledNote(0, 4)
    voice.rest(4)


def theme03_bk(voice):
    voice.scaledChord([0, 2], 4)
    voice.scaledChord([1, 3], 4)

    for x in [0, 1, 2]:
        voice.scaledChord([y - x for y in [2, 4]], 8)

    voice.scaledChord([0, 2], 4)
    voice.scaledChord([2, 4], 4)

    voice.scaledChord([0, 2, 4], 4)
    voice.scaledChord([-1, 1, 4], 4)
    voice.scaledChord([-1, 1, 3], 4)
    voice.scaledChord([-2, 0, 2], 4)
    voice.scaledChord([-3, 0, 2], 4)
    voice.scaledChord([-3, 0, 2], 4)

def theme04_01(voice):
    voice.setVolume(melodyVol)
    for x in [0, 0, 1, 2, 2, 0, 1, 1, -1]:
        voice.scaledNote(x, 2);
    voice.scaledNote(0, 4)

def theme04_01_bk(voice):
    voice.setVolume(backgroundVol)
    voice.scaledChord([0, 2], 6)
    voice.scaledChord([2, 4], 6)
    voice.scaledChord([1, 3], 6)
    voice.scaledChord([0, 2], 4)

def theme04_02(voice):
    voice.setVolume(melodyVol)

    for x in [0, 2, 2, 0, 3, 3, 0, 4, 3, 1]:
        voice.scaledNote(x, 2)
    voice.scaledNote(2, 4)

def theme04_02_bk(voice):
    voice.setVolume(backgroundVol)

    voice.scaledChord([0, 2, 4], 6)

    voice.scaledChord([0, 2, 4], 2)
    voice.scaledChord([0, 3, 5], 4)

    voice.scaledChord([0, 2, 5], 2)
    voice.scaledChord([-1, 1, 4], 2)
    voice.scaledChord([-1, 1, 3], 4)

    voice.scaledChord([0, 2, 4], 4)


# Composition

#comp.stop()#dmz1

strings.setVolume(backgroundVol)
cello.setVolume(melodyVol)

motive01(strings)

comp.catchUpAll()
motive01(strings)
theme01(cello)


###

cello.scaledNote(0, 4)

comp.catchUpAll()
motive02_over(cello, strings)

comp.catchUpAll()
theme02_bk(strings)
theme02(cello)

cello.setVolume(backgroundVol)
strings.setVolume(melodyVol)

comp.catchUpAll()
motive02_over(strings, cello)

strings.scaledChord([0, -3], 4)
strings.scaledChord([1, -1], 4)

comp.setKey(baseKey + 2)
strings.scaledChord([0, -4], 4)
strings.scaledChord([0, -3], 4)


###

cello.setVolume(melodyVol)
strings.setVolume(backgroundVol)

comp.catchUpAll()
motive01(strings)
theme01(cello)

strings.scaledChord([0, 2, 4], 4)
strings.scaledChord([0, 2, 5], 4)
strings.scaledChord([0, 3, 5], 4)
strings.scaledChord([1, 4, 6], 4)

comp.catchUpAll()
theme03(cello)
theme03_bk(strings)

cello.setVolume(backgroundVol)
strings.setVolume(melodyVol)
comp.catchUpAll()
theme03(strings)
theme03_bk(cello)

cello.setVolume(melodyVol)
strings.setVolume(backgroundVol)
comp.catchUpAll()
motive03_over(cello, strings)

cello.setVolume(backgroundVol)
strings.setVolume(melodyVol)
comp.catchUpAll()
motive01(cello)
theme01(strings)

comp.catchUpAll()
motive03_over(strings, cello)

cello.scaledChord([0, 2, 4], 4)
cello.scaledChord([0, 2, 5], 4)
cello.scaledChord([0, 3, 5], 4)
cello.scaledChord([1, 4, 6], 4)


###


comp.catchUpAll()
# Question
theme04_01(cello)
theme04_01_bk(strings)

# Answer
theme04_02(strings)
theme04_02_bk(cello)

# Start at 0, 2, 4
strings.setVolume(backgroundVol)
strings.scaledChord([0, 2, 4], 4)
strings.scaledChord([-1, 1, 4], 4)
strings.scaledChord([-2, 0, 3], 4)
strings.scaledChord([-3, -1, 2], 4)
strings.scaledChord([-3, 0, 2], 4)
# End at 0, 2
comp.catchUpAll()

motive03_over_alt(cello, strings)

strings.setVolume(backgroundVol)
cello.setVolume(backgroundVol)

strings.scaledChord([1, 3, 5], 4)
strings.scaledChord([0, 2, 5], 4)
strings.scaledChord([-1, 1, 3], 4)
strings.scaledChord([-3, -1, 2], 4)
comp.catchUpAll()
strings.scaledChord([-2, 0, 2], 8)
cello.rest(4)
cello.scaledNote(0, 4)

###

comp.catchUpAll()
cello.setVolume(backgroundVol)
strings.setVolume(melodyVol)
theme02_bk(cello)
theme02(strings)

cello.setVolume(melodyVol)
strings.setVolume(backgroundVol)

for x in [3, 2, -1]:
    cello.scaledNote(x, 4)

comp.catchUpAll()
cello.scaledNote(0, 16)
strings.rest(4)
strings.scaledChord([-2, 0, 3], 4)
strings.scaledChord([-3, 0, 2], 8)




# End script.

filename = 'Output/' + __file__[:-2] + 'mid'
comp.writeToFile(filename)
os.system('fluidsynth -a alsa -g 1.5 ' + SETTING__SOUND_FONT + ' ./' + filename)
