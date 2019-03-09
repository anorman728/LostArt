# Untitled
# This will be the boss battle, though.

# Import modules.
import os
import sys

# Import classes from other files.
sys.path.insert(0, './src')
from Composition import Composition
from Voice import Voice
from ScaledNote import ScaledNote
SC = ScaledNote

# Script below.

comp = Composition(2, 110)

strings = comp.buildVoice(41, 'Strings') # Same as violin, but different part.
violin = comp.buildVoice(41, 'String Ens')
tuba = comp.buildVoice(59, 'Tuba')
timpani = comp.buildVoice(48, 'Timpani')
cello = comp.buildVoice(43, 'Cello')

# "Metal" variant.
#strings = comp.buildVoice(31, 'Distorted Guitar')
#violin = comp.buildVoice(26, '"Steel" Acoustic Guitar')
#tuba = comp.buildVoice(34, 'Electric Bass')
#timpani = comp.buildVoice(117, 'Bass drum') # This is actually a "Taiko drum", whatever that is.
#cello = comp.buildVoice(30, 'Overdriven Guitar')

violin.setVolume(80)
strings.setVolume(80)
cello.setVolume(90)
tuba.setVolume(120)
timpani.setVolume(120)

timpani.adjustPitchOffset(-30)
cello.adjustPitchOffset(-12)
tuba.adjustPitchOffset(-24)
violin.adjustPitchOffset(12)

comp.setKey(60)
mode = [0,2,3,5,7,9,10]
comp.setScale(mode) # This is some kind of mode or something.

# Functions

def intro(voice):
    voice.scaledNote(-3, 2)
    voice.scaledNote(2,2)
    voice.scaledNote(1, 2)
    voice.scaledNote(0, 1)
    voice.scaledNote(-1, 1)
    voice.scaledNote(0, 2)
    voice.scaledNote(-2, 2)
    voice.scaledNote(-3, 3)
    voice.rest(1)

def main(voice, durMult = 1): # durMult * 8 beats
    ''' Beats = durMult * 8 '''
    voice.scaledNote(-3, durMult)
    voice.scaledNote(1, durMult)
    voice.scaledNote(2, durMult)
    voice.scaledNote(0, durMult)
    voice.scaledNote(1, durMult)
    voice.scaledNote(-1, durMult)
    voice.scaledNote(0, durMult)
    voice.scaledNote(-2, durMult)

def main_perc(voice, durMult = 1): # durMult * 8 beats
    ''' Beats = durMult * 8 '''
    for x in range(0, 4):
        voice.note(60, 2 * durMult)

def main_bk(voice): # 16 beats
    main_bk_intermed(voice, 0)
    main_bk_intermed(voice, 1)
    main_bk_intermed(voice, 2)
    main_bk_intermed(voice, 1)

def main_bk_intermed(voice, note_offset = 0): # 4 beats
    for x in range(0,4): # 2 beats
        voice.scaledNote(note_offset + -1, .25)
        voice.rest(.25)
    for x in range(0,2): # 2 beats
        voice.scaledNote(note_offset + -1, .25)
        voice.scaledNote(note_offset + -2, .25)
        voice.scaledNote(note_offset + -3, .25)
        voice.rest(.25)

def theme_01_01(voice):
    voice.scaledNote(6, 6.5)
    voice.scaledNote(SC(6, acc=-1), .5)
    voice.scaledNote(4, .5)
    voice.scaledNote(6, .5)

def theme_01_02(voice):
    voice.scaledChord([6, 4], 6.5)
    voice.scaledNote(SC(6, acc=-1), .5)
    voice.scaledNote(4, .5)
    voice.scaledNote(6, .5)

def theme_01_03(voice):
    voice.scaledChord([6, 4], 6.5)
    voice.scaledNote(SC(6, acc=-1), .5)
    voice.scaledNote(4, .5)
    voice.scaledNote(3, .5)

def theme_01_04(voice):
    for x in range(0,2):
        voice.scaledChord([6, 4], .5)
        voice.rest(.5)
    voice.rest(4.5)
    voice.scaledNote(SC(6, acc=-1), .5)
    voice.scaledNote(4, .5)
    voice.scaledNote(3, .5)

def theme_02_01(voice):
    voice.scaledNote(6, 1)
    voice.scaledNote(SC(6, acc=-1), 1)
    voice.scaledNote(4, 1)
    voice.scaledNote(6, 1)
    voice.scaledNote(7, 1)
    voice.scaledNote(6, 1)
    voice.scaledNote(SC(6, acc=-1), 1)
    voice.scaledNote(3, 1)

def theme_02_02(voice):
    voice.scaledChord([SC(2, acc=-1), -1, -3], 8)


# Script

#comp.stop()#dmz1

# Intro
intro(strings)
violin.catchUp(strings.whereAreWe())


# Main theme
for x in range(0,4): # 16 beats
    main(strings, .5) # 4 beats
violin.rest(8)
violin.scaledChord([-3, SC(-5, acc=-1)], 8)

timpani.catchUp(violin.whereAreWe())

for _ in range(0,4):
    main(strings, .5)
for _ in range(0,2):
    main(violin, 1)
    main_perc(timpani, 1)


# First theme
cello.catchUp(strings.whereAreWe())

for _ in range(0,2):
    main(strings, .5)
theme_01_01(cello)

# Keychange
comp.setKey(58)
for _ in range(0,2):
    main(strings, .5)
theme_01_02(cello)

# Return to previous key.
comp.setKey(60)

for _ in range(0,2):
    main(strings, .5)
theme_01_03(cello)


# Main theme.

timpani.catchUp(strings.whereAreWe())
for _ in range(0,4):
    main(strings, .5)
for _ in range(0,2):
    theme_01_04(cello)
    main_perc(timpani, 1)

cello.setVolume(100)
violin.setVolume(100)
tuba.catchUp(strings.whereAreWe())
cello.catchUp(strings.whereAreWe())
for _ in range(0,4):
    main(strings, .5)
main(tuba, 2)
main(cello, 2)

violin.catchUp(cello.whereAreWe())
for _ in range(0,4):
    main(strings, .5)
main(tuba, 2)
main(cello, 2)
main_bk(violin)

cello.setVolume(90)
violin.setVolume(80)

for _ in range(0,2):
    main(strings, .5)
tuba.scaledNote(-3, 8)


# Second theme
comp.catchUpAll()
for _ in range(0,2):
    main(strings, .5)
theme_02_01(cello)

# Keychange
comp.setKey(58)
for _ in range(0,2):
    main(strings, .5)
theme_02_01(cello)

# Return to previous key.
comp.setKey(60)
for _ in range(0,2):
    main(strings, .5)
theme_02_02(cello)


# Ending part 1
comp.catchUpAll()
for _ in range(0,4):
    main(strings, .5)
for _ in range(0,2):
    main(violin, 1)

comp.catchUpAll()
for _ in range(0,4):
    main(strings, .5)
for _ in range(0,2):
    main_perc(timpani, 1)

violin.setVolume(100)
main_bk(violin)


# Ending part 2
comp.catchUpAll()
for _ in range(0,3):
    main(strings, .5)
strings.scaledNote(-3, 3)

intro(cello)
intro(tuba)
main_perc(timpani,2)


filename = 'Output/game_what_was_found.mid'
comp.writeToFile(filename)
# To listen on write, uncomment below if you have a Linux OS with an
# alsa-based sound system.  (You'll need to have fluidsynth installed.)
# Otherwise, you'll need to open the sound file.
os.system('fluidsynth -a alsa -g 1.5 /usr/share/sounds/sf2/FluidR3_GM.sf2 ./' + filename)
