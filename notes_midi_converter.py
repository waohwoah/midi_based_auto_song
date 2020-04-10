
# to get a MIDI_Chord object:
#   1.  import notes_midi_converter
#   2.  notes_midi_converter.get_random_chord([optiona]scale = one_of_the_elements in chord_progression.chord_progressions_dict)
#   3.  each returned MIDI_Chord object has 3 important instance variables for use:
#       notation(string), MIDI_velocity(int) and MIDI_beats_after_last_chord(int)


import chord_progression
import get_midi_note


class MIDI_Chord:
    notation = "Not"
    chords_list = list()
    MIDI_velocity = 0
    MIDI_beats_after_last_chord = 0
    MIDI_chords_list = list()

    def set_parameters(self, notation, strength, wait_duration):
        self.notation = notation.strip()
        self.MIDI_velocity = strength
        self.MIDI_beats_after_last_chord = wait_duration
        self.MIDI_chords_list = get_midi_note.chord_to_midiNotes(notation)
        print("======================")
        print("MIDI Chord Object Properties(updated):")
        print("Notation = {}\nVelocity/Intensity = {}\nBeats Since Last Chord = {}".format(self.notation,
                                                                                           self.MIDI_velocity,
                                                                                           self.MIDI_beats_after_last_chord))
        print("======================")

    # def get_MIDI_note(self):
    #     return self.MIDI_note

    def get_velocity(self):
        return self.MIDI_velocity

    def get_beats_after_last(self):
        return self.MIDI_beats_after_last_chord

    def get_ticks_after_last(self):
        return self.MIDI_beats_after_last_chord * 480


nchord = MIDI_Chord()


def get_random_chord(scale='C major'):
    scale = scale.strip()
    if scale[1] is 'b':
        scale = scale[0].upper() + scale[1] + scale[2:].upper()
    else:
        scale = scale.upper()
    print("Processed Scale is {}".format(scale))
    import sensible_randoms, random
    try:
        note = chord_progression.chord_progressions_dict[scale][sensible_randoms.non_repeated_randoms()] + "4"
    except:
        print("Given scale {} not present in dictionary.\nAvailable scales are:".format(scale,
                                                                                        chord_progression.chord_progressions_dict))
        return None
    nchord.set_parameters(notation=note, strength=random.randint(80, 120),
                          wait_duration=int(pow(2, random.randint(-1, 4))))
    return nchord


for i in range(10):
    print(get_random_chord())
