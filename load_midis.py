import read_midi, model_storage
from os import listdir, stat
from os.path import isfile, join, isdir

start_dir = 0
start_file = 0
dataset_record_file = open("dataset_record.txt", "r")
if stat("dataset_record.txt").st_size == 0:
    print('Dataset record file is empty.\nRestarting model training from start of dataset...')
else:
    path = dataset_record_file.read().split("\\")
    start_dir = path[-2]
    start_file = path[-1]
    print("{}\t{}".format(start_dir, start_file))

dataset_record_file.close()

root_path = "E:\Project Stuff\lmd_full"
midi_directory_paths = [join(root_path, midi_directory_name) for midi_directory_name in listdir(root_path) if
                        isdir(join(root_path, midi_directory_name))]
files_trained = 0

if start_dir is not 0:
    start_dir = midi_directory_paths.index(join(root_path, start_dir))
for i in range(start_dir, len(midi_directory_paths)):
    directory = midi_directory_paths[i]
    print(":->\tDirectory: {}".format(directory))
    midi_file_paths = [join(directory, midi_file_name) for midi_file_name in listdir(directory) if
                       isfile(join(directory, midi_file_name))]
    if start_file is not 0:
        start_file = midi_file_paths.index(join(midi_directory_paths[i], start_file))
        print("Resuming learning from path: {}".format(midi_file_paths[start_file]))
    else:
        print("Initiating learning from path: {}".format(midi_file_paths[0]))
    for j in range(start_file, len(midi_file_paths)):
        file = midi_file_paths[j]
        try:
            print("\t:->File No. {}: {}".format(files_trained + 1, file))
            if read_midi.train_model(file) is 0:
                files_trained += 1
            if files_trained % 25 is 0:
                print("Saving model...")
                model_storage.save()
                dataset_record_file = open("dataset_record.txt", "wt")
                dataset_record_file.write(
                    '{}\\{}'.format(midi_file_paths[j].split('\\')[-2], midi_file_paths[j].split('\\')[-1]))
                dataset_record_file.close()
                print("Dataset record file updated succesfully!")
        except:
            print("Invalid MIDI file @ path: {}".format(file))
