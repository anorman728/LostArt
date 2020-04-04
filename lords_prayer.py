# The Lord's Prayer

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

comp = Composition(2, 60)

violin = comp.buildVoice(41, 'Violin')

violin2 = comp.buildVoice(41, 'Violin 2')
#violin2.setVolume(90)

cello = comp.buildVoice(43, 'Cello')
cello.adjustPitchOffset(-24)
cello.setVolume(90)

viola = comp.buildVoice(42, 'Viola')
viola.adjustPitchOffset(-12)
viola.setVolume(90)

baseKey = 64
comp.setKey(baseKey)

# Functions.

def lead01(voice):
    voice.slideVolume(80, 100, 1)
    voice.scaledNote(0, 1)
    voice.scaledNote(0, 2)
    voice.scaledNote(0, 3)

    voice.rest(1)

    voice.scaledNote(3, 1)
    voice.scaledNote(2, 1)

    voice.scaledNote(1, 1)
    voice.scaledNote(1, 2)

    voice.scaledNote(0, 3)

def lead02(voice):
    voice.rest(1)
    voice.scaledNote(-4, 1)
    voice.scaledNote(-3, 1)
    voice.scaledNote(-2, 1)

    voice.scaledNote(-1, 7)

    voice.scaledNote(-1, 1)
    voice.scaledNote(-2, 8)

def lead03(voice):
    voice.rest(1)
    voice.scaledNote(3, 1)
    voice.scaledNote(2, 1)
    voice.scaledNote(1, 1)

    voice.scaledNote(0, 5)

    voice.scaledNote(5, 1)
    voice.scaledNote(4, 1)
    voice.scaledNote(3, 1)

    voice.scaledNote(2, 2.5)

    voice.rest(1)
    voice.slideVolume(60, 100, .5)
    voice.scaledNote(2, 1)
    voice.scaledNote(3, 6.5)

def lead04(voice):
    voice.rest(1.25)
    voice.slideVolume(60, 100, 1)
    voice.scaledNote(1, .5)
    voice.scaledNote(-1, .5)

    voice.scaledNote(0, 7)

    voice.slideVolume(80, 100, 1)
    voice.scaledNote(-4, 1)
    voice.scaledNote(-3, 3.75)

    voice.scaledNote(-4, 7)

def lead05(voice):
    voice.slideVolume(60, 100, 1)
    voice.scaledNote(-1, 1)
    voice.scaledNote(-2, 1)
    voice.scaledNote(1, 1)

    voice.scaledNote(0, 2)
    voice.scaledNote(-4, 1)

    voice.scaledNote(-1, 2)
    voice.scaledNote(-1, 1)

    voice.scaledNote(-2, 2)
    voice.scaledNote(0, .75)

def lead06(voice):
    voice.scaledNote(0, .25)
    voice.scaledNote(1, 1)

    voice.scaledNote(1, 1)
    voice.scaledNote(1, 1)

    voice.scaledNote(2, 2)

    voice.scaledNote(-1, 1)
    voice.scaledNote(1, 2)

    voice.scaledNote(-2, .33)
    voice.scaledNote(-2, .67)

    voice.scaledNote(-2, .33)
    voice.scaledNote(-2, 1)

    voice.scaledNote(-3, 1.25)

def lead07(voice):
    voice.scaledNote(-3, .66)
    voice.scaledNote(-3, .34)

    voice.scaledNote(-2, .66)
    voice.scaledNote(-2, .34)

    voice.scaledNote(-2, 1)
    voice.scaledNote(-2, 1)
    voice.scaledNote(0, 1)

def lead08(voice):
    voice.scaledNote(-2, 1)
    voice.scaledNote(-2, .66)
    voice.scaledNote(-2, .37)

    voice.scaledNote(-1, 1)
    voice.scaledNote(-1, 1)
    voice.scaledNote(-1, 1)

    voice.scaledNote(1, 1)
    voice.scaledNote(0, 1)
    voice.scaledNote(0, 1.25)

def lead09(voice, run):
    voice.scaledNote(3, 3)
    voice.scaledNote(2, .66)
    voice.scaledNote(3, .34)
    voice.scaledNote(5, 2)

    voice.scaledNote(4, 1.34)
    voice.scaledNote(SC(4, acc=-1), .33)
    voice.scaledNote(4, .33)

    voice.scaledNote(5, 2)

    voice.scaledNote(4, 1.34)
    voice.scaledNote(SC(4, acc=-1), .33)
    voice.scaledNote(4, .33)

    voice.scaledNote(6, 2)
    voice.scaledNote(5, 1)

    if (run == 1):
        voice.scaledNote(4, 1)
        voice.scaledNote(5, 3)
        voice.scaledNote(6, .33)
        voice.scaledNote(5, .33)
        voice.scaledNote(4, 4.34)
    elif (run == 2):
        voice.scaledNote(4, 1.25)
        voice.scaledNote(7, 4)
        voice.scaledNote(3, 4)
        voice.rest(2)

def lead10(voice):
    voice.slideVolume(60, 100, 2)
    voice.scaledNote(4, 4)
    voice.scaledNote(3, 13)

# Harmony

def harm01(voice1, voice2):
    voice1.slideVolume(60, 100, 2)
    voice1.scaledNote(0, 6)
    voice2.rest(6)

    voice1.scaledNote(-2, 3)
    voice1.scaledNote(-2, 1)
    voice1.scaledNote(1, 2)
    voice1.scaledNote(-3, 3)

    voice2.rest(1)
    voice2.scaledNote(1, 1)
    voice2.scaledNote(0, 1)
    voice2.scaledNote(-2, 1)

    voice2.scaledNote(-1, 2)
    voice2.scaledNote(-3, 3)
    
def harm02(voice1, voice2):
    voice1.rest(5)
    voice2.rest(7)

    voice1.scaledNote(1, 1)
    voice1.scaledNote(3, 6)

    voice2.scaledNote(3, 1)
    voice2.scaledNote(6, 4)

    voice1.scaledNote(0, 4)
    voice1.scaledNote(3, 4)

    voice2.scaledNote(3, 4)
    voice2.scaledNote(0, 4)

def harm03(voice1, voice2):
    voice1.scaledNote(1, 4)

    voice1.scaledNote(-2, 1)
    voice1.scaledNote(0, 3)

    voice1.scaledNote(3, 4)
    voice1.scaledNote(4, 2.5)

    voice2.rest(5)
    voice2.scaledNote(2, 1)
    voice2.scaledNote(3, 1)
    voice2.scaledNote(4, 1)
    voice2.scaledNote(5, 1)

    for x in [3, 2, 1]:
        voice2.scaledNote(x, 1)
    voice2.scaledNote(0, 2.5)

    voice1.rest(5)
    voice2.rest(5)

    voice2.slideVolume(60, 100, .5)
    voice2.scaledNote(1, 1)
    voice2.scaledNote(0, 2.5)

    voice1.slideVolume(60, 100, .5)
    voice1.scaledNote(-1, 1)
    voice1.scaledNote(-4, 2.5)

def harm04(voice1, voice2):
    voice1.rest(2.25 + 2)
    voice2.rest(2.25 + 2)

    voice1.slideVolume(60, 100, 1)
    voice2.slideVolume(60, 100, 1)

    voice1.scaledNote(-4, 2)
    voice2.scaledNote(-2, 2)

    voice1.scaledNote(-2, 3)
    voice2.scaledNote(3, 3)

    voice1.rest(6.75)
    voice2.rest(6.75)

    voice1.scaledNote(1, 2)
    voice1.scaledNote(0, 4)

    voice2.scaledNote(-8, 2)
    voice2.scaledNote(-9, 4)

def harm05intro(voice1, voice2):
    voice1.scaledNote(1, 2)
    voice2.scaledNote(-8, 2)

    voice1.scaledNote(2, 2)
    voice2.scaledNote(-7, 2)

    voice1.scaledNote(3, 4)
    voice2.scaledNote(-7, 4)

def harm05(voice1, voice2):
    voice1.scaledNote(-4, 3)
    voice1.scaledNote(-2, 3)
    voice1.scaledNote(-3, 3)
    voice1.scaledNote(-4, 2)

    voice2.slideVolume(60, 100, 1)
    voice2.scaledNote(-3, 1)
    voice2.scaledNote(-4, 1)
    voice2.scaledNote(-1, 1)

    voice2.scaledNote(-2, 2)
    voice2.scaledNote(-6, 1)

    for x in [-3, -4, -5, -6]:
        voice2.scaledNote(x, .5)
    voice2.scaledNote(-5, 1)

    voice2.scaledNote(-4, 2)
    voice2.scaledNote(-4, .75)

def harm06(voice1, voice2):
    voice1.rest(.25)
    voice1.scaledNote(-6, 1)
    voice1.scaledNote(-5, 1)
    voice1.scaledNote(-4, 1)
    voice1.scaledNote(-2, 2)

    voice1.scaledNote(-5, 1)
    voice1.scaledNote(-3, 1)
    voice1.scaledNote(-1, 1)
    voice1.scaledNote(-2, 2.33)
    voice1.scaledNote(-3, 1.25)

    voice2.scaledNote(-4, .25)
    for _ in range(0, 3):
        voice2.scaledNote(-2, 1)
    voice2.scaledNote(0, 2)

    voice2.scaledNote(-3, 1)
    voice2.scaledNote(-1, 2)

    voice2.scaledNote(SC(-5, acc=1), .33)
    voice2.scaledNote(SC(-5, acc=1), .67)

    voice2.scaledNote(SC(-5, acc=1), .33)
    voice2.scaledNote(SC(-5, acc=1), 1)

    voice2.scaledNote(SC(-5, acc=0), 1.25)

def harm07intro(voice):
    voice.scaledNote(-1, 1)
    voice.scaledNote(1, 1)
    voice.scaledNote(3, 1)
    voice.scaledNote(5, 2.33)
    voice.scaledNote(4, 1.25)

def harm07(voice1, voice2):
    voice1.scaledNote(-3, 1)
    voice1.slideVolume(100, 60, 4)
    voice1.scaledNote(-2, 3)
    voice1.scaledNote(0, 1)

    voice2.scaledNote(-6, .66)
    voice2.scaledNote(-6, .34)

    voice2.scaledNote(-5, .66)
    voice2.scaledNote(-5, .34)

    voice2.scaledNote(-5, 1)
    voice2.scaledNote(-5, 1)

    voice2.scaledNote(-2, 1)

def harm08(voice1, voice2):
    voice1.rest(.5)
    for _ in range(0,3):
        voice1.scaledNote(0, .25)
        voice1.rest(.25)
    voice1.rest(.5)

    for _ in range(0, 4):
        voice1.scaledNote(1, .25)
        voice1.rest(.25)
    voice1.rest(.50)

    voice1.rest(.50)
    for _ in range(0, 4):
        voice1.scaledNote(2, .25)
        voice1.rest(.25)

    voice2.scaledNote(-4, 1)
    voice2.scaledNote(-4, .66)
    voice2.scaledNote(-4, .37)

    voice2.scaledNote(-4, 1)
    voice2.scaledNote(-4, 1)
    voice2.scaledNote(-4, 1)

    voice2.scaledNote(-4, 1)
    voice2.scaledNote(-6, 1)
    #voice2.scaledNote(-6, 1.25)

def harm09_1(voice1, voice2):
    voice1.rest(1)
    voice1.scaledNote(0, 1)
    voice1.scaledNote(3, 3)

    voice1.scaledNote(1, 1)
    voice1.scaledNote(4, 3)

    voice1.scaledNote(1, 1)
    voice1.scaledNote(4, 3)

    voice1.scaledNote(6, 1)
    voice1.scaledNote(5, 1)
    voice1.scaledNote(4, 1)

    voice1.scaledNote(5, 1)
    voice1.scaledNote(4, 1)
    voice1.scaledNote(3, 2)

    voice1.scaledNote(4, 1)
    voice1.scaledNote(3, 1)
    voice1.scaledNote(0, 2)


    voice2.rest(2)

    voice2.scaledNote(0, 4)
    voice2.scaledNote(1, 4)
    voice2.scaledNote(1, 3)

    voice2.scaledNote(4, 1)
    voice2.scaledNote(3, 1)
    voice2.scaledNote(2, 1)

    voice2.scaledNote(3, 1)
    voice2.scaledNote(2, 1)
    voice2.scaledNote(1, 2)

    voice2.scaledNote(2, 1)
    voice2.scaledNote(1, 1)
    voice2.scaledNote(0, 2)

def harm09_2(voice1, voice2):
    voice1.scaledNote(0, 4)
    voice1.scaledNote(3, 2)
    voice1.scaledNote(1, 2)

    voice1.scaledNote(3, 2)
    voice1.scaledNote(4, 2)

    voice1.scaledNote(6, 4)

    voice2.rest(1)
    voice2.scaledNote(7, 1)
    voice2.scaledNote(5, 1)
    voice2.scaledNote(4, 1)

    voice2.rest(1)
    voice2.scaledNote(5, 1)

    voice2.scaledNote(6, 1)
    voice2.scaledNote(8, 1)

    voice2.scaledNote(7, 1)
    voice2.scaledNote(10, 1)
    voice2.scaledNote(8, 1)
    voice2.scaledNote(6, 1)

    voice2.scaledNote(8, 2)
    voice2.scaledNote(7, 1)
    voice2.scaledNote(6, 1.25)
    voice2.rest(6)

    voice1.catchUp(voice2.whereAreWe())

    voice1.slideVolume(60, 100, 2)
    voice2.slideVolume(60, 100, 2)

    voice2.scaledNote(-2, 2)
    voice1.scaledNote(0, 2)

def harm10(voice1, voice2):
    voice1.rest(8)
    voice2.rest(8)

    voice1.slideVolume(60, 100, 2)
    voice2.slideVolume(60, 100, 2)

    voice1.scaledNote(-1, 2)
    voice2.scaledNote(1, 2)

    voice1.scaledNote(1, 2)
    voice2.scaledNote(-1, 2)

    voice1.scaledNote(2, 2)
    voice2.scaledNote(0, 2)

    voice1.scaledNote(3, 3)
    voice2.scaledNote(-2, 3)
    

# Bass

def bass02(voice):
    voice.scaledNote(-4, 4)
    voice.scaledNote(-1, 8)
    voice.scaledNote(-2, 8)


def bass03(voice):
    voice.scaledNote(1, 4)
    voice.scaledNote(0, 5)
    voice.scaledNote(-2, 3)
    voice.scaledNote(0, 2.5)

    voice.rest(5)

    voice.slideVolume(60, 100, .5)
    voice.scaledNote(1, 1)
    voice.scaledNote(3, 2.5)

def bass04(voice):
    voice.rest(2.25+2)
    voice.slideVolume(60, 100, 1)
    voice.scaledNote(-4, 2)
    voice.scaledNote(3, 3)

    voice.rest(8.75)
    voice.scaledNote(-4, 4)

def bass05intro(voice):
    voice.scaledNote(1, 1)
    voice.scaledNote(-1, 1)
    voice.scaledNote(2, 1)
    voice.scaledNote(4, 1)

    voice.scaledNote(3, 4)

def bass05(voice):
    voice.scaledNote(-4, 3)
    voice.scaledNote(0,  3)
    voice.scaledNote(-1, 3)
    voice.scaledNote(-2, 2)

def bass06(voice):
    voice.rest(.25)
    for _ in range(0, 3):
        voice.scaledNote(1, 1)
    voice.scaledNote(0, 1)
    voice.scaledNote(-1, 1)
    voice.scaledNote(-2, 1)

    voice.scaledNote(-1, 2)

    voice.scaledNote(-2, 2.33)
    voice.scaledNote(-3, 1.25)

def bass07intro(voice):
    voice.scaledNote(-1, 1)
    voice.scaledNote(1, 2)

    voice.scaledNote(-2, .33)
    voice.scaledNote(-2, .67)

    voice.scaledNote(-2, .33)
    voice.scaledNote(-2, 1)

    voice.scaledNote(-3, 1.25)

def bass07(voice):
    voice.scaledNote(3, 1)
    voice.scaledNote(2, 3)
    voice.scaledNote(0, 1)

def bass08(voice):
    voice.scaledNote(0, 2)
    voice.scaledNote(1, 3)
    voice.scaledNote(2, 3.25)

def bass09(voice, run = 1):
    voice.scaledNote(3, 4)

    voice.scaledNote(5, 2)
    voice.scaledNote(4, 2)

    voice.scaledNote(5, 2)
    voice.scaledNote(4, 2)

    voice.scaledNote(6, 4 if run == 1 else 4.25)

    if run == 1:
        voice.scaledNote(5, 4)

        voice.scaledNote(0, 4)
        voice.asyncScaledNote(0, 1)
    else:
        voice.rest(6)
        voice.slideVolume(60, 100, 2)
        voice.scaledNote(0, 2)

def bass10(voice):
    voice.rest(8)
    voice.slideVolume(60, 100, 2)
    voice.scaledNote(-1, 2)
    voice.scaledNote(1, 2)
    voice.scaledNote(2, 2)
    voice.scaledNote(3, 3)



altscale = [0,2,4,5,8,9,11]
altscale2 = [0,2,4,5,7,9,10,11]
# Script.

comp.setScale(Voice.MIXOLYDIAN)

#comp.stop()#dmz1

# Our Father, which art in heaven.
lead01(violin)
harm01(viola, violin2)

# Hallowed be Thy name.
comp.catchUpAll()
lead02(violin)
viola.adjustVolume(10)
harm02(viola, violin2)
bass02(cello)
viola.adjustVolume(-10)

# Thy Kingdom come. Thy will be done on earth
comp.catchUpAll()
lead03(violin)
bass03(cello)
harm03(viola, violin2)

# As it is in heaven.
lead04(violin)
harm04(viola, violin2)
bass04(cello)

harm05intro(viola, violin2)
bass05intro(cello)

# Give us this day our daily bread, and
comp.catchUpAll()
violin2.adjustVolume(10)
lead05(violin)
harm05(viola, violin2)
bass05(cello)
violin2.adjustVolume(-10)

comp.setScale(altscale)

# Forgive us our debts, as we forgive out debtors.
comp.catchUpAll()
lead06(violin)
harm06(viola, violin2)
bass06(cello)

cello.adjustVolume(10)
bass07intro(cello)
harm07intro(viola)
cello.adjustVolume(-10)

# And lead us not into tempta...
violin2.adjustVolume(-20)
comp.catchUpAll()
lead07(violin)
harm07(viola, violin2)
bass07(cello)

comp.setScale(altscale2)

# ...tion but deliver us from evil.
comp.catchUpAll()
lead08(violin)
harm08(viola, violin2)
bass08(cello)

comp.setScale(Voice.MIXOLYDIAN)

# For Thine is the kingdom and the power and the glory forever.
comp.catchUpAll()
lead09(violin, 1)
harm09_1(viola, violin2)
bass09(cello)

# For Thine is the kingdom and the power and the glory forever.
violin.scaledNote(0, 1)
viola.scaledNote(0, 1)

comp.catchUpAll()
lead09(violin, 2)
harm09_2(viola, violin2)
bass09(cello, 2)

# Amen
comp.catchUpAll()
lead10(violin)
harm10(viola, violin2)
bass10(cello)


filename = 'Output/' + __file__[:-2] + 'mid'
comp.writeToFile(filename)
os.system('fluidsynth -a alsa -g 1.5 ' + SETTING__SOUND_FONT + ' ./' + filename)
