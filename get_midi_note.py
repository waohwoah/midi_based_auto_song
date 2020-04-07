notes_order = ['C', 'D', 'E', 'F', 'G', 'A', 'B']


def notation_to_midiNote(note):
    midi_note = 20
    note = note.strip()[:3].upper()
    # print("Note received = {}".format(note))
    if note[1] is 'B':
        note = chr(ord(note[0]) - 1) + '#' + note[2]
    if note[0].isalpha() and note[1] is '#' and int(note[2]) >= 0:
        if note[0] is 'A':
            midi_note += 2
        elif note[0] is 'C':
            midi_note += 5
        elif note[0] is 'D':
            midi_note += 7
        elif note[0] is 'F':
            midi_note += 10
        elif note[0] is 'G':
            midi_note += 12
        else:
            midi_note = -999999
        if note[0] is 'A':
            midi_note += 12 * int(note[2])
        else:
            midi_note += 12 * (int(note[2]) - 1)
    elif note[0].isalpha() and int(note[1]) >= 0:
        if note[0] is 'A':
            midi_note += 1
        elif note[0] is 'B':
            midi_note += 3
        elif note[0] is 'C':
            midi_note += 4
        elif note[0] is 'D':
            midi_note += 6
        elif note[0] is 'E':
            midi_note += 8
        elif note[0] is 'F':
            midi_note += 9
        elif note[0] is 'G':
            midi_note += 11
        else:
            midi_note = -999999

        if note[0] is 'A' or note[0] is 'B':
            midi_note += 12 * int(note[1])
        else:
            midi_note += 12 * (int(note[1]) - 1)
    else:
        midi_note = -999999

    if midi_note > 127:
        print("Midi Tuning Range Exceeded: {}(>127)\nNote Capped to 127/G9".format(midi_note))
        midi_note = 127
    elif midi_note < 21:
        print("Invalid Note Given!: {}".format(note))
        midi_note = -1

    return midi_note


def chord_to_midiNotes(chord):
    from pychord import Chord
    chord = chord[0].upper() + chord[1:]
    if chord[1] is '#':
        chord = chr(ord(chord[0]) + 1) + 'b' + chord[2:]
    octave = int(chord[-1])
    try:
        chord_notes = Chord(chord[:-1])
    except:
        print("Invalid Chord = {}".format(chord))
    # print("Chord {} Notes: {}".format(chord, chord_notes))
    midi_notes = list()
    for i, note in enumerate(chord_notes.components()):
        if notes_order.index(note[0]) < notes_order.index(chord_notes.components()[0][0]) and i is not 0:
            # print("Note = {}".format(note + str(octave + 1)))
            midi_notes.append(notation_to_midiNote(note + str(octave + 1)))
        else:
            # print("Note = {}".format(note + str(octave)))
            midi_notes.append(notation_to_midiNote(note + str(octave)))
    return midi_notes


def trial():
    print("Chord {} MIDI Notes: {}".format('A5', chord_to_midiNotes('A5')))
    print("Chord {} MIDI Notes: {}".format('EM6', chord_to_midiNotes('E6')))
    print("Chord {} MIDI Notes: {}".format('B#m75', chord_to_midiNotes('b#m75')))


# trial()
