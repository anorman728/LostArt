# Main theme

# Import modules.
import os
import sys

# Import classes from other files.
sys.path.insert(0, './src')
from Composition import Composition
from Voice import Voice

# Script below.

comp = Composition(2, 110)

oboe = comp.buildVoice(69, 'Oboe')
guitar = comp.buildVoice(25, 'Guitar')
violin = comp.buildVoice(41, 'Violin')
horn = comp.buildVoice(61, 'French Horn')
cello = comp.buildVoice(43, 'Cello')
timpani = comp.buildVoice(48, 'Timpani')
lowStringSec = comp.buildVoice(50, 'Low string section')
lowStringSec.adjustPitchOffset(-24)
tuba = comp.buildVoice(61, 'Tuba') # 61 is actually french horn, because it's the only brass that doesn't sound terrible.
tuba.adjustPitchOffset(-24)

# Tweak volume, because some voices are really low for some reason.
violin.setVolume(80)
guitar.setVolume(80)
horn.setVolume(127)
tuba.setVolume(127)
cello.setVolume(90)
lowStringSec.setVolume(90)
timpani.setVolume(127)

key = 61
comp.setKey(key)

# Functions

def main(voice):
    voice.scaledNote(5,1) # Pickup.
    voice.scaledNote(8,2)

    voice.scaledNote(7,1)
    voice.scaledNote(6,1)
    voice.scaledNote(7,2)

    voice.scaledNote(6,1)
    voice.scaledNote(5,1)
    voice.scaledNote(6,2)

    voice.scaledNote(5,1)
    voice.scaledNote(4,1)
    voice.scaledNote(5,3)

def mainHarmony(voice):
    voice.rest(1)
    voice.scaledChord([-6],1)
    voice.scaledChord([-5],1)
    voice.scaledChord([-4],2)

    voice.scaledChord([-5],1)
    voice.scaledChord([-4],1)
    voice.scaledChord([-3],2)

    voice.scaledChord([-4],1)
    voice.scaledChord([-3],1)
    voice.scaledChord([-2],2)

    voice.scaledChord([-2, -5],3)

def background0(voice1, voice2):
    # voice1
    for y in [5,6,7,7]:
        for x in range(0,2):
            voice1.scaledChord([y, y-2, y-5], .5)
            voice1.rest(.5)
            for z in range(0,2):
                # Pyramid of death!
                voice1.scaledChord([y, y-2], .5)
                voice1.rest(.5)

    # voice2
    voice2.rest(18)
    voice2.scaledChord([5],1)
    voice2.scaledChord([6],1)
    voice2.scaledChord([7],1)
    voice2.scaledChord([8],1)
    voice2.scaledChord([9],1)
    voice2.scaledChord([10],1)

def background0Perc(voice):
    # The percussion part to go with background0.
    for x in range(8):
        voice.note(30,2)
        voice.rest(1)

def background1Intermed(voice, chordArr):
    voice.scaledChord(chordArr, .5)
    voice.rest(.5)
    voice.scaledChord(chordArr, .5)
    voice.rest(.5)
    voice.scaledChord(chordArr, .5)
    voice.scaledChord(chordArr, .5)

def background1(voice):
    for x in range(0,3):
        background1Intermed(voice, [-2,-5])
    background1Intermed(voice, [0, -2])
    background1Intermed(voice, [-1, -3])
    background1Intermed(voice, [-3,-6])

def background1Perc(voice):
    # The percussion part to go with background1.
    for x in range(0,6):
        background1PercIntermed(voice)

def background1PercIntermed(voice):
    for y in range(0,2):
        voice.note(30, 1)
    for y in range(0,2):
        voice.note(30, .5)

def theme1(voice):
    voice.scaledNote(5,8)
    voice.scaledNote(6,.5)
    voice.scaledNote(7,.5)

    voice.scaledNote(5,8)
    voice.scaledNote(6,.5)
    voice.scaledNote(7,.5)

    voice.scaledNote(8,2)
    voice.scaledNote(7,2)
    voice.scaledNote(4,2)
    voice.scaledNote(5,6)

def background1Alt(voice1, voice2):
    background1Intermed(voice1, [-2, -5])
    background1Intermed(voice1, [0, -2])
    background1Intermed(voice1, [-1, -3])
    background1Intermed(voice1, [2, 0])
    background1Intermed(voice1, [4, 2])
    voice2.catchUp(voice1.whereAreWe())
    for x in [voice1, voice2]:
        background1Intermed(x, [3, 1])
        background1Intermed(x, [5, 3])
        background1Intermed(x, [7, 5])
        background1Intermed(x, [8, 6])
        for y in range(0,2):
            background1Intermed(x, [9, 7])
        for y in range(0,2):
            background1Intermed(x, [9, 6])

def background1AltBase(voice):
    voice.rest(27)
    for x in range(0, 2):
        voice.scaledChord([7], 1)
        voice.rest(2)
    for x in range(0, 2):
        voice.scaledChord([6], 1)
        voice.rest(2)

def conclusion(voice1, voice2):
    voice1.scaledNote(5,1.5)
    voice1.scaledNote(8,3)
    voice1.scaledNote(7,3)
    voice1.scaledNote(6,3)
    voice1.scaledNote(6,1)
    voice1.scaledNote(5,1)
    voice1.scaledNote(4,1)
    voice1.scaledNote(5,11)

    voice2.rest(20.5)
    voice2.scaledChord([-2, -5], 3)
    

#Intro
main(oboe)

guitar.catchUp(oboe.whereAreWe())
main(oboe)
mainHarmony(guitar)

# Rest & change tempo.
oboe.rest(2)
comp.setTempo(180)

# First run of background 1.
background1(violin)
oboe.catchUp(violin.whereAreWe())
for x in range(0,2):
    background1(violin)
theme1(oboe)

# Main theme again.
lowStringSec.catchUp(violin.whereAreWe())
horn.catchUp(violin.whereAreWe() -1)
background0(violin, lowStringSec)
main(horn)

horn.catchUp(violin.whereAreWe()-1)
cello.catchUp(horn.whereAreWe())
background0(violin, lowStringSec)
main(horn)
mainHarmony(cello)

# One last background1 before key change.
comp.catchUpAll()
background1(cello)

# Change key and return to background1.

comp.setKey(key+4)
comp.catchUpAll()

background1(horn)
background1Perc(timpani)
violin.catchUp(timpani.whereAreWe())

for x in range(0,2):
    background1(horn)
    background1Perc(timpani)
theme1(violin)

# Main theme.

horn.adjustPitchOffset(-12)
tuba.adjustPitchOffset(-12)

cello.catchUp(horn.whereAreWe()-1)
tuba.catchUp(horn.whereAreWe())
timpani.catchUp(horn.whereAreWe())
background0(horn, tuba)
background0Perc(timpani)
main(cello)

lowStringSec.adjustPitchOffset(12)
lowStringSec.setVolume(100)
cello.catchUp(horn.whereAreWe()-1)
lowStringSec.catchUp(cello.whereAreWe())
tuba.catchUp(horn.whereAreWe())
timpani.catchUp(horn.whereAreWe())
background0(horn, tuba)
background0Perc(timpani)
main(cello)
mainHarmony(lowStringSec)

# Alt background 1, leading to conclusion.
comp.catchUpAll()
background1Alt(horn, cello)
background1AltBase(tuba)
for x in range(0,2):
    background1Perc(timpani)

timpani.catchUp(cello.whereAreWe())
for x in range(0,2):
    background1PercIntermed(timpani)
timpani.note(30,1) # One last note

timpani.rest(6)


# Finish

comp.catchUpAll()
comp.setTempo(140)
lowStringSec.setVolume(80)
conclusion(oboe, lowStringSec)

filename = 'Output/game_maintheme.mid'
comp.writeToFile(filename)
# To listen on write, uncomment below if you have a Linux OS with an
# alsa-based sound system.  (You'll need to have fluidsynth installed.)
# Otherwise, you'll need to open the sound file.
#os.system('fluidsynth -a alsa -g 1.5 /usr/share/sounds/sf2/FluidR3_GM.sf2 ./' + filename)
