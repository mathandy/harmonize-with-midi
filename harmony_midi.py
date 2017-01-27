
"""Create's a harmony at a fixed diatonic interval for any midi file which does
not contain accidental notes.  If an acidental is encountered, the harmony will
be P8 or -P8."""
TODO DONE WITH EVERYTHING, just need to know how to swap one pitch in a score for another
ask on stackexchange
from music21 import *


KEY = ''
INTERVAL = 3  # can be -7, -6, ..., -1, 1, 2, ..., or 7
FIN = '/Users/Andy/Desktop/old country road chorus.mid'
FOUT = '/Users/Andy/Desktop/old_country_road_chorus_harmony.mid'
FIX_OCTAVE = True  # use to retain the octave 


def sgn(x):
    return cmp(x, 0)

def nzint(interval_):
    """converts a diatonic degree/interval to be a unit with a natural 0.
    I.e. 1, -1 notes become 0; 2, -2 become 1, etc."""
    return sgn(interval_)*(abs(interval_) - 1)

# minor_shift_dict = dict([(1, 9), (2, 1), (3, 3), (4, 5), ()])
# key_notes = [kp.midi % 12 for kp in key.pitches]
# adjusted_naturals = [(n + nz) % 12 for n in key_notes]
# adjusted_naturals = [n if n in key_notes else]
# adjusted accidental = 

def harmonize_pitch(p, interval, key, fix_octave=FIX_OCTAVE):
    """Create's a harmony with pitch `p` with a distance determined by the 
    input diatonic interval, `interval` and key.
    If p is not in the input key, the harmony will
    be P8 or -P8 (match the sign of `interval')."""
    key_notes = [kp.midi % 12 for kp in key.pitches]
    try:
        degree = key_notes.index(p.midi % 12)
    except ValueError:
        return p.transpose(sgn(interval)*12)
    new_degree = degree + nzint(interval)

    if fix_octave:
        octave_adjustment = 0
    else:
        octave_adjustment = nzint(new_degree)//6
    return key.pitchFromDegree(new_degree).transpose(12*octave_adjustment)


# Parse input and user args
score = converter.parse(FIN)
if not KEY:
    try:
        key = score.analyze('key')
    except:
        raise Exception("Havin difficulty determining key.  "
                        "Please specify a key.")
else:
    key = KEY


# Harmonize the score
harmony_score = [[harmonize_pitch(p) for p in part.pitches] for part in pitches]

m = midi.translate.streamToMidiFile(s)
m.open(FOUT)
m.write()
m.close()

