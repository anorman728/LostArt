# Stand Up Straight With Your Shoulders Back
# Note: The code organization here is horrendous.

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

brass = comp.buildVoice(62, 'Brass Section')
brass.setVolume(80)

lowBrass = comp.buildVoice(62, 'Low Brass')
lowBrass.adjustPitchOffset(-24)
lowBrass.setVolume(100)

bariSax = comp.buildVoice(68, 'Baritone Sax')
bariSax.adjustPitchOffset(-24)
bariSax.setVolume(127)

tenorSax = comp.buildVoice(67, 'Tenor Sax')
tenorSax.adjustPitchOffset(-12)
tenorSax.setVolume(127)


baseKey = 67
comp.setKey(baseKey)

modScale = [0,3,5,6,7,9,10]
          # 0 1 2 3 4 5 6

comp.setScale(Voice.HEXATONIC_BLUES)


# Functions

def mainTheme(voice):
    for _ in range(0,2):
        voice.scaledNote(0, 1.5)
        voice.scaledNote(6, .5)
        voice.rest(1)
        voice.scaledNote(5, 1.5)
        voice.scaledNote(4, .5)
        voice.rest(1) # 6 beats

        voice.scaledNote(3, 1.5)
        voice.scaledNote(2, 1)
        voice.scaledNote(1, .5)
        voice.scaledNote(2, 1) # 4 beats

        voice.scaledNote(1, .5)
        voice.scaledNote(0, 1)
        voice.scaledNote(-1, .5) # 2 beats

def mainTheme_Harmony(voice):
    def dummyFunc():
        for _ in range(0,2):
            voice.scaledNote(7, .5)
            voice.scaledNote(6, .5)
            voice.rest(2)

    dummyFunc()
    voice.scaledNote(5, 1.5)
    voice.scaledNote(6, 1.5)
    voice.scaledNote(4, 1.5)
    voice.scaledNote(5, 1.5)

    dummyFunc()
    voice.scaledNote(5, 1.5)
    voice.scaledNote(6, 1.5)
    voice.scaledNote(4, 1.5)
    voice.scaledNote(2, 1.5)

def mainTheme_Harmony2(voice):
    def dummyFunc():
        voice.scaledNote(0, 1.5)
        voice.scaledNote(1, 1.5)

        voice.scaledNote(2, 1.5)
        voice.scaledNote(4, 1.5)

    dummyFunc()

    voice.scaledNote(3, 1.5)
    voice.scaledNote(2, 1)
    voice.scaledNote(3, .5)
    voice.scaledNote(2, 1)

    voice.scaledNote(1, .5)
    voice.scaledNote(0, 1)
    voice.scaledNote(-1, .5)

    dummyFunc()
    voice.scaledNote(5, 1.5)
    voice.scaledNote(4, 1)
    voice.scaledNote(5, .5)
    voice.scaledNote(6, 1)
    voice.scaledNote(6, .5)
    voice.scaledNote(6, 1.5)

def mainTheme_Perc1(voice):
    voice.rest(12)
    voice.rest(8.5)
    for _ in range(0, 2):
        voice.beat('Bass Drum 1', .5)
        voice.beat('Snare Drum 1', 1)

def mainTheme_Perc2(voice):
    for _ in range(0,8):
        voice.beat('Bass Drum 2', 1)
        voice.beat('Bass Drum 1', .5)
        voice.beat('High Tom 1', 0)
        voice.beat('Closed Hi-hat', 1.5)

def mainTheme_Perc3(voice):
    for _ in range(0,7):
        voice.rest(1.5)
        voice.beat('Open Hi-hat', 1.5)
    voice.beat('High Tom 1', .5)
    voice.beat('High Tom 2', .5)
    voice.beat('High Tom 1', .5)
    voice.beat('Mid Tom 1', 1)
    voice.beat('Mid Tom 2', 0)

def mainTheme_Perc3_Alt(voice):
    for _ in range(0,8):
        voice.rest(1.5)
        voice.beat('Open Hi-hat', 1.5)

def mainTheme_Perc4(voice):
    for _ in range(0,8):
        voice.beat('Bass Drum 2', 1)
        voice.beat('Bass Drum 1', .5)
        voice.beat('High Tom 1', 0)
        voice.beat('Closed Hi-hat', 1)
        voice.beat('Closed Hi-hat', .5)

def theme2(voice):
    def dummyFunc():
        voice.scaledNote(0, .5)
        voice.rest(2)
        voice.scaledNote(1, .5)
        voice.scaledNote(2, 1)
        voice.scaledNote(1, .5)
        voice.rest(1)
        voice.scaledNote(3, .5)
        voice.rest(1)
        voice.scaledNote(1, .5)
        voice.rest(1)

    dummyFunc()
    voice.scaledNote(3, .5)
    voice.scaledNote(2, 1)
    voice.scaledNote(1, .5)
    voice.scaledNote(0, 1)
    voice.scaledNote(-1, .5)

    dummyFunc()
    voice.scaledNote(2, .5)
    voice.scaledNote(4, .5)
    voice.scaledNote(2, .5)
    voice.scaledNote(3, .5)
    voice.scaledNote(4, .5)

def theme2_counter(voice):
    def dummyFunc():
        voice.scaledNote(0, .5)
        voice.scaledNote(-2, .5)
        voice.scaledNote(-1, .5)
        voice.scaledNote(0, .5)
        voice.rest(.5)

        voice.scaledNote(4, .5)
        voice.scaledNote(6, .5)
        voice.scaledNote(4, .5)
        voice.scaledNote(2, .5)
        voice.scaledNote(0, .5)
        voice.rest(.5)

        voice.scaledNote(0, .5)
        voice.scaledNote(0, .5)
        voice.scaledNote(-1, .5)
        voice.scaledNote(0, .5)

        voice.scaledNote(1, .5)
        voice.scaledNote(0, .5)
        voice.scaledNote(1, .5)

    dummyFunc()

    voice.scaledNote(2, .5)
    voice.scaledNote(1, .5)
    voice.scaledNote(2, .5)

    voice.scaledNote(3, .5)
    voice.scaledNote(2, .5)
    voice.scaledNote(1, .5)

    dummyFunc()

    voice.scaledNote(2, .5)
    voice.scaledNote(1, .5)
    voice.scaledNote(3, .5)
    voice.scaledNote(4, 1.5)

def theme3(voice):
    voice.scaledNote(0, 3)
    voice.scaledNote(1, 3)
    voice.scaledNote(2, 3)
    voice.scaledNote(1, 3)
    voice.scaledNote(4, 3)
    voice.scaledNote(1, 3)
    voice.scaledNote(2, 3)
    voice.scaledNote(1, 3)

def ending01(voice):
    for _ in range(0,3):
        voice.scaledNote(0, .5)
    voice.scaledNote(0, 1.5)

    voice.scaledNote(1, .5)
    voice.scaledNote(4, .5)
    voice.scaledNote(1, .5)
    voice.scaledNote(0, 1)

    voice.scaledNote(-1, .5)
    voice.scaledNote(0, 4)

def ending02(voice):
    voice.rest(7.5)
    voice.scaledNote(1, .5)
    voice.scaledNote(2, .5)
    voice.scaledNote(1, .5)
    voice.scaledNote(0, .5)
    voice.scaledNote(-2, .5)
    voice.scaledNote(-1, .5)
    voice.scaledNote(0, .5)

def endingPerc(voice):
    for _ in range(0,4):
        voice.rest(1.5)
        voice.beat('Open Hi-hat', 1.5)


# Composition

#comp.stop()#dmz1

mainTheme(bassGuitar)

comp.catchUpAll()
mainTheme(bassGuitar)
mainTheme_Harmony(leadGuitar)

comp.catchUpAll()
mainTheme(bassGuitar)
mainTheme_Harmony2(leadGuitar)
mainTheme_Perc1(perc)

comp.catchUpAll()
mainTheme(bassGuitar)
mainTheme_Harmony2(brass)
mainTheme_Perc2(perc)

comp.catchUpAll()
mainTheme(bassGuitar)
theme2(bariSax)
mainTheme_Perc2(perc)

comp.catchUpAll()
mainTheme(bassGuitar)
theme2_counter(tenorSax)
mainTheme_Perc2(perc)

comp.catchUpAll()
mainTheme(bassGuitar)
mainTheme_Perc2(perc)
theme3(lowBrass)

lowBrass.scaledNote(0, 12)
perc.rest(6)
for _ in range(0,2):
    perc.beat('Bass Drum 1', 1.5)
    perc.beat('Bass Drum 2', 1.5)

comp.setKey(baseKey - 6)
comp.catchUpAll()
mainTheme(brass)
mainTheme_Perc3(perc)

comp.catchUpAll()
mainTheme(brass)
mainTheme_Harmony(lowBrass)
mainTheme_Perc4(perc)

comp.catchUpAll()
mainTheme(brass)
theme2(tenorSax)
mainTheme_Perc4(perc)

comp.catchUpAll()
mainTheme(brass)
theme2_counter(bariSax)
mainTheme_Perc4(perc)

comp.catchUpAll()
mainTheme(brass)
mainTheme_Harmony2(lowBrass)
mainTheme_Perc4(perc)

comp.catchUpAll()
mainTheme(leadGuitar)
mainTheme_Perc3_Alt(perc)

comp.catchUpAll()
ending01(leadGuitar)
ending02(tenorSax)
endingPerc(perc)

# End script.

filename = 'Output/' + __file__[:-2] + 'mid'
comp.writeToFile(filename)
os.system('fluidsynth -a alsa -g 1.5 ' + SETTING__SOUND_FONT + ' ./' + filename)
