import pretty_midi, mido
from os import listdir
from os.path import isfile, join, isdir

root_path = "E:\Project Stuff\lmd_full"
midi_directory_paths = [join(root_path, midi_directory_name) for midi_directory_name in listdir(root_path) if
                        isdir(join(root_path, midi_directory_name))]
for i in range(1):
    directory = midi_directory_paths[0]
    # for directory in midi_directory_paths:
    print(":->\tDirectory: {}".format(directory))
    for file in [join(directory, midi_file_name) for midi_file_name in listdir(directory) if
                 isfile(join(directory, midi_file_name))]:
        print("\t:->{}".format(file))

# for file in onlyfiles:
#     try:
#         pm = pretty_midi.PrettyMIDI('C:\\Users\\ashwi\\Downloads\\lmd_full\\0\\' + file)
#         for i, key_change in enumerate(pm.key_signature_changes):
#             print('->{}. Key {} starting at time {:.2f}'.format(i + 1, pretty_midi.key_number_to_key_name(
#                 key_change.key_number),
#                                                                 key_change.time))
#     except:
#         print("Improper MIDI File: {}".format('C:\\Users\\ashwi\\Downloads\\lmd_full\\0\\' + file))
