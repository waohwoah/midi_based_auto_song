import mido, random, math
from mido import Message, MidiFile, MidiTrack, MetaMessage
import get_midi_note, chord_progression

mid = MidiFile(type=1)

track_list = list()
time_list = list()
for i in range(1):
    track_list.append(MidiTrack())
    time_list.append(0)

for track in track_list:
    track.append(MetaMessage('key_signature', key='F#'))
    track.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(140)))
    track.append(Message('program_change', program=1, time=0))

for i in range(16):
    for track in track_list:
        if random.randint(0, 100) % 2 is 0:
            chord = chord_progression.give_chords('C major', random_chords=True)
        else:
            chord = chord_progression.give_chords('Ab major', random_chords=True)
        for note in chord:
            track.append(Message('note_on', note=note, velocity=random.randint(50, 100), time=0))
        for i, note in enumerate(chord):
            if i is 0:
                track.append(
                    Message('note_off', note=note, velocity=127, time=int(480 * math.pow(2, random.randint(1, 2)))))
            else:
                track.append(Message('note_off', note=note, velocity=127, time=0))

for track in track_list:
    track.append(MetaMessage('end_of_track'))
    mid.tracks.append(track)

mid.save('auto_chord_song.mid')
