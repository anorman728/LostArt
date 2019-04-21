# "Prelude and Fuguoid"

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

comp = Composition(2, 80)

orgInd = 20
#orgInd = 1 # Piano makes it easier to hear while testing.
organHigh = comp.buildVoice(orgInd, 'Organ High')
organMid = comp.buildVoice(orgInd, 'Organ Mid')
organLow = comp.buildVoice(orgInd, 'Organ Low')

organMid.adjustPitchOffset(-12)
organLow.adjustPitchOffset(-24)

defKey = 68
comp.setKey(defKey)

# Functions

def main(voice, durMult = 1): # 12 * durMult beats.
    voice.scaledNote(0, 1 * durMult)
    voice.scaledNote(1, 1 * durMult)
    voice.scaledNote(2, 1 * durMult)
    voice.scaledNote(0, 1 * durMult)

    for _ in range(0,2):
        voice.scaledNote(3, 1 * durMult)
        voice.scaledNote(2, .5 * durMult)
        voice.scaledNote(1, .5 * durMult)
        voice.scaledNote(2, 1 * durMult)
        voice.scaledNote(0, 1 * durMult)

    voice.scaledNote(-1, 1 * durMult)
    voice.scaledNote(1, 1 * durMult)
    voice.scaledNote(0, 1 * durMult)
    voice.rest(1 * durMult)

def main_harm(voice, durMult = 1): # 12 * durMult beats
    voice.scaledChord([0, -2, -4], 1 * durMult)
    voice.scaledChord([-2, -4, -6], 1 * durMult)
    voice.scaledChord([-2, -5, -7], 1 * durMult)
    voice.scaledChord([0, -3, -5], 1 * durMult)

    for _ in range(0, 2):
        voice.scaledChord([1, -1, -3], 1 * durMult)
        voice.scaledChord([2, -1, -3], 1 * durMult)
        voice.scaledChord([2, 0, -2], 1 * durMult)
        voice.scaledChord([1, -2, -4], 1 * durMult)

    voice.scaledNote(1, .5 * durMult)
    voice.scaledNote(0, .5 * durMult)
    voice.scaledNote(-1, .5 * durMult)
    voice.scaledNote(-3, .5 * durMult)
    voice.scaledChord([0, -3, -5], 1 * durMult)

    voice.rest(1 * durMult)

def part01(voice1, voice2):
    part01_v1(voice1)
    part01_v2(voice2)

def part01_v1(voice):
    # First block.
    def dummy():
        voice.scaledNote(0, 1)
        voice.scaledNote(1, 1)
        voice.scaledNote(2, 1)
        voice.scaledNote(4, 1)

    dummy()

    voice.scaledNote(3, 1)
    voice.scaledNote(2, 1)
    voice.scaledNote(1, 1)
    voice.scaledNote(-1, 1)

    dummy()

    voice.scaledNote(SC(4, acc = 1), 1)
    voice.scaledNote(3, 1)
    voice.scaledNote(SC(1, acc=1), 1)
    voice.scaledNote(1, 1)

    # Second block.
    voice.rest(1)
    voice.scaledNote(-4, 1)
    voice.rest(1)
    voice.scaledNote(-6, 1)

    voice.rest(1)
    voice.scaledNote(-5, 1)
    voice.rest(1)
    voice.scaledNote(-8, 1)

    voice.rest(1)
    voice.scaledNote(-5, 1)
    voice.rest(1)
    voice.scaledNote(-4, 1)

    voice.rest(1)
    voice.scaledNote(-5, 1)
    voice.rest(1)
    voice.scaledNote(-9, 1)

    # Third block.
    for x in [0, -1]:
        block3Dum(voice, x)
    voice.rest(8)

    # Fourth block.
    voice.scaledChord([-1, 1, 3], 2)
    voice.scaledChord([-2, 0, 3], 2)

    voice.scaledChord([1, 3, 5], 2)
    voice.scaledChord([0, 2, 5], 2)

    voice.scaledChord([0, 2, 4], 4)
    voice.scaledChord([-6, -4, -1], 4)

def block3Dum(voice, offset):
    voice.scaledNote(offset + 3, .5)
    voice.scaledNote(offset + 2, .5)

    voice.scaledNote(offset + -2, .5)
    voice.scaledNote(offset + -3, .5)

    voice.scaledNote(offset + 2, .5)
    voice.scaledNote(offset + 0, .5)

    voice.scaledNote(offset + 4, .5)
    voice.scaledNote(offset + 3, .5)


def part01_v2(voice):
    # First block
    voice.scaledChord([0, 2, 4], 4)
    voice.scaledChord([3, 5, 7], 4)
    voice.scaledChord([2, 4, 7], 4)
    voice.scaledChord([0, 3, 5], 4)

    # Second block
    voice.scaledNote(0, 1)
    voice.scaledNote(-2, 1)
    voice.scaledNote(1, 1)
    voice.scaledNote(-2, 1)

    voice.scaledNote(2, 1)
    voice.scaledNote(-3, 1)
    voice.scaledNote(1, 1)
    voice.scaledNote(-3, 1)

    voice.scaledNote(2, 1)
    voice.scaledNote(-3, 1)
    voice.scaledNote(3, 1)
    voice.scaledNote(-2, 1)

    voice.scaledNote(2, 1)
    voice.scaledNote(-2, 1)
    voice.scaledNote(1, 1)
    voice.scaledNote(-2, 1)

    # Third block.
    voice.rest(8)
    for x in [-1, -3]:
        block3Dum(voice, x)

    # Fourth block.
    voice.scaledChord([-3, -1, 1], 4)
    voice.scaledChord([-1, 1, 3], 4)
    voice.scaledChord([-2, 0, 2], 4)
    voice.scaledChord([-10, -6, -4], 4)


def transitionToMixolydian(voice, voice2):
    startScale = voice.getScale()

    voice.asyncScaledNote(6, 4)
    voice.rest(1)
    voice.asyncScaledNote(4, 3)
    voice.rest(1)
    voice.scaledNote(8, 2)

    voice.scaledChord([5, 3, 1], 4)
    voice2.catchUp(voice.whereAreWe() - 2)
    voice2.scaledNote(5, 2)

    comp.setScale(Voice.MAJOR)

    voice.scaledChord([5, 2, 0], 4)
    voice2.catchUp(voice.whereAreWe() - 2)
    voice2.scaledNote(5, 2)

    comp.setScale(startScale)

    voice.scaledChord([3, 1, -1], 4)
    voice2.catchUp(voice.whereAreWe() - 2)
    voice2.scaledNote(3, 2)

    voice.scaledChord([4, 2, 0], 4)

    voice2.catchUp(voice.whereAreWe() - 2)
    voice2.scaledNote(4, 2)

def fugue01(voice, coef = 1, con = 0): # 8 beats
    def fugueNote(note):
        voice.scaledNote(con, .25)
        voice.scaledNote(coef*note + con, .25)

    fugueNote(3)
    fugueNote(4)
    fugueNote(5)
    fugueNote(3)

    fugueNote(8)
    fugueNote(7)
    fugueNote(6)
    fugueNote(4)

    fugueNote(7)
    fugueNote(6)
    fugueNote(5)
    fugueNote(3)

    fugueNote(6)
    fugueNote(5)
    fugueNote(4)
    fugueNote(2)

def episode(voice1):
    # This is most certainly not an episode and I'm really screwing with the
    # terminology here.

    def fugueNote(note):
        voice1.scaledNote(0, .25)
        voice1.scaledNote(note, .25)

    for x in [4, 3, 1]:
        fugueNote(x)

    lick = [0, 3, 4, 2, 1, 0]
    for x in lick:
        fugueNote(x)

    for _ in range(0,4):
        voice1.scaledChord([-2, 0, 2], .4)
        voice1.rest(.1)
        for _ in range(0,2):
            voice1.scaledChord([-2, 0, 2], .2)
            voice1.rest(.05)
    voice1.scaledChord([-2, 0, 2], 2)

    for x in lick:
        voice1.scaledNote(x, .75)
    voice1.scaledChord([-2, 0, 2], 4)
    voice1.scaledChord([-3, 0, 2], 2)
    voice1.scaledChord([-3, -1, 2], 2)
    voice1.scaledChord([-1, 1, 4], 2)
    voice1.scaledChord([-1, 1, 3], 2)
    voice1.scaledChord([-2, 0, 3], 4)
    voice1.scaledChord([-3, -1, 2], 4)

    voice1.scaledChord([-3, 0, 3], 4)
    voice1.asyncScaledChord([-2, 1, 4], 4)
    voice1.rest(2)
    voice1.scaledNote(-4, 2)
    voice1.asyncScaledChord([-1, 2, 4], 4)
    voice1.rest(2)
    voice1.scaledNote(-5, 2)
    voice1.asyncScaledChord([-2, 0, 3], 8)
    voice1.rest(4)
    voice1.scaledNote(-4, 4)

    voice1.rest(2)

def fugue01_bk(voice, coef = 1, con = 0):
    def fugueNote(note, dur = 2):
        voice.scaledNote(coef*note + con, dur)
    voice.rest(.25)

    fugueNote(3)
    fugueNote(5)
    fugueNote(0)
    fugueNote(4, 1.75)

def fugue02(voice):
    def dummyFunction(con):
        voice.scaledNote(0 + con, .5)
        voice.scaledNote(1 + con, .5)
        voice.scaledNote(-1 + con, .5)
        voice.scaledNote(-3 + con, .5)
    dummyFunction(0)
    dummyFunction(-1)
    dummyFunction(-2)
    voice.scaledNote(-4, .5)
    voice.scaledNote(-3, .5)
    voice.scaledNote(-2, .5)
    voice.scaledNote(0, .5)

def fugue02_bk(voice):
    for x in [0,-1,1,0]:
        voice.scaledNote(x, 2)

def fugue02_bk2(voice):
    voice.scaledChord([0, -2, -4], 2)
    voice.scaledChord([0, -3, -5], 2)
    voice.scaledChord([1, -1, -3], 2)
    voice.scaledChord([0, -2, -4], 2)

def fugue02_bk3(voice):
    # Admittedly, this is probably the worst code organization I've ever done.
    for x in [8, 7, 9, 10]:
        voice.rest(1)
        voice.scaledNote(x, 1)

def fugue02_final(voice1, voice2):
    voice1.scaledChord([0, -2, -4], 4)
    voice1.scaledChord([0, -3, -5], 4)
    voice1.scaledChord([1, -1, -3], 4)

    voice1.scaledChord([0, -2, -4], 8, bor = Voice.MAJOR)

    voice2.scaledNote(4, 2)
    voice2.scaledNote(2, 2)

    voice2.scaledNote(3, 2)
    voice2.scaledNote(0, 2)

    voice2.scaledNote(1, 2)
    voice2.scaledNote(2, 2)

    voice2.rest(4)
    voice2.scaledChord([0, -2, -4], 4, bor = Voice.MAJOR)


# Begin prelude

comp.setScale(Voice.HARMONIC_MINOR)

main(organMid)
organHigh.catchUp(organMid.whereAreWe())
main(organHigh)
main_harm(organMid)

comp.catchUpAll()
part01(organHigh, organMid)
main(organLow, 4)

for _ in range(0,2):
    organMid.scaledNote(0, 4)

# Transition to Mixolydian.
comp.catchUpAll()
transitionToMixolydian(organMid, organLow)

comp.setScale(Voice.MIXOLYDIAN)
transitionToMixolydian(organMid, organLow)

comp.catchUpAll()
main(organHigh)
main_harm(organMid)


# Begin fugue.

comp.setTempo(120)
organHigh.rest(3.75)
comp.catchUpAll()

modScale = [0,1,4,5,7,8,10]; # 1 3 1 2 1 2
# Phrygian with sharped third.

fugue01(organMid)

for x in [Voice.MIXOLYDIAN, modScale]:
    comp.setScale(x)

    comp.catchUpAll()
    fugue01(organMid)
    fugue01_bk(organLow)

    comp.catchUpAll()
    fugue01(organHigh)
    fugue01_bk(organMid)

    comp.catchUpAll()
    fugue01(organMid, con = -4)
    fugue01_bk(organLow, con = -4)

    comp.catchUpAll()
    fugue01(organHigh, con = -4)
    fugue01_bk(organMid, con = -4)

    comp.catchUpAll()
    fugue01(organMid, con = 1)
    fugue01_bk(organLow, con = 1)

    comp.catchUpAll()
    fugue01(organHigh, con = 1)
    fugue01_bk(organMid, con = 1)

comp.catchUpAll()
episode(organMid)

for key in [defKey, defKey - 2]:
    comp.setKey(key)

    comp.catchUpAll()
    fugue02(organHigh)

    comp.catchUpAll()
    fugue02(organHigh)
    fugue02_bk(organLow)

    comp.catchUpAll()
    fugue02(organHigh)
    fugue02_bk(organLow)
    fugue02_bk2(organMid)

    comp.catchUpAll()
    fugue02(organHigh)
    fugue02_bk3(organLow)
    fugue02_bk2(organMid)

    comp.catchUpAll()
    fugue02_bk3(organLow)
    fugue02_bk2(organMid)

comp.catchUpAll()
fugue02_final(organMid, organHigh)


filename = 'Output/' + __file__[:-2] + 'mid'
comp.writeToFile(filename)
os.system('fluidsynth -a alsa -g 1.5 ' + SETTING__SOUND_FONT + ' ./' + filename)
