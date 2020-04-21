import mido, learn, model_storage
import numpy as np

model_storage.initialize()


def get_biggest_track(midi_path):
    mid = mido.MidiFile(midi_path)
    key_count = 0
    key = 'NA'
    for msg in mid:
        if msg.is_meta and msg.type == 'key_signature':
            key = msg.key
            key_count += 1
    if key_count is not 1:
        return None
    max_track_index, max_track_length = max(
        enumerate([len(set([msg.note for msg in track if (msg.type is 'note_on' and msg.time is not 0)])) for
                   track in mid.tracks]), key=lambda x: x[1])
    return key, [msg for msg in mid.tracks[max_track_index] if msg.type is 'note_on' and msg.time is not 0]


def train_model(midi_path):
    try:
        key, track_stream = get_biggest_track(midi_path)
    except:
        print("MIDI file has multiple/no detected keys!\nSkipping to next file...")
        return

    key = key.upper()
    encoded_key = 2 * (ord(key[0]) - ord('A'))
    if len(key) > 1:
        if key[1] is 'B':
            encoded_key += 1
            if key[2] is 'M':
                encoded_key = -encoded_key
        elif key[1] is 'M':
            encoded_key = -encoded_key
    print("Key = {}\tEncoded Key = {}".format(key, encoded_key))
    datablock = []
    for note_msg in track_stream:
        datablock.append([encoded_key, note_msg.note, note_msg.velocity,
                          note_msg.time])
    datablock = np.array(datablock)
    learn.train(datablock, reps_per_block=100)
    print("Successfully trained model for MIDI file @ path: {}".format(midi_path))


def predict_from_modeL(start_msg, track_length):
    predicted_track = learn.predict(np.array([start_msg]), track_length)
    print("Sample Song of length: {} after latest training:{}".format(100, predicted_track))


# train_model('0a14c3717b42adbaf474848851b744d0.mid')
predict_from_modeL([4, 65, 100, 4], 100)
