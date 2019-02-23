class Note:
    '''
    This is a class that helps with some knitty-gritty stuff of individual
    notes, like volume change for a single note and tuning, but it's not
    necessary to call this class individually to add a note to a composition or
    individual voice.

    This class serves primarily as a way to store information-- The actual
    effects it will have are done by the Voice class.
    '''

    # Private variables listed below this line.

    # Absolute pitch (absolute as opposed being in a key).
    _pitch = None

    # Volume
    _volumeOffset = None

    # Tuning
    _tuning = None

    def __init__(self, pitch, vo = 0, tuning = None):
        '''
        The constructor only requires pitch.  Everything else defaults to zero
        or None and the Voice class will use whatever is currently set for that
        voice.
        '''
        self.setPitch(pitch)
        self.setVolumeOffset(vo)
        self.setTuning(tuning)

    def setPitch(self, pitch):
        '''
        Set the absolute pitch.  (60 is middle C, for reference.)
        '''
        self._pitch = pitch

    def getPitch(self):
        return self._pitch

    def setVolumeOffset(self, volumeOffset):
        '''
        Offset the volume.  Positive makes it louder, negative makes it quieter.
        '''
        self._volumeOffset = volumeOffset

    def getVolumeOffset(self):
        return self._volumeOffset

    def setTuning(self, tuning):
        '''
        Important: Currently does nothing!
        '''
        self._tuning = tuning

    def getTuning(self):
        return self._tuning
