from Note import Note
import copy

class ScaledNote(Note):
    '''
    This is a class that helps with some knitty-gritty stuff of individual
    scaled notes.  It has all of the properties of the Note class, but lets you
    used scaled notes with accidentals.

    This class is agnostic for which key it's actually in-- It only stores the
    key for the list used by Voice.
    '''

    # Private variables listed below this line.

    # Note (relative pitch, relative to scale)
    _note = None

    # Acc (accidental)
    _acc = None

    def __init__(self, note, acc = 0, vo = 0, tuning = None):
        '''
        The constructor only requires note (the key for the scale list).
        Everything else defaults to 0, except tuning, which defaults to None.
        '''
        self.setPitch(None) # Not relevant for scaled notes-- Voice will find
                            # the actual pitch.
        self.setVolumeOffset(vo)  # Pulled over from Note class.
        self.setTuning(tuning)    # Pulled over from Note class.
        self.setNote(note)
        self.setAcc(acc)

    def setNote(self, note):
        '''
        Note is the relative pitch (relative to scale), as opposed to absolute
        pitch in the Note class.
        '''
        self._note = note

    def getNote(self):
        return self._note

    def setAcc(self, acc):
        '''
        "Acc" is short for "accidental."  It's just a pitch offset, so 1 would
        be a sharp and -1 would be a flat.  You can actually set it to any
        integer, so it can be used for weird things like double-sharps,
        triple-sharps, or anything else.
        '''
        self._acc = acc

    def getAcc(self):
        return self._acc

    def __add__(self, scNote):
        '''
        This function simply adds an SC note to existing one.

        Note: As of now, this does nothing with tuning!
        '''
        returnNote = copy.deepcopy(self)

        if type(scNote) == int:
            returnNote.setNote(self.getNote() + scNote)
        else:
            returnNote.setNote(self.getNote() + scNote.getNote())
            returnNote.setAcc(self.getAcc() + scNote.getAcc())

        return returnNote
