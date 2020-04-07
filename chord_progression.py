import get_midi_note

# chord_progressions = dict()

chord_progressions_dict = {'C MAJOR': ['C', 'G', 'Am', 'F'],
                           'Db MAJOR': ['Db', 'Ab', 'Bbm', 'Gb'],
                           'D MAJOR': ['D', 'A', 'Bm', 'G'],
                           'Eb MAJOR': ['Eb', 'Bb', 'Cm', 'Ab'],
                           'E MAJOR': ['E', 'B', 'C♯m', 'A'],
                           'F MAJOR': ['F', 'C', 'Dm', 'Bb'],
                           'F♯ MAJOR': ['F♯', 'C♯', 'D♯m', 'B'],
                           'G MAJOR': ['G', 'D', 'Em', 'C'],
                           'Ab MAJOR': ['Ab', 'Eb', 'Fm', 'Db'],
                           'A MAJOR': ['A', 'E', 'F♯m', 'D'],
                           'Bb MAJOR': ['Bb', 'F', 'Gm', 'Eb'],
                           'B MAJOR': ['B', 'F♯', 'G♯m', 'E']}


def input_progressions():
    print("Enter Chord Progressions")
    while True:
        stream = input().strip()
        if stream is 'N' or stream is 'n':
            break
        else:
            try:
                # print("Name = {}\nChord = {}".format(stream.split(': ')[0], stream.split(': ')[1].split('-')))
                chord_progressions_dict[stream.split(': ')[0].upper()] = [chord for chord in
                                                                          stream.split(': ')[1].split('-')]
            except:
                continue

    print("Chord Progressions = {}".format(chord_progressions_dict))


def give_chords(progression, random_chords=False):
    progression = progression.strip()
    if progression[1] is 'b':
        progression = progression[0].upper() + progression[1] + progression[2:].upper()
    else:
        progression = progression.upper()
    midi_chords_list = list()
    if not random_chords:
        for chord in chord_progressions_dict[progression]:
            midi_chords_list.append(get_midi_note.chord_to_midiNotes(chord + "4"))
    else:
        import sensible_randoms
        midi_chords_list = get_midi_note.chord_to_midiNotes(
            chord_progressions_dict[progression][sensible_randoms.non_repeated_randoms()] + "4")
    return midi_chords_list

# input_progressions()
