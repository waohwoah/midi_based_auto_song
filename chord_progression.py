import get_midi_note

chord_progressions = dict()


def input_progressions():
    print("Enter Chord Progressions")
    while True:
        stream = input().strip()
        if stream is 'N':
            break
        else:
            chord_progressions[stream.split(': ')[0]] = [chord for chord in stream.split(': ')[1].split('-')]

    print("Chord Progressions = {}".format(chord_progressions))
