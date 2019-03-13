# Sleepy hamlet.

# I'm going to go ahead and version this, but it's really bad.  I'm going to restart a song called "Sleepy Hamlet" from scratch.

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

comp = Composition(2, 110)

guitar = comp.buildVoice(25, 'Guitar')
flute = comp.buildVoice(74, 'Flute')

guitar.adjustPitchOffset(-12)
flute.adjustPitchOffset(12)

guitar.setVolume(80)


comp.setKey(64)

strumSp = .03


# Functions

def guitarChord(voice, chordArr, dur):
    '''
    The top note of the guitar chords really need to be heard more.

    I generally very strongly dislike making functions specifically for one
    voice, but this time it really gets out of a problem.

    (I actually thought of a better way to do this later, but, too late now.)
    '''
    chordArr[-1] = SC(chordArr[-1], vo = 30)
    voice.scaledStrum(chordArr, dur, strumSp)

def intro(voice):
    voice.scaledChord([7, 5], 1)
    voice.scaledChord([5, 3], 2)
    voice.scaledChord([7, 4], 1)
    voice.scaledChord([4, 2], 6)
    #voice.scaledStrum([0, 3, 5, 7], 1, strumSp)
    #voice.scaledStrum([-2, 0, 3, 5], 2, strumSp)
    #voice.scaledStrum([0, 2, 4, 7], 1, strumSp)
    #voice.scaledStrum([-3, 0, 2, 4], 6, strumSp)

def pickup(voice):
    voice.scaledNote(0, 1)
    voice.scaledNote(1, 1)

def part01_01(voice):
    voice.scaledNote(3, 4)

    voice.scaledNote(1, 1)
    voice.scaledNote(0, 1)
    voice.scaledNote(-2, 4)

    voice.scaledNote(-3, 1)
    voice.scaledNote(-2, 1)
    voice.scaledNote(0, 1)
    voice.scaledNote(1, 1)
    voice.scaledNote(0, 2)

    voice.scaledNote(-2, 2)
    voice.scaledNote(0, 2)
    voice.scaledNote(-3, 3)
    voice.rest(1)

def part01_01_bk(voice):
    guitarChord(voice, [-2, 0, 3], 6)
    guitarChord(voice, [-6, -4, -2], 4)
    voice.scaledNote(-5, 1)
    voice.scaledNote(-4, 1)
    guitarChord(voice, [-4, -2, 0], 2)
    guitarChord(voice, [-6, -4, -2], 2)
    guitarChord(voice, [-4, -2, 0], 2)
    guitarChord(voice, [-11, -7, -4], 2)
    guitarChord(voice, [-5, -3, 0], 4)

def part01_02(voice):
    voice.scaledNote(-4, 1)
    voice.scaledNote(-3, 1)
    voice.scaledNote(-2, 1)
    voice.scaledNote(0, 1)

    voice.scaledNote(3,2)
    voice.scaledNote(1,2)
    voice.scaledNote(0,3)
    voice.rest(1)

def part01_02_bk(voice):
    dumList=[-6, -5, -4, -2]
    for x in dumList:
        voice.scaledNote(x, 1)
    guitarChord(voice, [-4, SC(-1, acc=-1), 1], 2)
    guitarChord(voice, [-2, 0, 3], 2)
    guitarChord(voice, [-3, 0, 2], 7) # 2 extra beats here


def part01_03(voice):
    voice.scaledNote(0, 1)
    voice.scaledNote(-2, 1)
    #voice.scaledNote(0, 1)
    voice.scaledNote(0, 5)

def part01_03_bk(voice):
    # Invisible rest, because previous went two beats long.
    guitarChord(voice, [-5, -3, 0], 5)

def part01_04(voice):
    voice.rest(1)
    voice.scaledNote(0, 1)
    voice.scaledNote(1, 1)
    #voice.scaledNote(-2, 1)
    #voice.scaledNote(-3, 1)
    voice.scaledNote(-2, 3)

    voice.scaledNote(-2, 1)
    voice.scaledNote(0, 1)
    voice.scaledNote(-2, 1)
    voice.scaledNote(-3, 4)

def part01_04_bk(voice):
    voice.scaledNote(-2, 1)
    voice.scaledNote(-3, 1)
    voice.scaledStrum([-6, -4, -2], 6, strumSp)
    voice.scaledStrum([-7, -5, -3], 4, strumSp)

def part01(voice1, voice2):
    part01_01(voice1)
    part01_01_bk(voice2)
    part01_02(voice1)
    part01_02_bk(voice2)
    part01_03(voice1)
    part01_03_bk(voice2)
    part01_04(voice1)
    part01_04_bk(voice2)

def part02_intro(voice):
    '''Only use guitar here.'''
    voice.scaledChord([7,5], 1)
    voice.scaledNote(5, 1)
    voice.scaledNote(3, 1)
    voice.scaledNote(5, 1)

    voice.scaledChord([7,4], 1)
    voice.scaledNote(4, 1)
    voice.scaledNote(2, 1)
    voice.scaledNote(4,1)

    voice.scaledStrum([1, 3, 5], 2)
    voice.scaledStrum([3, 5, 7], 2)
    #voice.scaledStrum([6, 4, 1], 6)
    voice.scaledStrum([-1, 1, 4], 6)

def pickup2(voice):
    voice.scaledNote(0, 1)
    voice.scaledNote(0, 1)

def part02(voice1, voice2):
    comp.setScale(Voice.MAJOR)
    part02_01(voice1)
    part02_bk(voice2)
    voice1.rest(1)

    comp.setScale(Voice.HARMONIC_MINOR)
    pickup2(voice1) # Really don't like putting this here, but refactoring would
                    # make it more complicated.
    part02_01(voice1)
    part02_bk(voice2)

    comp.setScale(Voice.MAJOR) # Be sure to reset.

def part02_01(voice, uselownote = False):
    # Left off here.  I'm really struggling to to continue this.
    voice.scaledNote(3, 3)

    voice.scaledNote(3, 1)
    voice.scaledNote(2, 1)
    voice.scaledNote(1, 1)
    voice.scaledNote(2, 3)

    voice.scaledNote(2, 1)
    voice.scaledNote(1, 1)
    voice.scaledNote(0, 1)
    voice.scaledNote(1, 3)

    voice.scaledNote(1, 1)
    voice.scaledNote(0, 1)
    if uselownote:
        voice.scaledNote(-4, 1)
    else:
        voice.scaledNote(-1, 1)
    voice.scaledNote(0, 3)

def part02_bk(voice):
    guitarChord(voice, [-2, 1, 3], 1)
    voice.scaledNote(2,1)
    voice.scaledNote(1,4)

    guitarChord(voice, [-3, 0, 2], 1)
    voice.scaledNote(1,1)
    voice.scaledNote(0,4)

    guitarChord(voice, [-4, -1, 1], 1)
    voice.scaledNote(0, 1)
    voice.scaledNote(-1, 4)

    guitarChord(voice, [-5, -2, 0], 6)

def part03_intro(voice):
    voice.scaledStrum([7, 5], 1)
    voice.scaledStrum([5, 3], 2)
    voice.scaledStrum([7, 4], .5)
    voice.scaledStrum([5], .5)
    voice.scaledStrum([4, 2], 6)

def part03(voice1, voice2):
    part01_01(voice1)    # Borrowed from part 1.
    part01_01_bk(voice2) # Borrowed from part 1.
    part01_02(voice1)    # Borrowed from part 1.
    part01_02_bk(voice2) # Borrowed from part 1.

    # Todo: Something needs to be done here.  The space here is too long.
    voice1.catchUp(voice2.whereAreWe()-3)
    part03_03(voice1)
    part03_03_bk(voice2)

    part03_04(voice1)
    voice2.rest(3)
    part03_outro(guitar)

def part03_03(voice):
    voice.scaledNote(-3, 1)
    voice.scaledNote(-2, 1)
    voice.scaledNote(-4, 1)
    voice.scaledNote(0, 4)

def part03_03_bk(voice):
    # Invisible rest because previous note went long.
    voice.scaledStrum([-7, -5, -3], 5)

def part03_04(voice):
    voice.rest(1)
    voice.scaledNote(0, 1)
    voice.scaledNote(1, 1)
    voice.scaledNote(3, 1)
    voice.scaledNote(3, 8)

def part03_outro(voice):
    '''Only use guitar here.'''
    voice.scaledChord([7,5], 1)
    voice.scaledNote(5, 1)
    voice.scaledNote(3, 1)
    voice.scaledNote(5, 1)

    voice.scaledChord([7,4], 1)
    voice.scaledNote(4, 1)
    voice.scaledNote(2, 1)
    voice.scaledNote(4,1)

    voice.scaledStrum([1, 3, 5], 2)
    voice.scaledStrum([-1, 1, 4], 2)
    voice.scaledStrum([-2, 0, 3], 4)


# Intro
intro(guitar)

# Part 1
flute.catchUp(guitar.whereAreWe()-2)
pickup(flute)
part01(flute, guitar)

# Part 2
guitar.rest(1)
part02_intro(guitar)

flute.catchUp(guitar.whereAreWe()-2)
pickup2(flute)
guitar.catchUp(flute.whereAreWe())
part02(flute, guitar)

# Part 3
part03_intro(guitar)

flute.catchUp(guitar.whereAreWe()-2)
pickup(flute)
part03(flute, guitar)


filename = 'Output/' + __file__[:-2] + 'mid'
comp.writeToFile(filename)
os.system('fluidsynth -a alsa -g 1.5 ' + SETTING__SOUND_FONT + ' ./' + filename)
