# Well-Deserved Rest

# This does not have a scale set, so it's using Major, but I think it's actually
# Phrygian, because it centers around the third note in the scale.

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

leadGuitar = comp.buildVoice(27, 'Lead Guitar')
leadGuitar.adjustPitchOffset(-12)

rhythmGuitar = comp.buildVoice(25, 'Rhythm Guitar')
rhythmGuitar.adjustPitchOffset(-12)

perc = comp.buildPerc()

bassGuitar = comp.buildVoice(34, 'Bass Guitar')
bassGuitar.adjustPitchOffset(-24)
bassGuitar.setVolume(127)

violin = comp.buildVoice(44, 'Violin')
# 44 is actually contrabass, but it sounds softer.


pianoLeft = comp.buildVoice(1, 'Piano Left Hand')
pianoLeft.adjustPitchOffset(-12)
pianoLeft.setVolume(80)

pianoRight = comp.buildVoice(1, 'Piano Right Hand')

baseKey=57
comp.setKey(baseKey)

# Functions

def main(voice, useLongEnd = False):
    def dummyFunc():
        voice.scaledChord([-3, 0, 2], 4)
        voice.scaledChord([2, 4, 6], 4)

    dummyFunc()
    voice.scaledChord([0, 3, 5], 8)

    dummyFunc()
    if useLongEnd:
        voice.asyncScaledChord([3, 5, 7], 16)
        voice.rest(8)
    else:
        voice.scaledChord([3, 5, 7], 8)

def mainPiano(left, right):
    def leftDum():
        for x in [-3, 0, 2, 0, 2, 4, 6, 4]:
            left.scaledNote(x, 1)

    def repeatme(voice, notes):
        for x in notes[0:-1]:
            voice.scaledNote(x, 1)
        for x in notes[1:]:
            voice.scaledNote(x, 1)

    leftDum()
    repeatme(left, [5, 3, 0, -2, -4])
    leftDum()
    repeatme(left, [7, 5, 3, 0, -2])

    if right != None:
        main(right)

def drum01(voice, count = 8):
    for _ in range(0, count):
        voice.beat('Low Tom 1', 1.5)
        voice.beat('Low Tom 1', .5)
        voice.beat('Snare Drum 1', 1)
        voice.beat('Low Tom 1', 1)

def mainBassCommon(voice):
    voice.scaledNote(2, 3)
    voice.scaledNote(4, 1)
    voice.scaledNote(6, 3)
    voice.scaledNote(7, 1)

def mainBass1(voice):
    mainBassCommon(voice)
    voice.scaledNote(5, 6)
    voice.scaledNote(6, .5)
    voice.scaledNote(5, .5)
    voice.scaledNote(3, .5)
    voice.scaledNote(1, .5)

def mainBass2(voice):
    mainBassCommon(voice)
    voice.scaledChord([5, 7], 6)
    voice.scaledNote(8, 1)
    voice.scaledNote(7, 1)

def mainBass3(voice):
    voice.scaledNote(9, 3)
    voice.scaledNote(11, 1)
    voice.scaledChord([8, 6], 3)
    voice.scaledNote(6, 1)
    voice.scaledChord([7, 5], 6)
    voice.scaledNote(8, 2)

def mainBass4(voice):
    voice.scaledNote(9, 3)
    voice.scaledNote(7, 1)
    voice.scaledNote(8, 3)
    voice.scaledNote(6, 1)
    voice.scaledChord([7, 5], 8)

def mainEndBass(voice):
    voice.scaledNote(8, 2)
    voice.scaledNote(9, 6)

    voice.scaledNote(7, 2)
    voice.scaledNote(8, 6)

    voice.scaledNote(6, 2)
    voice.scaledNote(7, 18)

def mainEndViolin(voice):
    voice.rest(2)
    voice.scaledNote(9, 8)
    voice.scaledNote(8, 8)
    voice.scaledChord([7, 4], 18)

def mainEndPianoLeft(voice):
    voice.rest(26)
    voice.asyncScaledNote(2, 10)
    voice.rest(2)
    voice.asyncScaledNote(4, 8)
    voice.rest(3)
    voice.asyncScaledNote(7, 5)


# Composition below.

main(leadGuitar)
perc.rest(16)
drum01(perc, 4)

comp.catchUpAll()
main(leadGuitar)
drum01(perc)
mainBass1(bassGuitar)
mainBass2(bassGuitar)

comp.catchUpAll()
main(leadGuitar)
drum01(perc)
mainBass3(bassGuitar)
mainBass4(bassGuitar)
violin.setVolume(80)
violin.catchUp(bassGuitar.whereAreWe()-6)
violin.scaledNote(0, 6)
violin.setVolume(100)

perc.beat('Low Tom 1', 0)
comp.catchUpAll()

violin.scaledNote(2, 4)
violin.scaledNote(4, 4)
violin.scaledNote(3, 8)

violin.scaledNote(2, 4)
violin.scaledNote(4, 4)
violin.scaledNote(5, 8)

main(leadGuitar)

comp.catchUpAll()
mainBass1(violin)
mainBass2(violin)
main(pianoLeft)
main(pianoRight)

comp.catchUpAll()
mainBass3(violin)
mainBass4(violin)
pianoLeft.setVolume(100)
mainPiano(pianoLeft, pianoRight)

comp.catchUpAll()
for x in [violin, bassGuitar]:
    mainBass1(x)
    mainBass2(x)
mainPiano(pianoLeft, None)
main(leadGuitar)
drum01(perc)

comp.catchUpAll()
for x in [violin, bassGuitar]:
    mainBass3(x)
    mainBass4(x)
mainPiano(pianoLeft, None)
main(leadGuitar)
drum01(perc)
perc.beat('Low Tom 1', 0)

comp.catchUpAll()
pianoRight.setVolume(100)
main(leadGuitar, True)
main(pianoLeft, True)
mainBass1(pianoRight)

mainBassCommon(pianoRight)
pianoRight.scaledChord([5, 7], 8)

#comp.catchUpAll()
#mainEndBass(bassGuitar)
#mainEndViolin(violin)
#mainEndPianoLeft(pianoLeft)

# End script.

filename = 'Output/' + __file__[:-2] + 'mid'
comp.writeToFile(filename)
os.system('fluidsynth -a alsa -g 1.5 ' + SETTING__SOUND_FONT + ' ./' + filename)

