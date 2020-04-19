import mido, learn
import numpy as np

learn.create_model()


def get_biggest_track(midi_path):
    mid = mido.MidiFile(midi_path)
    key_count = 0
    key = 0
    for msg in mid:
        if msg.is_meta and msg.type == 'key_signature':
            key = msg.key
            # print("Key = {}".format(key))
            key_count += 1
    if key_count is not 1:
        return None
    max_track_index, max_track_length = max(
        enumerate([len(set([msg.note for msg in track if (msg.type is 'note_on' and msg.time is not 0)])) for
                   track in mid.tracks]), key=lambda x: x[1])
    # print("Biggest Track = {}: {}(Unique Notes = {})".format(max_track_index, mid.tracks[max_track_index].name,
    #                                                          max_track_length))
    return key, [msg for msg in mid.tracks[max_track_index] if msg.type is 'note_on' and msg.time is not 0]


def train_model(midi_path):
    key, track_stream = get_biggest_track(midi_path)
    key = key.upper()
    if track_stream is None:
        print("MIDI file has multiple/no detected keys!\nSkipping to next file...")
    else:
        datablock = []
        for note_msg in track_stream:
            datablock.append([-1, note_msg.note, note_msg.velocity, note_msg.time])
        datablock = np.array(datablock)
        # print("Datablock = {}".format(datablock))
        learn.train(datablock)
        print("Starting point for generation = {}".format(datablock[2]))
        # print("Sample Song of length: {} after latest training:{}".format(100, learn.predict(datablock[2], 100)))


train_model('E:\\Project Stuff\\lmd_full\\0\\0a14c3717b42adbaf474848851b744d0.mid')
