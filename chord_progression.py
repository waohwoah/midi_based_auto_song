import get_midi_note

# chord_progressions = dict()

chord_progressions_dict = {'C major': ['C', 'G', 'Am', 'F'], 'D♭ major': ['D♭', 'A♭', 'B♭m', 'G♭'],
                           'D major': ['D', 'A', 'Bm', 'G'],
                           'E♭ major': ['E♭', 'B♭', 'Cm', 'Ab'], 'E major': ['E', 'B', 'C♯m', 'A'],
                           'F major': ['F', 'C', 'Dm', 'B♭'],
                           'F♯ major': ['F♯', 'C♯', 'D♯m', 'B'], 'G major': ['G', 'D', 'Em', 'C'],
                           'A♭ major': ['A♭', 'E♭', 'Fm', 'D♭'],
                           'A major': ['A', 'E', 'F♯m', 'D'], 'B♭ major': ['B♭', 'F', 'Gm', 'E♭'],
                           'B major': ['B', 'F♯', 'G♯m', 'E']}


def input_progressions():
    print("Enter Chord Progressions")
    while True:
        stream = input().strip()
        if stream is 'N' or stream is 'n':
            break
        else:
            try:
                # print("Name = {}\nChord = {}".format(stream.split(': ')[0], stream.split(': ')[1].split('-')))
                chord_progressions_dict[stream.split(': ')[0]] = [chord for chord in stream.split(': ')[1].split('-')]
            except:
                continue

    print("Chord Progressions = {}".format(chord_progressions_dict))


def give_chords(progression, random_chord=False):
    progression = progression.strip()
    midi_chords_list = list()
    if not random_chord:
        for chord in chord_progressions_dict[progression]:
            midi_chords_list.append(get_midi_note.chord_to_midiNotes(chord))
    else:
        import random
        midi_chords_list = [get_midi_note.notation_to_midiNote(note) for note in
                            chord_progressions_dict[progression][random.randint(0, 3)]]
    return midi_chords_list

# input_progressions()
