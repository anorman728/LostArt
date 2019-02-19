# This script is very similar to (but I don't think exactly the same as) a small
# portion of "Dancing Mad", a song by Nobuo Uematsu in Final Fantasy VI.  The
# purpose of the script is to demonstrate changing from a major key to a minor
# key easily.

# Import modules.
import os
import sys

# Import classes from other files.
sys.path.insert(0, './src')
from Composition import Composition
from Voice import Voice # For constants

# Script below.

comp = Composition(2, 160)

rightHand = comp.buildVoice(1, 'Right Hand')
# Right hand of the keyboard.  I never build a left hand voice.

rightHand.setKey(7+12*4)

def staccatoNote(note, isChromatic = False):
    if isChromatic:
        rightHand.scaledChromaticNote(note,.5)
    else:
        rightHand.scaledNote(note, .5)
    rightHand.rest(.5)

def kefka():
    staccatoNote(0)
    staccatoNote(1)
    staccatoNote(2)
    staccatoNote(3)
    staccatoNote(7, True)
    staccatoNote(2)
    rightHand.scaledNote(5, 1)
    rightHand.scaledNote(4,.5)
    rightHand.scaledNote(3,.5)
    staccatoNote(4)
    staccatoNote(2)
    staccatoNote(1)
    staccatoNote(3)
    staccatoNote(2)
    staccatoNote(0)
    staccatoNote(-1)
    staccatoNote(1)
    rightHand.scaledNote(0,5)
    staccatoNote(-1)
    staccatoNote(-2)
    staccatoNote(-1)
    rightHand.scaledNote(0,5)
    rightHand.rest(2)

rightHand.setScale(Voice.MAJOR)
kefka()
# Notice that we're about to call the exact same function again, but, we've
# changed keys.
rightHand.setScale(Voice.HARMONIC_MINOR)
kefka()
# This one just sounds like garbage.
#rightHand.setScale(Voice.HEXATONIC_BLUES)
#kefka()

filename = 'Output/kefka.mid'
comp.writeToFile(filename)
#os.system('fluidsynth -a alsa -g 2 /usr/share/sounds/sf2/FluidR3_GM.sf2 ./' + filename)
