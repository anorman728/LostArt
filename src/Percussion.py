from Voice import Voice

class Percussion(Voice):
    '''
    This is a class that's similar to the Voice class, but specifically handles
    channel 9, the percussion channel.  (Channel 10 in MIDI docs.)

    (This class technically inherits things like scaledNote methods, but they're
    useless here.)
    '''

    # Conversion array.  Use this for reference.
    CONVERSION_ARR = {
        'High Q'            : 27,
        'Slap'              : 28,
        'Scratch Push'      : 29,
        'Scratch Pull'      : 30,
        'Sticks'            : 31,
        'Square Click'      : 32,
        'Metronome Click'   : 33,
        'Metronome Bell'    : 34,
        'Bass Drum 2'       : 35,
        'Bass Drum 1'       : 36,
        'Side Stick'        : 37,
        'Snare Drum 1'      : 38,
        'Hand Clap'         : 39,
        'Snare Drum 2'      : 40,
        'Low Tom 2'         : 41,
        'Closed Hi-hat'     : 42,
        'Low Tom 1'         : 43,
        'Pedal Hi-hat'      : 44,
        'Mid Tom 2'         : 45,
        'Open Hi-hat'       : 46,
        'Mid Tom 1'         : 47,
        'High Tom 2'        : 48,
        'Crash Cymbal 1'    : 49,
        'High Tom 1'        : 50,
        'Ride Cymbal 1'     : 51,
        'Chinese Cymbal'    : 52,
        'Ride Bell'         : 53,
        'Tambourine'        : 54,
        'Splash Cymbal'     : 55,
        'Cowbell'           : 56,
        'Crash Cymbal 2'    : 57,
        'Vibra Slap'        : 58,
        'Ride Cymbal 2'     : 59,
        'High Bongo'        : 60,
        'Low Bongo'         : 61,
        'Mute High Conga'   : 62,
        'Open High Conga'   : 63,
        'Low Conga'         : 64,
        'High Timbale'      : 65,
        'Low Timbale'       : 66,
        'High Agogo'        : 67,
        'Low Agogo'         : 68,
        'Cabasa'            : 69,
        'Maracas'           : 70,
        'Short Whistle'     : 71,
        'Long Whistle'      : 72,
        'Short Guiro'       : 73,
        'Long Guiro'        : 74,
        'Claves'            : 75,
        'High Wood Block'   : 76,
        'Low Wood Block'    : 77,
        'Mute Cuica'        : 78,
        'Open Cuica'        : 79,
        'Mute Triangle'     : 80,
        'Open Triangle'     : 81,
        'Shaker'            : 82,
        'Jingle Bell'       : 83,
        'Belltree'          : 84,
        'Castanets'         : 85,
        'Mute Surdo'        : 86,
        'Open Surdo'        : 87,
    }

    def __init__(self, mf, tempo, currenttime):
        super(Percussion, self).__init__(
            mf,
            9, # Percussion channel (10 in MIDI docs.)
            1, # Program doesn't matter (I don't think).
            tempo,
            'Percussion',
            currenttime
        )

    def beat(self, instrStr, span):
        '''
        Add a beat, similarly to the note method in the voice class.

        span = How long before next beat starts.

        Span is the amount of rest after the beginning of the beat.  It can be
        zero if want to have two beats at the same time.
        '''
        self.asyncNote(self.CONVERSION_ARR[instrStr], 1)
        # Duration is irrelevant (I think)
        self.rest(span)
