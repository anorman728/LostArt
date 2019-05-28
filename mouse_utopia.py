# Mouse Utopia

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

leadVocal = comp.buildVoice(41, 'Lead Vocal')
leadVocal.adjustPitchOffset(-12)
#leadVocal.setVolume(127)


baseKey = 67
comp.setKey(baseKey)

#modScale = [0,1,3,5,7,8,10]
          # 0 1 2 3 4 5 6

bridgeScale = [0,2,3,5,7,10,11];
#              0 1 2 3 4 5  6

comp.setScale(Voice.DORIAN)

# Ideas for lyrics:
#   Troll under every bridge.
#   Something about keyboard warriors.
#   Man can't feed his family and we've found justice.
#   Something about hit pieces.
#   They don't check the sources.  They won't know we lied.
#   It doesn't matter what you haven't done.  You're guilty by being their son.
#   Ask not for whom the mob roars.  It roars for thee.
#
#
#


# Functions

def counterTheme(voice):
    def dummyFunc():
        voice.scaledNote(0, .5)
        voice.scaledNote(-1, .5)
        voice.scaledNote(0, 3)

        voice.scaledNote(2, 1)
        voice.scaledNote(1, 3)

    dummyFunc()

    voice.scaledNote(1, .5)
    voice.scaledNote(2, .5)
    voice.scaledNote(3, 1)
    voice.scaledNote(0, 1)
    voice.scaledNote(0, 1)

    voice.scaledNote(-1, 1)
    voice.scaledNote(0, 3)

    dummyFunc()

    voice.scaledNote(0, 1)
    voice.scaledNote(0, 3)

def counterThemeBass(voice):
    voice.rest(1)
    for _ in range(0,2):
        for x in [0, 1, 3, 2]:
            voice.scaledNote(x, 4)

def counterThemePerc(voice):
    def beginning():
        perc.beat('Low Tom 1', 1)
        perc.beat('Low Tom 1', 0)
        perc.beat('High Tom 1', 1)

        perc.rest(1)
        perc.beat('Low Tom 1', .5)
        perc.beat('High Tom 1', .5)

        perc.rest(1)
        perc.beat('Bass Drum 1', 0)
        perc.beat('Snare Drum 1', 1)
        perc.beat('Snare Drum 2', 1)

        perc.beat('Bass Drum 2', 0)
        perc.beat('Mid Tom 1', 0)
        perc.beat('Closed Hi-hat', 1)

        perc.rest(1)
        perc.beat('High Tom 1', 1)
        perc.beat('High Tom 2', 1)
        perc.beat('Mid Tom 1', 1)

        perc.rest(1)

    beginning()
    for _ in range(0,2):
        perc.beat('Snare Drum 1', .5)
        perc.beat('Snare Drum 2', .5)
    perc.beat('Mid Tom 1', 0)
    perc.beat('Bass Drum 1', 1)

    beginning()

    perc.beat('High Tom 1', 0)
    perc.beat('Snare Drum 1', 1)
    perc.beat('Snare Drum 2', 1)

    perc.beat('High Tom 2', 0)
    perc.beat('Bass Drum 1', 0)
    perc.beat('Snare Drum 1', 1)
    perc.beat('Bass Drum 2', 0)
    perc.beat('Snare Drum 2', 1)

def counterThemeRhyth(voice):
    def dummyFunc():
        voice.scaledStrum([0, 2, 4, 6], 4)
        voice.scaledStrum([-1, 1, 4, 6], 4)
        voice.scaledStrum([0, 3, 5, 7], 2)
        voice.scaledStrum([0, 2, 4, 6], 2)
        voice.scaledStrum([0, 2, 4, 7], 4)

    voice.rest(1)
    for _ in range(0,2):
        dummyFunc()



def themeLead(voice): # 32 beats
    def dummyFunc(offset):
        voice.scaledNote(0 + offset, 1)
        voice.scaledNote(2 + offset, 2)
        voice.scaledNote(1 + offset, 2)
        voice.scaledNote(-1 + offset, 3)
        # 8 beats

    dummyFunc(0)
    dummyFunc(1)
    dummyFunc(0)
    # 24 beats

    voice.scaledNote(0, 1)
    voice.scaledNote(0, 7)
    # 8 beats

def themeLeadIntro(voice):
    voice.scaledNote(0, 1)
    voice.scaledNote(3, 3)
    voice.scaledNote(0, 1)
    voice.scaledNote(0, 3)

    voice.scaledNote(0, 1)
    voice.scaledNote(6, 3)
    voice.scaledNote(7, 1)
    voice.scaledNote(4, 3)
    
    themeLead(voice)

def themeLeadIntroHarmony(voice):
    voice.scaledNote(0, 1)
    voice.scaledNote(-1, 3)
    voice.scaledNote(0, 1)
    voice.scaledNote(0, 3)

    voice.scaledNote(0, 1)
    voice.scaledNote(3, 3)
    voice.scaledNote(4, 1)
    voice.scaledNote(2, 3)

    counterTheme(voice)

def themeBass(voice):
    def dummyFunc(offset):
        voice.scaledNote(0 + offset, 1)
        for _ in range(0,2):
            voice.scaledNote(-1 + offset, 2)
        voice.scaledNote(-1 + offset, 3)

    dummyFunc(0)
    dummyFunc(1)
    dummyFunc(0)
    voice.scaledNote(0, 1)
    voice.scaledNote(0, 7)

def themeRhythm(voice):
    voice.rest(1)
    voice.scaledStrum([0, 2, 4, 6], 8)
    voice.scaledStrum([0, 2, 4, 7], 8)
    voice.scaledStrum([-1, 1, 4, 6], 8)
    voice.rest(2)
    # 27 beats
    voice.scaledNote(-2, 1)
    voice.scaledNote(-1, 1)
    voice.scaledNote(0, 3)

def themePerc(voice):
    for _ in range(0,14):
        voice.rest(1)
        voice.beat('Closed Hi-hat', 1)
    voice.beat('Mid Tom 1', 1)
    voice.beat('Mid Tom 2', 1)
    voice.beat('Snare Drum 1', .5)
    voice.beat('Snare Drum 2', .5)

    voice.beat('Open Hi-hat', 0)
    voice.beat('Snare Drum 1', .5)
    voice.beat('Snare Drum 2', .5)

    voice.beat('Snare Drum 1', 0)

def verseIntro(leadVoice, rhythmVoice, bassVoice, percVoice):
    counterTheme(leadVoice)
    counterThemeBass(bassVoice)
    counterThemePerc(percVoice)
    counterThemeRhyth(rhythmVoice)

def verse(leadVoice, leadVoice2, rhythmVoice, bassVoice, percVoice):
    rhythmVoice.scaledChord([0, 2], 4)
    rhythmVoice.scaledChord([-1, 1], 4)
    bassVoice.scaledNote(0, 4)
    bassVoice.scaledNote(-1, 4)

    for _ in range(0, 4):
        percVoice.beat('Snare Drum 1', 1)
        percVoice.beat('Snare Drum 2', 1)

    where = percVoice.whereAreWe()
    leadVoice.catchUp(where)
    leadVoice2.catchUp(where)

    verseVocal(leadVoice)
    verseLead(leadVoice2)
    verseRhythm(rhythmVoice)
    verseBass(bassVoice)
    versePerc(percVoice)

def verseVocal(leadVoice):
    def verseDum(offset=0):
        leadVoice.rest(1)
        for _ in range(0,3):
            leadVoice.scaledNote(0+offset, 1)
        leadVoice.scaledNote(1+offset, 2)
        leadVoice.scaledNote(-1+offset, 2)
        leadVoice.scaledNote(0+offset, 3)
        leadVoice.rest(5)
        # 16 beats

    def verseDum2(offset=0):
        leadVoice.rest(1)
        leadVoice.scaledNote(4+offset, 1)
        leadVoice.scaledNote(3+offset, 1)
        leadVoice.scaledNote(2+offset, 1)
        leadVoice.scaledNote(3+offset, 2)
        leadVoice.scaledNote(1+offset, 2)
        # 8 beats

    # 1. Troll under every bridge.
    # 2. Keyboard warriors unite.
    # 3. We're addicted to rage.
    verseDum(0)
    # 1. You're not looking hard enough.
    # 2. They won't know that we lied.
    # 3. We will refuse to see.
    verseDum(2)

    # 1. No time for questions.
    # 2. The hit piece is posted.
    # 3. What lies ahead, no.
    verseDum2(0)
    # 1. We're on the offensive.
    # 2. His life has been ended.
    # 3. Ask not who the mob roars.
    verseDum2(-1)

    # 1. They'll know that we play rough.
    # 2. We've scored one for our side.
    # 3. The mob roars for thee.
    verseDum(0)

def verseLead(voice):
    def dummyFunc(offset):
        voice.scaledNote(0+offset, 4)
        voice.scaledNote(1+offset, 4)
        voice.scaledNote(2+offset, 2)
        voice.scaledNote(1+offset, 2)
        voice.scaledNote(0+offset, 2)
        voice.scaledNote(-1+offset, 2)

    def dummyFunc2(offset):
        for _ in range(0,2):
            voice.scaledNote(2+offset, 1)
            voice.scaledNote(1+offset, 1)
        for _ in range(0,2):
            voice.scaledNote(1+offset, 1)
            voice.scaledNote(-1+offset, 1)

    dummyFunc(0)
    dummyFunc(2)
    dummyFunc2(0)
    dummyFunc2(-1)
    dummyFunc(0)

def verseRhythm(voice):
    def dummyFunc(offset):
        voice.scaledStrum([x+offset for x in [0, 2, 4, 6]], 8)
        voice.scaledStrum([x+offset for x in [-3, 0, 2, 4]], 8)

    def dummyFunc2(offset):
        voice.scaledChord([x+offset for x in [2, 4]], 1)
        voice.scaledNote(3+offset, 1)
        voice.scaledNote(2+offset, 1)
        voice.scaledNote(0+offset, 1)

    dummyFunc(0)
    dummyFunc(2)

    voice.scaledNote(0, 1)
    dummyFunc2(0)
    dummyFunc2(-1)
    dummyFunc2(-1)
    dummyFunc2(-2)

    for x in [-1, 0, 1]:
        voice.scaledNote(x, 1)
    voice.scaledStrum([1, 3, 5, 7], 2)
    voice.scaledStrum([-1, 1, 3, 5], 2)
    voice.scaledStrum([-3, 0, 2, 4], 7)

def verseBass(voice):
    def dummyFunc(offset):
        voice.scaledNote(0+offset, 4)
        voice.scaledNote(3+offset, 4)
        voice.scaledNote(2+offset, 2)
        voice.scaledNote(1+offset, 2)
        voice.scaledNote(0+offset, 4)

    dummyFunc(0)
    dummyFunc(2)

    voice.scaledNote(4, 4)
    voice.scaledNote(1, 4)
    voice.scaledNote(3, 4)
    voice.scaledNote(0, 4)

    dummyFunc(0)

def versePerc(voice):
    def dummyFunc():
        voice.beat('Closed Hi-hat', 0)
        voice.beat('Bass Drum 1', 1.5)
        voice.beat('Bass Drum 2', .5)
        voice.beat('Closed Hi-hat', 0)
        voice.beat('Mid Tom 1', 1)
        voice.beat('Bass Drum 1', 1)

    for _ in range(0,8):
        dummyFunc()

    for _ in range(0,2):
        voice.beat('High Tom 1', 1)
        voice.beat('High Tom 2', 1)

    for _ in range(0,2):
        voice.beat('Mid Tom 1', 1)
        voice.beat('Mid Tom 2', 1)

    for _ in range(0,2):
        voice.beat('Bass Drum 1', 1)
        voice.beat('Bass Drum 2', 1)

    for _ in range(0,2):
        voice.beat('Low Tom 1', 1)
        voice.beat('Low Tom 2', 1)

    for _ in range(0,4):
        dummyFunc()

def chorus(leadVoice, leadVoice2, rhythmVoice, bassVoice, percVoice):
    # We'll lead the fight, they have no right.
    # In this mob's sight, they're the blight.
    for _ in range(0,2):
        percVoice.beat('Snare Drum 1', .5)
        percVoice.beat('Snare Drum 2', .5)
    percVoice.beat('Snare Drum 1', 1)
    percVoice.beat('Snare Drum 2', 1)
    perc.beat('Mid Tom 1', 1)
    perc.beat('Mid Tom 2', 1)
    perc.beat('Mid Tom 1', 1)
    bassVoice.scaledNote(0, 2)
    bassVoice.scaledNote(-1, 2)
    bassVoice.scaledNote(0, 3)
    for x in [-1, 0, 2, 0, -2, 0, 3]:
        rhythmVoice.scaledNote(x, 1)

    where = rhythmVoice.whereAreWe()
    leadVoice.catchUp(where)
    leadVoice2.catchUp(where)
    rhythmVoice.catchUp(where)

    themeLead(leadVoice)
    themeLead(leadVoice2)
    themeRhythm(rhythmVoice)
    themeBass(bassVoice)
    themePerc(percVoice)
    

def bridgeIntro(voice1, voice2, bassVoice, percVoice):
    voice1.scaledChord([0, 2], 4)
    voice1.scaledChord([1, 4], 4)
    voice1.scaledChord([-1, 3], 4)
    voice1.scaledChord([-3, -1], 4)
    voice1.scaledChord([-3, 0], 8)

    voice2.scaledStrum([0, 2, 4, 6], 4)
    voice2.scaledStrum([1, 4, 6, 8], 4)
    voice2.scaledStrum([-1, 3, 6, 8], 4)
    voice2.scaledStrum([-3, -1, 1, 3], 4)
    voice2.scaledStrum([-3, 0, 2, 4], 8)

    bassVoice.scaledNote(0, 8)
    bassVoice.scaledNote(-1, 8)
    bassVoice.scaledNote(-3, 8)

    # This transition was really hard, so the code here is horrible.
    for _ in range(0,5):
        percVoice.beat('Low Tom 1', 1)
        for _ in range(0, 3):
            percVoice.beat('Closed Hi-hat', 1)
    for _ in range(0, 4):
        percVoice.beat('Mid Tom 1', .5)
        percVoice.beat('Mid Tom 2', .5)
    percVoice.beat('High Tom 1', 1)
    percVoice.beat('High Tom 2', 1)
    for _ in range(0,4):
        percVoice.beat('Mid Tom 1', .5)
        percVoice.beat('Mid Tom 2', .5)
    percVoice.beat('Low Tom 1', 1)
    percVoice.rest(5)
    percVoice.beat('Bass Drum 1', 0)
    percVoice.beat('Low Tom 1', 2)
    percVoice.beat('Bass Drum 1', 0)
    percVoice.beat('Low Tom 1', 1)

    bassVoice.rest(4)
    for _ in range(0,2):
        bassVoice.scaledNote(-8, 2)
        bassVoice.scaledNote(-7, 6)
    bassVoice.rest(2)
    bassVoice.scaledNote(-7, 6)
    bassVoice.rest(2)

    percVoice.rest(4)
    for _ in range(0,3):
        percVoice.beat('Bass Drum 2', 0)
        percVoice.beat('Low Tom 2', 1)
        percVoice.beat('Bass Drum 2', 0)
        percVoice.beat('Low Tom 2', 1)
        percVoice.rest(2)


def bridge(voice1, voice2, rhythmVoice, bassVoice, percVoice):
    bridgeVocal01(voice1)
    bridgePerc01(percVoice)
    bridgeRhythm01(rhythmVoice)
    bridgeBass01(bassVoice)

    comp.catchUpAll()
    bridgeLead02(voice2)
    bridgeRhythm02(rhythmVoice)
    bridgePerc02(percVoice)
    bridgeBass02(bassVoice)

    for _ in range(0, 2):
        percVoice.beat('Snare Drum 1', .5)
        percVoice.beat('Snare Drum 2', .5)
    percVoice.beat('Low Tom 1', 0)
    percVoice.beat('Bass Drum 1', 1)
    percVoice.beat('Low Tom 2', 0)
    percVoice.beat('Bass Drum 2', 1)

    comp.catchUpAll()
    bridgeVocal05(voice1)
    bridgeRhythm05(rhythmVoice)
    bridgeBass05(bassVoice)
    bridgePerc05(percVoice)

    comp.catchUpAll()
    comp.setScale(Voice.DORIAN)

    for _ in range(0, 2):
        percVoice.beat('Mid Tom 1', .5)
        percVoice.beat('Mid Tom 2', .5)
    percVoice.beat('Snare Drum 1', 1)
    percVoice.beat('Snare Drum 2', 1)

    comp.catchUpAll()
    bridgeRhythm04(rhythmVoice)
    bridgeBass04(bassVoice)
    bridgeLead04(voice2)
    bridgePerc04(percVoice)

def bridgeVocal01(voice1):
    # Strike down.
    voice1.scaledNote(-4, 1)
    voice1.scaledNote(-3, 2)
    # (3)

    # There can not
    for _ in range(0, 3):
        voice1.scaledNote(-3, 1)
    # (3)

    # Be any dissention.
    voice1.scaledNote(-3, 1)
    for _ in range(0, 3):
        voice1.scaledNote(-1, 1)
    voice1.scaledNote(-2, 1)
    voice1.scaledNote(-4, 1)
    # (6)

    # No grace.
    voice1.scaledNote(-1, 1)
    voice1.scaledNote(0, 2)
    # (3)

    # No mercy.
    for _ in range(0, 3):
        voice1.scaledNote(0, 1)
    # (3)

    # No hope of redemption.
    voice1.scaledNote(0, 1)
    for _ in range(0, 3):
        voice1.scaledNote(2, 1)
    voice1.scaledNote(1, 1)
    voice1.scaledNote(-1, 1)
    # (6)

    # Todo: Lyrics at end of bridge: Bitterness will drive us to victory\Blood moves the wheels of history.

def bridgePerc01(voice):
    def dummyFunc():
        voice.beat('Bass Drum 1', 0)
        voice.beat('Low Tom 1', 1)
        voice.beat('Bass Drum 2', 0)
        voice.beat('Low Tom 1', 1)

    for _ in range(0,2):
        dummyFunc()
        voice.rest(10)

def bridgeRhythm01(voice):
    voice.rest(1)
    voice.scaledChord([-3, -6], 6)
    voice.scaledChord([-1, -4], 3)
    voice.scaledChord([-2, SC(-4, acc=-1)], 3)

    voice.scaledChord([0, -3], 6)
    voice.scaledChord([2, -1], 3)
    voice.scaledChord([1, SC(-1, acc=-1)], 2)

def bridgeBass01(voice):
    voice.scaledNote(-7, 1)
    voice.scaledNote(-3, 9)
    voice.scaledNote(-2, 3)
    voice.scaledNote(0, 9)
    voice.scaledNote(1, 2)

def bridgeRhythm04(voice):
    def dummyFunc(offset):
        listDum = [x-5+offset for x in [-1, -4]]
        voice.scaledChord(listDum, 1)
        voice.scaledChord(listDum, 9)

    dummyFunc(6)
    dummyFunc(6)
    dummyFunc(5)
    dummyFunc(6)

def bridgeBass04(voice):
    def dummyFunc(offset):
        voice.scaledNote(1+offset, .5)
        voice.scaledNote(0+offset, .5)
        voice.scaledNote(1+offset, 9)
    #voice.rest(10)
    dummyFunc(-8)
    dummyFunc(-8)
    dummyFunc(-9)
    dummyFunc(-8)

def bridgeLead04(voice):
    voice.rest(2)
    voice.scaledNote(0, 1)
    voice.scaledNote(2, 1)
    voice.scaledNote(1, 2)
    voice.scaledNote(-1, 1)
    voice.scaledNote(2, 1)
    voice.scaledNote(3, 1)
    voice.scaledNote(4, 2)
    voice.rest(1)
    voice.scaledNote(4, 1)
    voice.scaledNote(3, 1)
    voice.scaledNote(2, 2)
    voice.scaledNote(0, 1)
    voice.scaledNote(1, 1)
    voice.scaledNote(0, 1)
    voice.scaledNote(-1, 2)
    voice.rest(1)
    voice.scaledNote(-3, 1)
    voice.scaledNote(-4, 1)
    voice.scaledNote(-1, 2)
    voice.scaledNote(0, 1)
    voice.scaledNote(0, 1)
    voice.scaledNote(-3, 1)
    voice.scaledNote(-4, 2)
    voice.rest(1)
    voice.scaledNote(1, 1)
    voice.scaledNote(0, 1)
    voice.scaledNote(0, 5)

def bridgePerc04(voice):
    for _ in range(0, 4):
        voice.beat('Mid Tom 1', 0)
        voice.beat('Low Tom 1', 0)
        voice.beat('Bass Drum 1', 1)

        voice.beat('Mid Tom 2', 0)
        voice.beat('Low Tom 2', 0)
        voice.beat('Bass Drum 2', 1)

        voice.rest(8)

def bridgeLead02(voice):
    voice.scaledNote(6, 1)
    voice.scaledNote(7, 2)
    voice.scaledNote(8, .5)
    voice.scaledNote(9, .5)
    voice.scaledNote(7, 2)
    # (6)

    voice.scaledNote(6, .5)
    voice.scaledNote(SC(4, acc=1), .5)
    voice.scaledNote(4, 3)
    # (4)

    voice.setScale(bridgeScale);

    voice.scaledChord([5, 3], 3)

    for _ in range(0,3):
        voice.scaledChord([6, 4], 1)
    for _ in range(0,3):
        voice.scaledChord([7, 4], 1)
    for _ in range(0,2):
        voice.scaledChord([8, 6], 1)
    voice.scaledNote(4, 1)
    voice.scaledChord([9, 7], 2)


def bridgeRhythm02(voice):
    voice.rest(1)
    voice.scaledStrum([0, 2, 4, 7], 6)
    voice.scaledStrum([-3, -1, 1, 4], 3)

    comp.setScale(bridgeScale)
    voice.scaledStrum([-2, 1, 3, 5], 3)
    for x in [6, 4, 1, 7, 4, 1, 8, 6, 4]:
        voice.scaledNote(x, 1)
    voice.asyncScaledStrum([2, 4, 7, 9], 4)

def bridgePerc02(voice):
    voice.rest(1)
    voice.beat('Bass Drum 1', 0)
    voice.beat('Mid Tom 1', 1)
    voice.rest(5)
    voice.beat('Bass Drum 2', 0)
    voice.beat('Mid Tom 2', 1)
    voice.rest(2)
    voice.beat('Bass Drum 1', 0)
    voice.beat('Mid Tom 1', 1)

    voice.rest(2)
    for _ in range(0, 3):
        voice.beat('Low Tom 1', 0)
        for _ in range(0, 3):
            voice.beat('High Tom 2', 1)
    voice.beat('Mid Tom 1', 1)

def bridgeBass02(voice):
    voice.scaledNote(-3, 1)
    voice.scaledNote(0, 6)
    voice.scaledNote(1, 3)
    voice.setScale(bridgeScale)
    voice.scaledNote(-2, 3)
    voice.scaledNote(-1, 3)
    voice.scaledNote(0, 3)
    voice.scaledNote(1, 3)
    voice.asyncScaledNote(2, 4) # Bleeds over into drum transition.

def bridgeRhythm03(voice):
    voice.scaledChord([2, 0], 1)
    voice.scaledChord([1, -2], 2)
    voice.scaledChord([0, -3], 3)

def bridgeBass03(voice):
    voice.scaledNote(0, 1)
    voice.scaledNote(-2, 2)
    voice.scaledNote(-3, 1)
    voice.scaledNote(-7, 2)

def bridgePerc03(voice):
    voice.beat('Bass Drum 1', 1)
    voice.beat('Low Tom 1', 0)
    voice.beat('Bass Drum 2', 1)
    voice.rest(2)
    voice.beat('Low Tom 2', 0)
    voice.beat('Bass Drum 1', 1)

def bridgeLead03(voice):
    volDum = voice._volume
    voice.setVolume(volDum-10)
    voice.scaledNote(0, 1)
    voice.scaledNote(1, 1)
    voice.scaledNote(0, 1)
    voice.scaledNote(-1, 1)
    voice.scaledNote(0, 2)
    voice.setVolume(volDum)

def bridgeVocal05(voice):
    voice.rest(1)

    # The bitterness will drive us to victory.
    voice.scaledNote(0, 1)
    voice.scaledNote(0, .5)
    voice.scaledNote(0, .5)
    for _ in range(0, 5):
        voice.scaledNote(0, 1)
    voice.scaledNote(2, 1.5)
    voice.scaledNote(1, .5)
    voice.scaledNote(1, 2)
    # (11)

    voice.rest(1)

    # And blood turns the wheels of history.
    voice.scaledNote(1, 1)
    for _ in range(0,2):
        for x in [3, 2, 1]:
            voice.scaledNote(x, 1)
    voice.scaledNote(3, 1.5)
    voice.scaledNote(2, .5)
    voice.scaledNote(2, 2)
    # (11)

def bridgeRhythm05(voice):
    def dummyFunc(inputList, reps):
        for _ in range(0, reps):
            voice.scaledChord(inputList, .5)
            voice.scaledChord(inputList, .5)
            voice.scaledChord(inputList, 1)

    voice.scaledNote(-1, 1)

    voice.scaledChord([0, 2], 1)
    dummyFunc([0, 2], 3)
    dummyFunc([1, 3], 2)
    voice.scaledChord([1, 3], 1)

    dummyFunc([1, 4], 3)
    dummyFunc([2, 4], 2)
    voice.scaledChord([2, 4], 1)

def bridgeBass05(voice):
    voice.scaledNote(-1, 1)
    voice.scaledNote(0, 7)
    voice.scaledNote(1, 5)
    voice.scaledNote(1, 7)
    voice.scaledNote(2, 4)

def bridgePerc05(voice):
    def dummyFunc(reps):
        for _ in range(0,reps):
            #voice.beat('Low Tom 1', .5)
            #voice.beat('Low Tom 2', .5)
            voice.rest(1)
            voice.beat('Snare Drum 1', 1)

    def dummyFunc2():
        voice.beat('Mid Tom 1', .5)
        voice.beat('Mid Tom 2', .5)

    voice.beat('Bass Drum 1', 1)
    voice.beat('Bass Drum 2', 1)
    for _ in range(0,2):
        dummyFunc(5);
        dummyFunc2();



# Composition

#comp.stop()#dmz1

# *Almost done*  Todo items:
# > Tweak the bridge again.  (I still don't like the transition into the first vocal part.  But I think it's more the timing than the notes.  Though, I may add rhythm guitar riff.  Don't think so, though.)
# > Slow down the last vocal part of the bridge to hear it more clearly.

# Intro
themeLeadIntro(leadGuitar)
comp.catchUpAll()
counterTheme(rhythmGuitar)
perc.rest(28)

perc.setVolume(127)
perc.beat('Bass Drum 2', 1)
perc.beat('Snare Drum 1', 1)
perc.beat('Bass Drum 2', 1)
perc.beat('Snare Drum 1', 0)
perc.beat('Open Hi-hat', 1)


# Set volume of background instruments here.
#rhythmGuitar.setVolume(80)
#bassGuitar.setVolume(80)
perc.setVolume(110)


# Verse intro.
comp.catchUpAll()

rhythmGuitar.mute(True) # Rhythm is only heard in second verse intro.
verseIntro(leadGuitar, rhythmGuitar, bassGuitar, perc)
rhythmGuitar.mute(False)


# First verse.

comp.catchUpAll()
leadGuitar.mute(True) # Lead guitar is heard only in second and third verse.
verse(leadVocal, leadGuitar, rhythmGuitar, bassGuitar, perc)
leadGuitar.mute(False)


# Chorus
comp.catchUpAll()
chorus(leadVocal, leadGuitar, rhythmGuitar, bassGuitar, perc)


# Second verse intro.

comp.catchUpAll()
verseIntro(leadGuitar, rhythmGuitar, bassGuitar, perc)

# Second verse

comp.catchUpAll()
verse(leadVocal, leadGuitar, rhythmGuitar, bassGuitar, perc)


# Chorus
comp.catchUpAll()
chorus(leadVocal, leadGuitar, rhythmGuitar, bassGuitar, perc)


# Bridge
comp.catchUpAll()
comp.setKey(baseKey+4)
verseIntro(leadGuitar, rhythmGuitar, bassGuitar, perc)

comp.catchUpAll()
bridgeIntro(leadGuitar, rhythmGuitar, bassGuitar, perc)
comp.catchUpAll()
bridge(leadVocal, leadGuitar, rhythmGuitar, bassGuitar, perc)


# Final chorus.
comp.catchUpAll()
chorus(leadVocal, leadGuitar, rhythmGuitar, bassGuitar, perc)

# Third verse.

comp.catchUpAll()
verse(leadVocal, leadGuitar, rhythmGuitar, bassGuitar, perc)


# Ending
comp.catchUpAll()

for _ in range(0,2):
    perc.beat('Bass Drum 1', 1)
    perc.beat('Bass Drum 2', 1)
perc.beat('Bass Drum 1', 3)

comp.catchUpAll()

#themeLeadIntro(leadGuitar)
#themeLeadIntroHarmony(rhythmGuitar)
themeLead(leadGuitar)
counterTheme(rhythmGuitar)

# End script.

filename = 'Output/' + __file__[:-2] + 'mid'
comp.writeToFile(filename)
os.system('fluidsynth -a alsa -g 1.5 ' + SETTING__SOUND_FONT + ' ./' + filename)
