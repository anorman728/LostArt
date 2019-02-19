from midiutil.MidiFile import MIDIFile
from Voice import Voice

class Composition:
    # Private vars
    #   _mf
    #   _voices
    #   _tempo
    #   _marks
    # Todo: Update these vars to match the style of the Voices class.

    def __init__(self, numTracks, tempo):
        self._mf = MIDIFile(numTracks)
        self._voices = []
        self._tempo = tempo
        self._marks = {}

    def buildVoice(self, instrument, name):
        voiceDum = Voice(
            self._mf,
            len(self._voices),
            instrument,
            self._tempo,
            name,
            0, # For now, start all at zero.
        )
        self._voices.append(voiceDum)
        return voiceDum

    def addVoice(self, newVoice):
        # This adds a new voice, but it won't work if it uses a different
        # MIDIFile object.
        self._voices.append(newVoice)

    def adjustPitchOffset(self, newOffset):
        for voice in self._voices:
            voice.adjustPitchOffset(newOffset)

    def setScale(self, scale):
        '''
        Set the scale for every voice in composition.
        '''
        for voice in self._voices:
            voice.setScale(scale)

    def setKey(self, key):
        '''
        Set key for every voice in composition.
        '''
        for voice in self._voices:
            voice.setKey(key)

    def setTempo(self, tempo):
        '''
        Set tempo for every voice in composition at current time.
        '''
        curtime = self._getLastBeat()
        for voice in self._voices:
            voice.setTempo(tempo, curtime)

    def writeToFile(self, filename):
        # First, add a buffer silent note, so player doesn't cut it off
        # prematurely.
        lastBeat = self._getLastBeat()
        self._mf.addNote(
            0, # There will always be a track 0.
            0, # There will always be a channel 0.
            42, # Pitch is irrelevant
            lastBeat + 5, # Buffer of five beats.  Might not be too helpful if tempo is high, so might want to adjust this later.
            1,
            0 # Zero volume
        )
        with open(filename, 'wb') as outf:
            self._mf.writeFile(outf)

    def mark(self, markName, markTime):
        """
        This function is to help "mark" a time.  (This has nothing to do with
        time signatures.)  Once a time has been marked, it cannot be
        overwritten.
        """
        if markName not in self._marks:
            self._marks[markName] = markTime

    def getMark(self, markName):
        '''
        This function gets a time that was previously marked.
        '''
        return self._marks[markName]

    def catchUpAll(self):
        '''
        Catch up all voices to last beat.
        '''
        curtime = self._getLastBeat()
        for voice in self._voices:
            voice.catchUp(curtime)

    def stop(self):
        '''
        Stop moving forward.  See docstring for function of same name in the
        Voice class.
        '''
        for voice in self._voices:
            voice.stop()

    def start(self):
        '''
        Start moving forward, assuming that stop had previously been called.
        '''
        for voice in self._voices:
            voice.start()


    # Helper functions below this line.

    def _getLastBeat(self):
        timedum = 0
        for voice in self._voices:
            if (voice.whereAreWe() > timedum):
                timedum = voice.whereAreWe()
        return timedum
