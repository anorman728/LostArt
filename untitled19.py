# I Fight For My King

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

violinSol = comp.buildVoice(41, 'Violin Solo')
violinSol.setVolume(70)

harp = comp.buildVoice(47, 'Harp')
harp.setVolume(100)

stringEns = comp.buildVoice(49, 'Strings')

cello = comp.buildVoice(43, 'Cello')
cello.adjustPitchOffset(-24)

fHorn = comp.buildVoice(61, 'French Horn')
fHorn.adjustPitchOffset(-12)

perc = comp.buildPerc()

timpani = comp.buildVoice(48, 'Timpani')


baseKey = 69
comp.setKey(baseKey)

comp.setScale(Voice.DORIAN)

# Functions

# Slow functions.

def introMel1(voice):
    voice.slideVolume(80, 100, 2)
    voice.scaledNote(0, 4)
    voice.scaledNote(-3, 4)
    voice.scaledNote(-1, 4)

    voice.scaledNote(-2, 1)
    voice.scaledNote(-4, 1)
    voice.scaledNote(-3, 6)
    voice.rest(2)

def introHarm1(voice):
    voice.rest(16)
    voice.slideVolume(40, 100, 4, 20)
    voice.scaledChord([-3, -6, -8], 4)
    voice.rest(2)

def introMel2(voice):
    voice.slideVolume(80, 100, 2)
    voice.scaledNote(0, 4)
    voice.scaledNote(-3, 4)

    voice.scaledNote(0, 1)
    voice.scaledNote(1, 1)
    voice.scaledNote(2, 8)
    voice.rest(2)

def introHarm2(voice):
    voice.rest(12)
    voice.slideVolume(40, 100, 4, 20)
    voice.scaledChord([-1, SC(-3, acc=1), -5], 2)
    voice.scaledChord([-1, -3, -5], 4)
    voice.rest(2)

def mainSlowMel1_1(voice):
    voice.rest(1)
    voice.scaledNote(0, 1)
    voice.scaledNote(4, 2)

    voice.scaledNote(3, 1)
    voice.scaledNote(2, 1)
    voice.scaledNote(1, 2)

    voice.scaledNote(2, 1)
    voice.scaledNote(1, 1)
    voice.scaledNote(0, 1)
    voice.scaledNote(-1, 1)
    
    voice.scaledNote(0, 3)
    voice.rest(1)

def mainSlowHar1_1(voice1, voice2):
    def dummyFunc2(arr):
        voice1.scaledChord(arr, .5)
        voice1.rest(.5)
    def dummyFunc(arr, sec):
        for x in arr:
            dummyFunc2([x, sec])
    dummyFunc([-2, -4, -7, -4], -2)
    dummyFunc([-3, -5, -7, -5], -3)
    dummyFunc([-4, -7, -9, -11], -4)
    dummyFunc2([-9, -11])
    dummyFunc2([-7, -10])
    dummyFunc2([-5, -9])
    dummyFunc2([-3, -7])

    voice2.rest(12)
    voice2.scaledNote(-5, 1)
    voice2.scaledNote(-4, 1)
    voice2.scaledNote(-2, 1)
    voice2.scaledNote(0, 1)

def mainSlowMel1_2(voice):
    voice.rest(1)
    voice.scaledNote(0, 1)
    voice.scaledNote(4, 2)

    voice.scaledNote(5, 1)
    voice.scaledNote(6, 1)
    voice.scaledNote(5, .125)
    voice.scaledNote(6, .125)
    voice.scaledNote(5, .75)
    voice.scaledNote(3, 1)

    voice.scaledNote(4, 2)
    voice.scaledNote(2, 1)
    voice.scaledNote(4, 1)

    voice.slideVolume(100, 90, 3)
    voice.scaledNote(3, 3)
    voice.rest(1)

def mainSlowHar1_2(voice1, voice2):
    voice1.scaledChord([0, -2, -4], 4)
    voice1.scaledChord([-3, -5, -7], 4)
    voice1.scaledChord([-5, -8, -10], 4)
    voice1.scaledChord([-7, -9, -11], 4)

    voice2.scaledNote(0, 1)
    voice2.scaledNote(4, 1)
    voice2.scaledNote(3, 1)
    voice2.scaledNote(2, 1)

    voice2.scaledNote(3, 1)
    voice2.scaledNote(4, 1)
    voice2.scaledNote(3, 1)
    voice2.scaledNote(1, 1)

    voice2.scaledNote(2, 1)
    voice2.scaledNote(1, 1)
    voice2.scaledNote(0, 1)
    voice2.scaledNote(-1, 1)

    voice2.scaledStrum([-7,-5,-2], 2)
    voice2.rest(2)

def mainSlowMel2_1(voice):
    voice.slideVolume(40, 100, .5)
    voice.scaledNote(0, 1)
    voice.scaledNote(-3, 1)
    voice.scaledNote(0, 1)
    voice.scaledNote(1, 1)

    voice.scaledNote(2, 2)
    voice.scaledNote(4, 1)
    voice.scaledNote(2, 1)

    voice.scaledNote(3, 2)
    voice.scaledNote(2, 1)
    voice.scaledNote(1, 1)

    voice.scaledNote(2, 3)
    voice.rest(1)
    #voice.scaledNote(SC(-3, vo=-10), 1)

def mainSlowHar2_1(voice):
    voice.scaledStrum([-7, -5, -3], 1)
    voice.scaledNote(-4, 1)
    voice.scaledStrum([SC(-9, acc=-1), -7, -5], 1)
    voice.scaledNote(-4, 1)

    voice.scaledStrum([-7, -5, -3], 2)
    voice.scaledStrum([-5, -3, -1], 1)
    voice.scaledNote(-3, 1)

    voice.scaledStrum([-6, -4, -2], 1)
    voice.scaledNote(-1, .5)
    voice.scaledNote(-2, .5)
    voice.scaledStrum([-7, -5, -3], 1)
    voice.scaledNote(-4, 1)

    voice.scaledStrum([-7, -5, -3], 4)

def mainSlowHar2_1_Reprise(voice):
    voice.slideVolume(60, 100, 2)
    voice.scaledNote(7, 4)
    voice.scaledNote(9, 4)
    voice.scaledNote(10, 4)
    voice.slideVolume(100, 80, 4)
    voice.scaledNote(9, 4)

def mainSlowMel2_2(voice):
    voice.slideVolume(40, 100, .5)
    voice.scaledNote(0, 1)
    voice.scaledNote(-3, 1)
    voice.scaledNote(0, 1)
    voice.scaledNote(1, 1)

    voice.scaledNote(2, 2)
    voice.scaledNote(1, 1)
    voice.scaledNote(0, 1)

    voice.scaledNote(1, 2)
    voice.scaledNote(0, 1)
    voice.scaledNote(-1, 1)

    voice.scaledNote(0, 3)
    voice.rest(1)

def mainSlowHar2_2(voice):
    voice.scaledStrum([-7, -5, -3], 1)
    voice.scaledNote(-4, 1)
    voice.scaledStrum([SC(-9, acc=-1), -7, -5], 1)
    voice.scaledNote(-4, 1)

    voice.scaledStrum([-7, -5, -3], 2)
    voice.scaledStrum([-5, -3, -1], 1)
    voice.scaledNote(-3, 1)

    voice.scaledStrum([-8, -6, -4], 2)
    voice.scaledStrum([-10, -8, -5], 1)
    voice.scaledNote(-4, 1)

    voice.scaledStrum([-11, -9, -4], 4)

def mainSlowHar2_2_Reprise(voice):
    voice.scaledNote(7, 4)
    voice.scaledNote(9, 4)
    voice.scaledNote(6, 4)
    voice.slideVolume(100, 60, 4)
    voice.scaledNote(3, 4)

def mainSlowHar2_2_Reprise_Tim(voice):
    voice.rest(14)
    voice.note(20, 2)

def mainSlowMel1Mix_1(voice):
    voice.scaledNote(0, 1)
    voice.scaledNote(1, 1)
    voice.scaledNote(3, 1)
    voice.scaledNote(2, 1)

    voice.scaledNote(-1, 4)

    voice.scaledNote(1, 1)
    voice.scaledNote(0, 1)
    voice.scaledNote(1, 1)
    voice.scaledNote(2, 1)

    voice.scaledNote(2, 8)

def mainSlowHar1Mix_1(voice1, voice2, voiceBass):
    voice1.scaledNote(0, 4)
    voice1.scaledNote(-3, 4)

    voice1.scaledNote(-2, 2)
    voice1.scaledNote(-4, 2)

    voice1.scaledNote(-2, 1)
    voice1.scaledNote(-4, 1)
    voice1.scaledChord([-2, -5, -7], 2)
    voice1.scaledChord([-3, -5, -7], 4)
    voice1.rest(2)

    voiceBass.scaledNote(7, 4)
    voiceBass.scaledNote(4, 4)
    voiceBass.scaledNote(3, 4)
    voiceBass.scaledNote(5, 4)
    voiceBass.scaledNote(4, 4)
    voiceBass.rest(2)

    voice2.scaledStrum([-7, -5, -3], 2)
    voice2.scaledStrum([-5, -3, -1], 2)

    voice2.scaledStrum([-10, -8, -6], 2)
    voice2.scaledStrum([-8, -6, -4], 2)

    voice2.scaledStrum([-4, -2], 2)
    voice2.scaledStrum([-8, -6, -4], 2)

    voice2.scaledStrum([-6, -4, -2], 1)
    voice2.scaledNote(-1, .5)
    voice2.scaledNote(-2, .5)
    voice2.scaledChord([-3, -5, -7], 1)
    voice2.scaledNote(-4, 1)
    voice2.scaledChord([-3, -5, -7], 6)
    voice2.rest(2)

def mainSlowMel1Mix_2(voice):
    voice.rest(14)
    voice.scaledNote(-3, 1)
    voice.scaledNote(-1, 1)

def mainSlowHar1Mix_2(voice1, voice2):
    voice1.slideVolume(80, 100, 6)
    for _ in range(0,4):
        voice1.scaledChord([0, -2, -4], .5)
        voice1.rest(.5)
    for _ in range(0,4):
        voice1.scaledChord([2, 0, -2], .5)
        voice1.rest(.5)
    stringEns.slideVolume(70, 100, 6)
    voice1.scaledChord([1, -2, -4], 4)
    voice1.scaledChord([-1, -4, -6], 4)

    voice2.scaledNote(-4, 1)
    voice2.scaledNote(-2, 1)
    voice2.scaledNote(0, 1)
    voice2.scaledNote(-2, 1)

    voice2.scaledNote(-2, 1)
    voice2.scaledNote(0, 1)
    voice2.scaledNote(2, 1)
    voice2.scaledNote(0, 1)

    voice2.scaledNote(1, 1)
    voice2.scaledNote(0, 1)
    voice2.scaledNote(-2, 1)
    voice2.scaledNote(-4, 1)

    voice2.scaledNote(-2, 1)
    voice2.scaledNote(-3, 1)
    voice2.scaledNote(-2, 1)
    voice2.scaledNote(0, 1)

def mainModPerc2_Alt1(voice):
    voice.rest(12)
    for _ in range(0, 2):
        voice.beat('Snare Drum 1', 1)
        voice.beat('Snare Drum 2', 1)

def mainModHar1Mix_1(voice):
    def dummyFunc(chord):
        for _ in range(0, 4):
            voice.scaledChord(chord, .33)
            voice.scaledChord(chord, .33)
            voice.scaledChord(chord, .34)

    dummyFunc([0, -2, -4])
    dummyFunc([2, 0, -2])
    dummyFunc([1, -2, -4])
    dummyFunc([-1, -4, -6])

def mainModBass1Mix_1(voice):
    def dummyFunc(note):
        voice.scaledNote(note, 4)
        #for _ in range(0, 2):
        #    voice.scaledNote(note, .5)
        #    voice.rest(1.5)

    for x in [0, 2, 1, -1]:
        dummyFunc(x)

def mainModMel1Mix_2(voice):
    voice.asyncScaledNote(0, 4)
    voice.rest(1)
    voice.asyncScaledNote(1, 3)
    voice.rest(1)
    voice.asyncScaledNote(3, 2)
    voice.rest(2)

    voice.scaledChord([1, -1, -3], 4)

    voice.asyncScaledNote(1, 4)
    voice.rest(1)
    voice.asyncScaledNote(0, 3)
    voice.rest(1)
    voice.asyncScaledNote(2, 2)
    voice.rest(2)

    voice.scaledChord([7, 2, 0, -3], 8)

def mainModHar1Mix_2(voice):
    voice.rest(16)
    voice.scaledNote(-3, 8)

        
# Moderate functions.

def introModPerc2_1(voice):
    for _ in range(0,4):
        voice.beat('Mute Triangle', 0)
        voice.beat('Sticks', .75)
        voice.beat('Sticks', .25)
        voice.beat('Sticks', 1)
        voice.beat('Sticks', .5)
        voice.beat('Sticks', .5)

def introModPerc2_Tim2(voice):
    voice.note(20, 3)
    voice.note(20, 3)
    voice.note(20, 1.5)
    voice.note(20, 1.5)
    voice.note(20, 3)

def introModMel2_1(voice):
    voice.scaledNote(0, .5)
    voice.rest(2.5)

    voice.scaledNote(-3, .5)
    voice.rest(2.5)

    voice.scaledNote(-1, .5)
    voice.rest(2)

    voice.scaledNote(-2, .33)
    voice.scaledNote(-1, .33)
    voice.scaledNote(-2, .34)
    voice.rest(.5)
    voice.scaledNote(-4, .5)
    voice.scaledNote(-3, .5)
    voice.rest(1)

def introModHar2_1_Hi(voice):
    arr = [-3, -6]
    for _ in range(0, 4):
        voice.scaledChord(arr, .25)
        voice.rest(.5)
        voice.scaledChord(arr, .25)
        voice.scaledChord(arr, .25)
        voice.rest(.75)
        voice.scaledChord(arr, .25)
        voice.rest(.25)
        voice.scaledChord(arr, .25)
        voice.rest(.25)

def introModHar2_1_Lo(voice):
    arr = [4, 1]
    for _ in range(0, 4):
        voice.scaledChord(arr, .5)
        voice.rest(2.5)

def introModHar2_Tim(voice):
    for _ in range(0, 4):
        voice.note(20, 1)
        voice.note(20, 2)

def introModMel2_2(voice):
    voice.scaledNote(0, 3)
    voice.scaledNote(-3, 3)
    voice.scaledNote(0, 1.5)
    voice.scaledNote(1, 1.5)
    voice.asyncScaledChord([2, -1], 15)
    voice.rest(3)

def introModHar2_2_Lo(voice):
    voice.scaledNote(0, 3)
    voice.scaledNote(-3, 3)
    voice.scaledNote(0, 1.5)
    voice.scaledNote(-3, 1.5)
    voice.asyncScaledNote(-1, 15)
    voice.rest(3)

def introModHar2_3(voice):
    voice.rest(-1)
    voice.scaledNote(0, 1)

    voice.scaledNote(3, 5)

    voice.scaledNote(2, .5)
    voice.scaledNote(1, .5)
    voice.scaledNote(2, 3)

    voice.scaledNote(-1, 3)

def mainModMel2_1(voice):
    voice.scaledNote(0, .5)
    voice.rest(1)
    voice.scaledNote(-3, .5)

    voice.scaledNote(0, .5)
    voice.rest(.5)
    voice.scaledNote(1, .5)
    voice.rest(.5)

    voice.scaledNote(2, .5)
    voice.rest(1)
    voice.scaledNote(4, .25)
    voice.scaledNote(3, .25)

    voice.scaledNote(2, .5)
    voice.rest(.5)
    voice.scaledNote(0, .5)
    voice.rest(.5)

    voice.scaledNote(3, .5)
    voice.rest(1.5)

    voice.scaledNote(2, .5)
    voice.rest(.5)
    voice.scaledNote(1, .5)
    voice.rest(.5)

    voice.scaledNote(0, .5)
    voice.rest(1.5)

def mainModPerc2(voice):
    for _ in range(0, 7):
        voice.beat('Mute Triangle', 0)
        for _2 in range(0,4):
            voice.beat('Sticks', .5)
    for _ in range(0, 2):
        voice.beat('Mute Triangle', 0)
        for _2 in range(0,2):
            voice.beat('Sticks', .5)

def mainModPerc2_Tim(voice):
    for _ in range(0, 7):
        voice.note(20, 2)
    for _ in range(0, 2):
        voice.note(20, 1)

def mainModHar2_1(voice):
    for _ in range(0, 2):
        voice.scaledChord([-7, -9, -11], .5)
        voice.rest(1.5)

    for _ in range(0, 2):
        voice.scaledChord([-3, -5, -7], .5)
        voice.rest(1.5)

    voice.scaledChord([-4, -6, -8], .5)
    voice.rest(1.5)

    voice.scaledChord([-6, -8, -11], .5)
    voice.rest(1.5)

    for _ in range(0, 2):
        voice.scaledChord([-7, -9, -11], 1.6)
        voice.rest(.4)


def mainModMel2_2(voice):
    voice.scaledNote(0, .5)
    voice.rest(1)
    voice.scaledNote(-3, .5)

    voice.scaledNote(0, .5)
    voice.rest(.5)
    voice.scaledNote(1, .5)
    voice.rest(.5)

    voice.scaledNote(2, .5)
    voice.rest(1.5)

    voice.scaledNote(1, .5)
    voice.rest(1)
    voice.scaledNote(0, .5)
    voice.scaledNote(1, .5)

    voice.rest(1)
    voice.scaledNote(2, .25)
    voice.scaledNote(1, .25)
    voice.scaledNote(0, .5)

    voice.rest(.5)
    voice.scaledNote(-1, .5)
    voice.rest(.5)

    voice.scaledChord([-2, -4], 2)
    # This weird stuff is to get the cutoff sound I want.
    voice.rest(-.3)
    voice.slideVolume(100, 0, .3)

    voice.scaledChord([-2, -4], 2)

    voice.rest(.5)

def mainModHar2_2(voice):
    def dummyFunc(scale):
        for _ in range(0, 2):
            voice.scaledChord(scale, .5)
            voice.rest(1.5)

    dummyFunc([0, -2, -4])

    dummyFunc([2, -1, -3])

    dummyFunc([1, -1, -4])

    voice.scaledChord([-2, -4], 4)

def mainModHar2_2_Bk(voice):
    voice.scaledChord([-7, -9, -11], 4)
    voice.scaledChord([-5, -8, -10], 4)
    voice.scaledChord([-6, -8, -11], 4)

    voice.scaledChord([-9, -11], 4)

def mainModMel1_1(voice, voice2):
    # Just yanking mainSlowMel1_1, but keeping separate function for code
    # consistency.
    mainSlowMel1_1(voice)

    voice2.rest(12)
    voice2.slideVolume(60, 100, 2)
    for _ in range(0,2):
        voice2.scaledNote(0, 1.8)
        voice2.rest(.2)

def mainModMel1_2(voice):
    # Just yanking mainSlowMel1_2, but keeping separate function for code
    # consistency.
    mainSlowMel1_2(voice)

def mainModHar1_1(voice1, voice2):
    def dummyFunc(voice, chord):
        voice.scaledChord(chord, .25)
        voice.rest(1.75)
        voice.scaledChord(chord, .25)
        voice.rest(1.75)

    dummyFunc(voice1, [0, -2])
    dummyFunc(voice1, [3, 1])
    dummyFunc(voice1, [2, 0])
    dummyFunc(voice1, [0, -3])

    for x in [0, 3, 2, 0]:
        voice2.scaledNote(x, 4)

def mainModHar1_2(voice1, voice2):
    def dummyFunc(voice, chord):
        voice.scaledChord(chord, .25)
        voice.rest(2.75)
        voice.scaledChord(chord, .25)
        voice.rest(.75)

    dummyFunc(voice1, [0, -2])
    dummyFunc(voice1, [3, 1])
    dummyFunc(voice1, [4, 2])
    
    for _ in range(0, 2):
        voice1.scaledChord([3, 1], .25)
        voice1.rest(1.75)

    for x in [0, 3, 4, 3]:
        voice2.scaledChord([x, x-2], 4)

def mainModPerc1_Tim(voice):
    def dummyFunc():
        voice.note(20, 1)
        voice.note(20, 1)
        voice.rest(1)
        voice.note(20, 1)

    for _ in range(0,4):
        dummyFunc()

def mainModPerc1(voice):
    def dummyFunc():
        voice.beat('Snare Drum 1', .33)
        voice.beat('Snare Drum 2', .33)
        voice.beat('Snare Drum 1', .34)

    for _ in range(0,2):
        dummyFunc()

    voice.rest(1)

    for _ in range(0,3):
        dummyFunc()

    voice.rest(1)

    dummyFunc()

    voice.beat('Snare Drum 1', 1)
    voice.beat('Snare Drum 2', 1)

    voice.rest(1)
    voice.beat('Snare Drum 2', 1)
    voice.beat('Snare Drum 1', 1)
    voice.beat('Snare Drum 2', 1)


# Fast functions.

def mainBkRep(voice, base, offset = -3):
    voice.scaledNote(base, 1)
    for _ in range(0,2):
        voice.scaledNote(base + offset, 1)

def mainBk(voice, run = 1):
    for _ in range(0, 2):
        mainBkRep(voice, 0)

    voice.scaledNote(0, 1)
    voice.scaledNote(-3, 1)
    voice.scaledNote(0, 1)
    voice.scaledNote(1, 1)

    for _ in range(0, 2):
        mainBkRep(voice, 2)

    voice.scaledNote(2, 1)
    voice.scaledNote(-1, 1)
    voice.scaledNote(2, 1)
    voice.scaledNote(3, 1)

    for _ in range(0, 2):
        mainBkRep(voice, 1, -2)

    voice.scaledNote(1, 1)
    voice.scaledNote(-1, 1)
    voice.scaledNote(2, 1)
    voice.scaledNote(1, 1)

    voice.scaledNote(0, 1)
    voice.scaledNote(-1, 1)

    if (run == 1):
        for _ in range(0, 2):
            mainBkRep(voice, -2, -2)

        voice.scaledNote(-4, 1)
        voice.scaledNote(-3, 1)
        voice.scaledNote(-2, 1)
        voice.scaledNote(-1, 1)
    if (run == 2):
        for _ in range(0,2):
            mainBkRep(voice, 3, -3)

        voice.scaledNote(3, 1)
        voice.scaledNote(2, 1)
        voice.scaledNote(1, 1)
        voice.scaledNote(0, 1)


def mainMel1_1(voice):
    voice.scaledNote(0, 7)
    voice.scaledNote(-1, 1)
    voice.scaledNote(0, 1)
    voice.scaledNote(1, 1)

    voice.scaledNote(2, 3)
    voice.scaledNote(4, 3)
    voice.scaledNote(2, 4)

    voice.scaledChord([3, 1], 8)
    voice.scaledChord([-1, -4], 4)
    voice.rest(4)
    voice.slideVolume(100, 60, 4)
    voice.rest(-4)
    # This is hacky.
    voice.scaledChord([0, -2], 8)

def mainMel1_2(voice):
    voice.scaledNote(0, 7)
    voice.scaledNote(-1, 1)
    voice.scaledNote(0, 1)
    voice.scaledNote(1, 1)

    voice.scaledNote(2, 3)
    voice.scaledNote(1, 3)
    voice.scaledNote(0, 4)

    voice.scaledChord([1, -1], 8)
    voice.scaledChord([-1, -4], 4)
    voice.scaledChord([-2, -4], 8)

def mainHarm1_1(voice):
    voice.rest(20)

    voice.slideVolume(60, 100, 6)
    voice.scaledNote(6, 10)
    voice.scaledNote(5, 1)
    voice.scaledNote(4, 1)
    voice.scaledNote(5, 8)

def mainHarm1_2(voice):
    voice.rest(20)

    voice.slideVolume(80, 100, 6)
    voice.scaledNote(1, 8)
    voice.scaledNote(3, 4)
    voice.scaledNote(3, 8)

def mainBkBass(voice, run = 1):
    for _ in range(0,2):
        voice.scaledNote(0, 1)
        voice.rest(2)

    voice.scaledNote(0, 1)
    voice.rest(1)
    voice.scaledNote(1, 1)
    voice.rest(1)

    for _ in range(0,2):
        voice.scaledNote(2, 1)
        voice.rest(2)

    voice.scaledNote(2, 1)
    voice.rest(1)
    voice.scaledNote(3, 1)
    voice.rest(1)

    for _ in range(0,2):
        voice.scaledNote(1, 1)
        voice.rest(2)

    voice.scaledNote(1, 1)
    voice.rest(1)
    voice.scaledNote(2, 1)
    voice.rest(1)
    voice.scaledNote(1, 1)
    voice.rest(1)

    endnote = 0 if run == 1 else 3
    for _ in range(0, 2):
        voice.scaledNote(endnote, 1)
        voice.rest(2)

    for _ in range(0, 2):
        voice.scaledNote(endnote, 1)
        voice.rest(1)
    
def mainBkTim(voice):
    def dummyFunc():
        voice.note(20, 1)
        voice.rest(2)
        voice.note(20, 1)
        voice.rest(2)
        voice.note(20, 1)
        voice.rest(1)
        voice.note(20, 1)
        voice.rest(1)

    for _ in range(0, 3):
        dummyFunc()

    voice.note(20, 1)
    voice.rest(1)

    dummyFunc()

def mainMel2(voice):
    # Pattern is 6, 4, 4, 6, 4, 2, 6
    def dummyFunc(chInp, rep):
        #for _ in range(0, rep):
        #    voice.scaledChord(chInp, .5)
        #    voice.rest(.5)
        voice.scaledChord(chInp, rep)

    dummyFunc([0, -2], 3)
    dummyFunc([4, -3], 3)

    dummyFunc([3, -2], 2)
    dummyFunc([2, -1], 2)

    dummyFunc([1, -2], 4)

    dummyFunc([2, -1], 3)
    dummyFunc([1, -3], 3)

    dummyFunc([0, -2], 4)
    dummyFunc([0, -4], 2)
    dummyFunc([0, -3], 6)

def mainHarm2(voice):
    # This is difficult because of the timechanges in the mainMel2 func.  Some
    # parts are 6/4 and others are 4/4.
    # Pattern is 6, 4, 4, 6, 4, 2, 6
    def dummyFunc6(noteInp):
        # For 6/4 time. 6 beats total.
        for _ in range(0,4):
            voice.slideVolume(100, 80, .33)
            voice.scaledNote(noteInp, .33)
            voice.rest(.33)
        voice.rest(1.36)
        for _ in range(0, 2):
            voice.scaledNote(noteInp, .5)
            voice.rest(.5)

    def dummyFunc4(noteInp):
        # For 4/4 time.  4 beats total.
        for _ in range(0, 2):
            voice.scaledNote(noteInp, .25)
            voice.rest(1.75)

    dummyFunc6(0)
    dummyFunc4(1)
    dummyFunc4(1)

    dummyFunc6(2)
    dummyFunc4(-1)
    dummyFunc6(0)
    voice.rest(2)

def mainBkBass2(voice):
    voice.scaledNote(0, 6)
    voice.scaledNote(1, 8)
    voice.scaledNote(2, 6)
    voice.scaledNote(-1, 4)
    for _ in range(0, 4):
        voice.scaledNote(0, 1)
        voice.rest(1)

def mainTim2(voice):
    for _ in range(0, 7):
        voice.note(20, 4)
    for _ in range(0, 2):
        voice.note(30, 1)
        voice.note(20, 1)

def mainMel2_2(voice):
    # Pattern is 6, 4, 4, 6, 4, 2, 6
    def dummyFunc(chInp, rep):
        voice.scaledChord(chInp, rep)

    dummyFunc([0, -2], 3)
    dummyFunc([4, -3], 3)

    dummyFunc([5, -2], 8)
    for _ in range(0, 2):
        dummyFunc([6, -1], 3)

    dummyFunc([7, 4, 0], 12)

def mainHarm2_2(voice):
    # Pattern is 6, 4, 4, 6, 4, 2, 6
    def dummyFunc6(noteInp):
        # For 6/4 time. 6 beats total.
        for _ in range(0,4):
            voice.slideVolume(100, 80, .33)
            voice.scaledNote(noteInp, .33)
            voice.rest(.33)
        voice.rest(1.36)
        for _ in range(0, 2):
            voice.scaledNote(noteInp, .5)
            voice.rest(.5)

    def dummyFunc4(noteInp):
        # For 4/4 time. 4 beats total.
        for x in [noteInp, noteInp - 1, noteInp - 2]:
            voice.scaledNote(x, 0.665)
            voice.rest(.665)
        voice.rest(.01)

    dummyFunc6(0)
    dummyFunc4(1)
    dummyFunc4(2)
    dummyFunc6(2)

    dummyFunc4(3)
    dummyFunc4(4)
    voice.scaledNote(0, 4)

def mainMel3(voice):
    for _ in range(0, 6):
        voice.scaledNote(0, .5)
        voice.rest(.5)
    voice.scaledNote(0, .5)
    voice.rest(.5)
    voice.scaledNote(-1, .5)
    voice.rest(.5)

    for _ in range(0, 6):
        voice.scaledNote(2, .5)
        voice.rest(.5)

    voice.scaledNote(2, .5)
    voice.rest(.5)
    voice.scaledNote(3, .5)
    voice.rest(.5)

    for _ in range(0, 6):
        voice.scaledNote(1, .5)
        voice.rest(.5)

    voice.scaledNote(2, .5)
    voice.rest(.5)
    voice.scaledNote(1, .5)
    voice.rest(.5)

    for _ in range(0, 3):
        voice.scaledNote(0, .5)
        voice.rest(.5)
        voice.scaledNote(-2, .5)
        voice.rest(.5)
    voice.scaledNote(-3, .5)
    voice.rest(.5)
    voice.scaledNote(-4, .5)
    voice.rest(.5)

def mainMel3_2(voice):
    for _ in range(0, 4):
        voice.scaledNote(0, .5)
        voice.rest(.5)
        voice.scaledNote(-1, .5)
        voice.rest(.5)

    for _ in range(0, 4):
        voice.scaledNote(2, .5)
        voice.rest(.5)
        voice.scaledNote(1, .5)
        voice.rest(.5)

    for _ in range(0, 4):
        voice.scaledNote(1, .5)
        voice.rest(.5)
        voice.scaledNote(0, .5)
        voice.rest(.5)

    for _ in range(0, 2):
        for x in [4, 3, 2, 0]:
            voice.scaledNote(x, .5)
            voice.rest(.5)

def mainTim3(voice):
    for _ in range(0, 4):
        voice.note(20, 3)
        voice.note(18, 1)
        voice.note(20, 4)

def mainBkBass3(voice):
    voice.scaledNote(0, 8)
    voice.scaledNote(2, 8)
    voice.scaledNote(6, 8)
    voice.scaledNote(5, 8)

def mainHar3(voice):
    for x in [
        0, 2, 4, 2,
        2, 4, 6, 7,
        6, 5, 3, 1
    ]:
        voice.scaledNote(x, 2)

    voice.scaledChord([5, 0], 4)
    voice.scaledChord([4, 0], 3)
    voice.rest(1)

def mainHar3_2(voice):
    for x in [
        0, 2, 4, 2,
        2, 4, 6, 7,
        6, 5, 3, 1,
    ]:
        voice.scaledChord([x, x - 2], 2)
    voice.scaledChord([5, 3], 4)
    voice.scaledChord([2, 0], 4)

def mainHar3_3(voice):
    def dummyFunc(chordInp): # 2 bts
        for _ in range(0, 2):
            voice.scaledChord(chordInp, .5)
            voice.rest(.5)
    voice.rest(-1)
    voice.scaledNote(-1, 1)

    dummyFunc([0, -2])
    dummyFunc([1, -2])
    dummyFunc([2, -1])
    dummyFunc([1, -1])

    # 8/8 bts

    for x in [2, 1, 0, -1]:
        voice.scaledNote(x, 1)
    # 4/12 bts

    dummyFunc([2, 0])
    dummyFunc([3, 0])
    dummyFunc([4, 1])
    dummyFunc([3, 1])

    # 8/20 bts

    for x in [4, 3, 2, 1]:
        voice.scaledNote(x, 1)

    # 4/24 bts

    dummyFunc([2, 0])
    dummyFunc([2, 0])

    dummyFunc([2, -1])
    dummyFunc([2, -1])

    dummyFunc([1, -2])
    dummyFunc([1, -2])

    dummyFunc([0, -2])
    dummyFunc([0, -2])

    # 16/40 bts

    dummyFunc([0, -2])
    dummyFunc([0, -2])

    dummyFunc([0, -3])
    dummyFunc([0, -3])

    # 8/48 bts

def mainBkBass3_3(voice):
    def dummyFunc1(noteInp):
        for _ in range(0, 4):
            voice.scaledNote(noteInp, 1)
            voice.rest(1)

    def dummyFunc2(inp1, inp2):
        for x in [inp1, inp2]:
            voice.scaledNote(x, 1)
            voice.rest(1)

    dummyFunc1(0)
    dummyFunc2(2, 1)

    dummyFunc1(2)
    dummyFunc2(4, 3)

    dummyFunc1(2)
    dummyFunc1(1)
    dummyFunc1(0)

def mainMel3_3(voice):
    def dummyFunc(chordInp):
        for _ in range(0, 2):
            voice.scaledChord(chordInp, 1)
            voice.rest(1)

    for x in [0, 1, 2, 1, 0, -1]:
        voice.scaledNote(x, 2)

    for x in [2, 3, 4, 3, 2, 1]:
        voice.scaledNote(x, 2)

    dummyFunc([2, 0])
    dummyFunc([2, -1])
    dummyFunc([1, -2])
    dummyFunc([0, -2])

    voice.scaledChord([0, -2], 4)
    voice.scaledChord([0, -3], 4)

def mainTim3_3(voice):
    for _ in range(0, 2):
        voice.note(30, .5)
        voice.rest(.5)
        voice.note(20, .5)
        voice.rest(.5)
        voice.note(20, .5)
        voice.rest(.5)

        voice.note(30, 3)
        voice.rest(2)

        voice.note(20, 1)
        voice.rest(1)
        voice.note(20, 1)
        voice.rest(1)

    for _ in range(0, 8):
        voice.note(20, 2)

    voice.note(30, 4)
    voice.note(20, 4)

def mainHarp(voice, run = 1):
    def dummyFunc(base, offset = -3):
        voice.scaledStrum([base + offset - 2, base + offset, base], 1)
        for _ in range(0, 2):
            voice.scaledNote(base + offset, 1)

    voice.asyncScaledStrum([-12, -10, -7], 6)
    for _ in range(0, 2):
        dummyFunc(0)

    for x in [0, -3, 0, 1]:
        voice.scaledNote(x, 1)

    voice.asyncScaledStrum([-10, -8, -5], 6)
    for _ in range(0, 2):
        dummyFunc(2)

    for x in [2, -1, 2, 3]:
        voice.scaledNote(x, 1)

    voice.asyncScaledStrum([-10, -8, -6], 6)
    for _ in range(0, 2):
        dummyFunc(1, -2)

    for x in [1, -1, 2, 1, 0, -1]:
        voice.scaledNote(x, 1)

    if (run == 1):
        voice.asyncScaledStrum([-13, -11, -9], 6)
        for _ in range(0, 2):
            dummyFunc(-2, -2)
        for x in [-4, -3, -2, 1]:
            voice.scaledNote(x, 1)
    if (run == 2):
        voice.asyncScaledStrum([-9, -7, -4], 6)
        for _ in range(0, 2):
            dummyFunc(3, -3)
        for x in [3, 2, 1, 0]:
            voice.scaledNote(x, 1)

def mainFastMel1Mix_2(voice):
    for _ in range(0, 2):
        voice.asyncScaledStrum([-11, -9, -7], 4)
        for x in [-4, -2, 0, -2]:
            voice.scaledNote(x, 1)

    for _ in range(0, 2):
        voice.asyncScaledStrum([-9, -7, -5], 4)
        for x in [-2, 0, 2, 0]:
            voice.scaledNote(x, 1)

    for _ in range(0, 2):
        voice.asyncScaledStrum([-11, -9, -6], 4)
        for x in [1, 0, -2, -4]:
            voice.scaledNote(x, 1)

    for _ in range(0, 2):
        voice.asyncScaledStrum([-12, -11, -9], 4)
        for x in [-2, -3, -2, 0]:
            voice.scaledNote(x, 1)

def mainFastHar1Mix_2(voice):
    voice.rest(4)
    voice.scaledChord([-4, -7], 4)
    voice.rest(4)
    voice.scaledChord([-2, -4], 4)
    voice.rest(4)
    voice.scaledChord([0, -2], 4)
    voice.rest(4)
    for x in [-2, -3, -2, 0]:
        voice.scaledNote(x, 1)

def mainFastMel1Mix(voice):
    for x in [0, 1, 3]:
        voice.scaledNote(x, 8)
    voice.scaledChord([-1, -3], 16)
    for x in [1, 0, 1, 2]:
        voice.scaledNote(x, 8)
    voice.scaledChord([3, 0], 16)

def mainFastBass1Mix(voice):
    for x in [0, 1, -1, -3, -4]:
        voice.scaledNote(x, 8)
    for x in [-1, -2, -3, -5]:
        voice.scaledNote(x, 8)
    voice.scaledNote(-4, 16)

def mainFastHarp1Mix(voice):
    def dummyFunc(startNote):
        voice.asyncScaledStrum([startNote - 11, startNote - 9, startNote - 7], 8)
        for x in range(0, 8):
            voice.scaledNote(startNote - x, 1)

    for x in [0, 1, 3, 4]:
        dummyFunc(x)
    for _ in range(0, 4):
        voice.scaledNote(-4, 1)
        voice.scaledNote(-5, 1)
    for x in [1, 0, 1, 2]:
        dummyFunc(x)
    for _ in range(0, 7):
        voice.asyncScaledStrum([-4, -7], 2)
        voice.scaledNote(3, 1)
        voice.scaledNote(2, 1)
    voice.asyncScaledStrum([-4, -7], 2)
    for _ in range(0, 2):
        voice.scaledNote(3, 1)

def mainFastHar1Mix(voice):
    def dummyFunc(note1, note2):
        for _ in range(0, 4):
            voice.scaledNote(note1, 1)
            voice.scaledNote(note2, 1)

    dummyFunc(0, -2)
    dummyFunc(1, -1)
    dummyFunc(3, -1)
    dummyFunc(4, -1)
    dummyFunc(2, -1)

    dummyFunc(1, -1)
    dummyFunc(0, -3)
    dummyFunc(1, -3)
    dummyFunc(2, -1)
    voice.scaledChord([3, -2], 16)

def mainFastLead1Mix(voice):
    #for x in [0, 1, 3, 1, 0, 1]:
    #    voice.scaledNote(x, 4)
    for x in [0, 1, 3]:
        voice.scaledNote(x, 8)

    for x in [-1, -4]:
        voice.scaledNote(x, 8)
    for x in [1, 2, 1, 0]:
        voice.scaledNote(x, 8)
    voice.scaledNote(-4, 16)

# Script

#comp.stop()#dmz1
comp.setTempo(100)

# Intro
introMel1(violinSol)
introHarm1(stringEns)
stringEns.rest(2)

comp.catchUpAll()
introMel2(violinSol)
introHarm2(stringEns)

stringEns.rest(2)

# Second slow melody (I mixed up the order)

comp.catchUpAll()
mainSlowHar2_1(harp)

comp.catchUpAll()
mainSlowMel2_1(violinSol)
mainSlowHar2_1(harp)

mainSlowMel2_2(violinSol)
mainSlowHar2_2(harp)

# Transition to first slow melody.
stringEns.setVolume(80)
stringEns.catchUp(violinSol.whereAreWe()-4)
stringEns.slideVolume(40, 100, 4)
for _ in range(0,4):
    stringEns.scaledChord([-4, -7], .5)
    stringEns.rest(.5)

# First slow melody.
comp.catchUpAll()
mainSlowMel1_1(violinSol)
mainSlowHar1_1(stringEns, harp)

comp.catchUpAll()
stringEns.setVolume(60)
mainSlowMel1_2(violinSol)
mainSlowHar1_2(stringEns, harp)

# Return to second slow melody.

violinSol.rest(-1)
violinSol.slideVolume(80, 90, 1)
violinSol.scaledNote(-1, 1)

comp.catchUpAll()
cello.setVolume(65)
mainSlowMel2_1(violinSol)
mainSlowHar2_1(harp)
mainSlowHar2_1_Reprise(cello)

comp.catchUpAll()
mainSlowMel2_2(violinSol)
mainSlowHar2_2(harp)
mainSlowHar2_2_Reprise(cello)
mainSlowHar2_2_Reprise_Tim(timpani)

# Transition to mixolydian briefly.

comp.catchUpAll()

harp.rest(-2)
harp.scaledNote(-5, 1)
harp.scaledNote(-4, 1)

stringEns.rest(-4)
for _ in range(0, 4):
    stringEns.scaledChord([-4, -7, -9], .5)
    stringEns.rest(.5)

mainSlowMel1Mix_2(violinSol)
mainSlowHar1Mix_2(stringEns, harp)

comp.catchUpAll()
cello.setVolume(50)
comp.setScale(Voice.MIXOLYDIAN)
mainSlowMel1Mix_1(violinSol)
mainSlowHar1Mix_1(stringEns, harp, cello)

comp.setScale(Voice.DORIAN)


# Transition to moderate speed with perc.

comp.setTempo(180)
comp.catchUpAll()

introModPerc2_1(perc)
stringEns.setVolume(80)

# Speed up, returning to a variation of the intro.

cello.setVolume(127)
violinSol.setVolume(90)
comp.catchUpAll()
introModPerc2_1(perc)
introModMel2_1(violinSol)

comp.catchUpAll()
introModPerc2_1(perc)
introModHar2_1_Lo(cello)
introModHar2_Tim(timpani)
introModHar2_1_Hi(stringEns)

comp.catchUpAll()
introModPerc2_Tim2(timpani)
introModMel2_2(stringEns)
cello.setVolume(70)
introModHar2_2_Lo(cello)

comp.catchUpAll()
introModPerc2_1(perc)
introModHar2_Tim(timpani)
introModHar2_3(violinSol)

comp.catchUpAll()   
for _ in range(0, 6):
    timpani.note(20, .5)

timpani.note(20, 6)

stringEns.setVolume(90)

# Main mel 2
comp.catchUpAll()
mainModMel2_1(violinSol)
mainModPerc2(perc)
mainModPerc2_Tim(timpani)
mainModHar2_1(stringEns)

comp.catchUpAll()
stringEns.setVolume(70)
fHorn.setVolume(80)
mainModMel2_2(violinSol)
mainModPerc2(perc)
mainModPerc2_Tim(timpani)
mainModHar2_2_Bk(stringEns)
mainModHar2_2(fHorn)

# Main mel 1

stringEns.setVolume(80)
fHorn.setVolume(100)

comp.catchUpAll()

perc.rest(-2)
perc.beat('Snare Drum 1', 1)
perc.beat('Snare Drum 2', .5)
perc.beat('Snare Drum 1', .5)

mainModHar1_1(stringEns, cello)
mainModPerc1_Tim(timpani)
mainModPerc1(perc)

comp.catchUpAll()
mainModMel1_1(fHorn, violinSol)
mainModHar1_1(stringEns, cello)
mainModPerc1_Tim(timpani)
mainModPerc1(perc)

stringEns.setVolume(90)
fHorn.setVolume(70)
comp.catchUpAll()
mainModPerc1_Tim(timpani)
mainModMel1_2(violinSol)
mainModHar1_2(stringEns, fHorn)
mainModPerc1(perc)

# Return to main mel 2, but with horn.

fHorn.setVolume(100)

comp.catchUpAll()
mainModMel2_1(fHorn)
mainModPerc2_Alt1(perc)
mainModPerc2_Tim(timpani)
mainModHar2_1(stringEns)

comp.catchUpAll()
mainModMel2_2(fHorn)
mainModPerc1(perc)
mainModPerc2_Tim(timpani)
mainModHar2_1(stringEns)

# Transition to Mixolydian, briefly.

comp.catchUpAll()
cello.setVolume(100)

mainModHar1Mix_1(fHorn)
mainModBass1Mix_1(cello)
mainModPerc1(perc)
mainModPerc2_Tim(timpani)

comp.setScale(Voice.MIXOLYDIAN)

stringEns.setVolume(100)
comp.catchUpAll()
mainModMel1Mix_2(fHorn)
mainModHar1Mix_2(stringEns)

timpani.rest(16)
for _ in range(0, 2):
    timpani.note(22, 2)
    timpani.note(20, 2)


# Start fast part.

comp.setScale(Voice.DORIAN)
timpani.setVolume(127)

comp.setTempo(300)
stringEns.setVolume(100)

comp.catchUpAll()
mainBk(stringEns)
mainBkBass(cello)
mainBkTim(timpani)

fHorn.setVolume(120)
violinSol.setVolume(70)
cello.setVolume(120)

comp.catchUpAll()
mainMel1_1(fHorn)
mainHarm1_1(violinSol)
mainBk(stringEns, 2)
mainBkBass(cello, 2)
mainBkTim(timpani)

comp.catchUpAll()
mainMel1_2(fHorn)
mainHarm1_2(violinSol)
mainBk(stringEns)
mainBkBass(cello)
mainBkTim(timpani)


comp.catchUpAll()
for _ in range(0, 2):
    timpani.note(30, 1)
    timpani.note(20, 1)
    timpani.note(20, 1)
timpani.note(30, 2)

fHorn.setVolume(100)
cello.setVolume(100)

comp.catchUpAll()
mainMel3(stringEns)
mainBkBass3(cello)
mainTim3(timpani)
mainHar3(fHorn)

comp.catchUpAll()
mainMel3_2(stringEns)
mainBkBass3(cello)
mainTim3(timpani)
mainHar3_2(fHorn)

fHorn.setVolume(127)
comp.catchUpAll()
mainMel3_3(stringEns)
mainHar3_3(fHorn)
mainBkBass3_3(cello)
mainTim3_3(timpani)

for _ in range(0, 2):
    timpani.note(30, 1)
    timpani.note(20, 1)
    timpani.note(20, 1)

timpani.note(30, 2)

fHorn.setVolume(120)

comp.catchUpAll()
mainMel2(fHorn)
mainHarm2(stringEns)
mainBkBass2(cello)
mainTim2(timpani)

stringEns.rest(-2)
for _ in range(0, 5):
    stringEns.scaledNote(0, .5)
    stringEns.rest(.5)

timpani.note(30, 2)
timpani.note(30, 2)

comp.catchUpAll()
mainMel2_2(fHorn)
mainHarm2_2(stringEns)
mainBkBass2(cello)
mainTim2(timpani)

violinSol.setVolume(100)
stringEns.setVolume(80)

comp.catchUpAll()
mainMel1_1(violinSol)
mainHarm1_1(stringEns)
mainBk(fHorn, 2)
mainBkBass(cello, 2)
mainBkTim(timpani)

comp.catchUpAll()
mainMel1_2(violinSol)
mainHarm1_2(stringEns)
mainBk(fHorn)
mainBkBass(cello)
mainBkTim(timpani)

comp.catchUpAll()
mainHarp(harp, 1)

violinSol.setVolume(75)
comp.catchUpAll()
mainMel1_1(violinSol)
mainHarp(harp, 2)


# Transition to mixolodian for conclusion.
comp.catchUpAll()
mainFastMel1Mix_2(harp)
mainFastHar1Mix_2(violinSol)

comp.catchUpAll()
fHorn.setVolume(127)
pickup = 4
fHorn.rest(-pickup)
fHorn.slideVolume(40, 100, pickup)
fHorn.scaledNote(-1, pickup)

comp.setScale(Voice.MIXOLYDIAN)

stringEns.setVolume(100)
mainFastMel1Mix(fHorn)
mainFastHarp1Mix(harp)
mainFastHar1Mix(stringEns)
mainFastBass1Mix(cello)
mainFastLead1Mix(violinSol)
for _ in range(0, 9):
    timpani.note(30, 4)
    timpani.note(20, 4)
for _ in range(0, 4):
    timpani.note(30, 2)
    timpani.note(20, 2)

comp.catchUpAll()
cello.setVolume(80)

# Final chord.
stringEns.slideVolume(60, 100, 8)
stringEns.scaledChord([-4, -7, -9], 16)
cello.slideVolume(60, 80, 8)
cello.scaledChord([3, 0, -2], 16)

# End script

filename = 'Output/' + __file__[:-2] + 'mid'
comp.writeToFile(filename)
os.system('fluidsynth -a alsa -g 1.5 ' + SETTING__SOUND_FONT + ' ./' + filename)

