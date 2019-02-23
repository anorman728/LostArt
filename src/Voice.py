from Note import Note
from ScaledNote import ScaledNote
import math

class Voice:
    '''
    Class describing an individual voice in the composition.
    '''

    # Class constants.

    # Scales are used in scaledNote and autoChord.

    # Major scale.
    MAJOR = [0,2,4,5,7,9,11]

    # Natural minor scale.
    NATURAL_MINOR = [0,2,3,5,7,8,10]

    # Harmonic minor scale.
    HARMONIC_MINOR = [0,2,3,5,7,8,11]

    # Hexatonic blues scale.
    HEXATONIC_BLUES = [0,3,5,6,7,10]

    # Heptatonic blues scale.
    HEPTATONIC_BLUES = [0,2,3,5,6,9,10]


    # Private variables listed below this line.

    # MediaFile object.
    _mf = None

    # Track, defaulting to zero.
    # Note that I don't really understand the difference between tracks and
    # channels at this point.  Will want to look it up on
    # http://homerecordinghub.com/midi-channels.html
    _track = 0

    # Channel.  This is essentially the number identifying the voice in the
    # MediaFile object.   Set in constructor.
    _channel = None

    # Current time.  Set in constructor.
    _currenttime = None

    # Volume.  Set in setVolume function.
    _volume = 100

    # Instrument number.  Set in constructor.
    _instrument = None

    # Tempo.  Set in constructor.
    _tempo = None

    # Name of channel.  I have no idea what this is for, but it's used in the
    # Midi file class.
    _name = None

    # Pitch offset.  Set in adjustPitchOffset, but defaults to zero if not used.
    _pitchoffset = 0

    # Mute.  Defaults to false.
    _mute = False

    # Key.  Defaults to none.  This needs to be set to use scaledNote and
    # autoChord.
    _key = None

    # Scale.  Defaults to self.MAJOR.  Is used in scaledNote and autoChord.
    _scale = MAJOR

    # Stop.  Defaults to false.  See docstrings for stop and start functions.
    _stop = False


    def __init__(self, mf, channel, instrument, tempo, name, currenttime):
        # Note: CHANNEL is the number for the voice.
        self._mf            = mf
        self._channel       = channel
        self._currenttime   = currenttime
        self._instrument    = instrument
        self._tempo         = tempo
        self._name          = name

        # Add track
        mf.addTrackName(
            self._track,
            self._currenttime,
            self._name
        )
        # Add instrument
        mf.addProgramChange(
            self._track,
            self._channel,
            self._currenttime,
            self._instrument - 1 # Subtract one because MidiUtil's array starts at zero, but most Midi docs start at one.
        )
        # Add tempo
        mf.addTempo(self._track,self._currenttime,self._tempo)

    def adjustPitchOffset(self, addOffset):
        '''
        Adjust the pitch.  This function is not a setter, because instead of
        setting the pitch offset to the addffset value, it adds addOffset to the
        existing offset.  This is so the offset will cascade.
        '''
        self._pitchoffset += addOffset

    def note(self, pitch, dur):
        """
        Add a note.
        """
        self.asyncNote(pitch, dur)
        self._increaseTime(dur)

    def chord(self, pitchArr, dur):
        """
        Add multiple notes at once.
        """
        for pitch in pitchArr:
            self.asyncNote(pitch, dur)
        self._increaseTime(dur)

    def asyncNote(self, pitch, dur):
        '''
        Add a note without increasing the current time.
        This also acts as a base to all other functions that add notes.
        '''
        # Return if muted or stopped.
        if self._mute or self._stop:
            return

        # Convert to Note object, if it's not already a Note or a ScaledNote
        # object.
        if type(pitch) == int:
            noteObj = Note(pitch)
        elif type(pitch) == ScaledNote or type(pitch) == Note:
            noteObj = pitch
        else:
            raise ValueError("note must be integer, Note, or ScaledNote object.")

        self._mf.addNote(
            self._track,
            self._channel,
            noteObj.getPitch() + self._pitchoffset,
            self._currenttime,
            dur,
            self._volume + noteObj.getVolumeOffset()
        )

    # Todo: String of single-length notes.

    def rest(self, dur):
        '''
        Tell voice to rest this many beats.
        '''
        # Don't actually add anything.  Just increase the time.
        self._increaseTime(dur)

    def catchUp(self, newtime):
        '''
        Tell voice to rest until this time.
        '''
        if not self._stop:
            if newtime < self._currenttime:
                raise Exception("Attempting to set current time to lower value" \
                + " than current value.")
            self._currenttime = newtime

    def whereAreWe(self):
        '''
        Return the current time/beat of this instrument.

        This function is named in honor of the drummer that sat behind me in
        the high school musical orchestra who kept losing his place and asking
        me "where are we", thereby causing me to lose my concentration and
        lose my place.
        '''
        return self._currenttime

    def mute(self, tf):
        '''
        Mute this instrument
        '''
        self._mute = tf

    def setVolume(self, newVol):
        '''
        Change the volume.  Default volume is 100, but can go as high as 127.
        '''
        self._volume = newVol

    def stop(self):
        '''
        Stop moving forward.  If this is enabled, not only will new notes not be
        added, but time will not increase.  This should be useful for debugging,
        say, if you want to start the song at a certain point.

        (It's not recommended to stop an individual voice.  It makes more sense
        to stop from the composition object.)
        '''
        self._stop = True

    def start(self):
        '''
        Start moving forward (assuming that stop was previously called).
        '''
        self._stop = False


    # Below this comment are functions requiring keys and scales.  Technically,
    # everything can be done using only the functions above this line.  These
    # functions below are just to make actually making music easier.

    def setKey(self, key):
        '''
        Set the "key," which is a little more nuanced than in real music.  The
        key is set by an integer, not a letter like "Key of G."  (For reference,
        60 is middle C.)  The key is then used by scaledNote and autoChord as a
        base.  As such, there IS a difference between running setKey(60) and
        setKey(72), even though 60 and 72 are both C, because 72 is an octave
        higher, so all notes added via scaledNote and autoChord will be an
        octave higher.
        '''
        self._key = key

    def setScale(self, scale):
        '''
        Set the scale, being one of the constants in this class, MAJOR,
        NATURAL_MINOR, HARMONIC_MINOR, HEXATONIC_BLUES, and HEPTATONIC_BLUES.
        This simply takes an array, though, so if you have some more obscure
        scale that you want to use, you can enter a numeric array describing
        that scale.
        '''
        self._scale = scale

    def setTempo(self, tempo, curtime):
        self._tempo = tempo
        self.catchUp(curtime)
        self._mf.addTempo(self._track,curtime,tempo)

    def scaledNote(self, noteInd, dur):
        '''
        Add a note according to the current set key and scale.  The input
        noteInd is the index of the current scale, so scaledNote(5,1) will add
        the fifth note of the current scale for one second.

        Can also enter a list to add a constant.  So, [5,1] would be 5-sharp
        and [5, -1] would be 5-flat.

        setKey needs to be run before anything involving scales can be used.

        It's easy to get confused by this (or at least I got confused by this):
        Scales are mod 7, not mod 8 (except one of the blues scales that's mod
        6).  It's easy to think of them as mod 8 because there are 8 notes
        played in a (non-blues) scale, but only seven of those notes are
        distinct.

        Please note that *scaled notes are affected by pitch offset*!
        '''
        self.asyncScaledNote(noteInd, dur)
        self._increaseTime(dur)

    def scaledChord(self, noteArr, dur):
        '''
        Add a chord based on scaled notes.
        '''
        self.asyncScaledChord(noteArr, dur)
        self._increaseTime(dur)

    def asyncScaledChord(self, noteArr, dur):
        '''
        Add a scaled chord asynchronously.
        '''
        for note in noteArr:
            self.asyncScaledNote(note, dur)

    def autoChord(self, topNote, dur):
        '''
        Add a chord based on the given topNote.

        (See docstring on scaledNote to see details on the params.)

        Todo: Add parameter for inverted chords.
        '''
        self.scaledChord([topNote,topNote-2,topNote-4], dur)

    def asyncScaledNote(self, note, dur):
        '''
        Add a note according to the current key and scale without increasing
        time.

        note can be either an integer for a numeric index of the scale or it
        can be a ScaledNote object.

        (See docstring on scaledNote to see details on the params.)
        '''
        # Convert to ScaledNote object, if it's not already.
        if type(note) == int:
            scaledNoteObj = ScaledNote(note)
        elif type(note) == ScaledNote:
            scaledNoteObj = note
        else:
            raise ValueError("note must be either integer or ScaledNote object.")

        # Add absolute pitch for note.
        pitch = self._getScaledNote(scaledNoteObj.getNote())
        offset = scaledNoteObj.getAcc()
        scaledNoteObj.setPitch(pitch + offset)

        self.asyncNote(scaledNoteObj, dur)

    def scaledChromaticNote(self, note, dur):
        '''
        Add a note using the key as a base, but ignoring the scale.  This allows
        keys that wouldn't be able to be added with regular scaled notes.
        '''
        self.asyncScaledChromaticNote(note, dur)
        self._increaseTime(dur)

    def scaledChromaticChord(self, noteArr, dur):
        '''
        Add multiple scaled notes at once.
        '''
        self.asyncScaledChromaticChord(noteArr, dur)
        self._increaseTime(dur)

    def asyncScaledChromaticNote(self, note, dur):
        '''
        Add a scaled chromatic note without increasing the time.
        '''
        if self._key == None:
            raise Exception("Key must be set to add a scaled note.")
        if not isinstance(note, int):
            raise Exception("Note must be integer.")
        self.asyncNote(self._key + note, dur)

    def asyncScaledChromaticChord(self, noteArr, dur):
        '''
        Add multiple scaled notes at once asynchronously.
        '''
        for note in noteArr:
            self.asyncScaledChromaticNote(note, dur)


    # Static functions below this line.

    @staticmethod
    def whatKey(noteArr, scale):
        '''
        Find what keys (reduced mod 12) the notes in the noteArr fit into.
        I'm 80% sure this works correctly.
        '''
        returnArr = []

        # Find every key that includes all of the notes in the specified scale.
        for key in range(0,12):
            contained = True # Assume true until disproven.
            for note in noteArr:
                if not Voice.belongsInKey(note, key, scale):
                    contained = False
            if contained:
                returnArr.append(key)

        return returnArr

    @staticmethod
    def likelyKey(noteArr, scale):
        '''
        Since not every melody uses keys that are exclusively in the key
        signature, this takes an array of notes and returns the most likely
        key(s).
        '''

        # Build frequency dictionary
        freqDict = {}
        for key in range(0,12):
            freqDict[key] = 0

        # Throwaway function to make adding to frequency easier.
        def addToFreq(note, key):
            if Voice.belongsInKey(note, key, scale):
                freqDict[key] += 1

        # Throwaway function to make looping through every key easier.
        def loopThroughKeys(note):
            for key in list(freqDict.keys()):
                addToFreq(note, key)

        for note in noteArr:
            loopThroughKeys(note)

        # Find the top frequencies.  May return more than one.
        likelyKeys = []
        topKeyFreq = 0
        for key in freqDict:
            if freqDict[key] > topKeyFreq:
                topKeyFreq = freqDict[key]
                likelyKeys = [key]
            elif freqDict[key] == topKeyFreq:
                likelyKeys.append(key)

        return likelyKeys


    @staticmethod
    def belongsInKey(note, key, scale):
        '''
        Return true if the specified note belongs in the specified key.
        I'm 80% sure this works correctly.
        '''
        noteMod = note % 12
        keyArr = [(key + x) for x in scale]
        return noteMod in keyArr


    # Helper functions below this line.

    def _increaseTime(self, dur):
        '''
        Increase time.
        '''
        if not self._stop:
            self._currenttime+=dur

    def _getScaledNote(self, noteInd):
        if self._key == None:
            raise Exception("Key must be set to add a scaled note.")
        scaleLen = len(self._scale)
        octaveOffset = math.floor(noteInd/scaleLen) * 12
        arrInd = noteInd % scaleLen

        return self._key + octaveOffset + self._scale[arrInd]
