import mido, pretty_midi

sample_midi_path = 'E:\\Project Stuff\\lmd_full\\0\\0a14c3717b42adbaf474848851b744d0.mid'
mid = mido.MidiFile(sample_midi_path)

for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))

pm = pretty_midi.PrettyMIDI(sample_midi_path)
for i, key_change in enumerate(pm.key_signature_changes):
    print(
        '->{}. Key {} starting at time {:.2f}'.format(i + 1, pretty_midi.key_number_to_key_name(key_change.key_number),
                                                      key_change.time))

print("Ticks/Beat = {}".format(mid.ticks_per_beat))

for i, msg in enumerate([msg for msg in mid.tracks[3] if msg.type is 'note_on']):
    print("Note Number = {}:".format(i + 1))
    print("\tNote = {}".format(msg.note))
    print("\tVelocity = {}".format(msg.velocity))
    print("\tBeats since last note = {}".format(msg.time / mid.ticks_per_beat))
