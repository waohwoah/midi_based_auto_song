import mido, random, math
from mido import Message, MidiFile, MidiTrack, MetaMessage
import get_midi_note, chord_progression

mid = MidiFile(type=1)

track_list = list()
time_list = list()
for i in range(3):
    track_list.append(MidiTrack())
    time_list.append(0)

for track in track_list:
    track.append(MetaMessage('key_signature', key='F#'))
    track.append(MetaMessage('set_tempo', tempo=mido.bpm2tempo(140)))
    track.append(Message('program_change', program=1, time=0))

for i in range(128):
    for i, track in enumerate(track_list):
        this_note = 60 + random.randint(-21, 21)
        if random.randint(0, 10) % 2 is 0:
            track.append(Message('note_on', note=this_note, velocity=random.randint(50, 100),
                                 time=int(480 / math.pow(2, random.randint(1, 1)))))
        else:
            track.append(
                Message('note_off', note=this_note, velocity=127, time=int(480 / math.pow(2, random.randint(0, 1)))))

for track in track_list:
    track.append(MetaMessage('end_of_track'))
    mid.tracks.append(track)

mid.save('auto_song.mid')
