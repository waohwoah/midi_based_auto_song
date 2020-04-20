import read_midi, model_storage
from os import listdir
from os.path import isfile, join, isdir

root_path = "E:\Project Stuff\lmd_full"
midi_directory_paths = [join(root_path, midi_directory_name) for midi_directory_name in listdir(root_path) if
                        isdir(join(root_path, midi_directory_name))]
files_trained = 0

# for i in range(1):
#     directory = midi_directory_paths[0]
for directory in midi_directory_paths:
    print(":->\tDirectory: {}".format(directory))
    for file in [join(directory, midi_file_name) for midi_file_name in listdir(directory) if
                 isfile(join(directory, midi_file_name))]:
        try:
            print("\t:->{}".format(file))
            read_midi.train_model(file)
            files_trained += 1
            if files_trained % 5 is 0:
                print("Saving model...")
                model_storage.save()
        except:
            print("Invalid MIDI file @ path: {}".format(file))
