import numpy as np
import random
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import LSTM
import matplotlib.pyplot as plt

np.random.seed(1)
scaler = MinMaxScaler(feature_range=(0, 1))
look_back = 1

music_model = None


# generate temp dataset
def temp_generator(amount):
    chord_list = range(1, 133)
    velocity_list = range(0, 128)
    beats_list = range(1, 20)
    data = []
    for i in range(amount):
        b = []
        b.append(-1)
        b.append(random.sample(velocity_list, 1)[0])
        b.append(random.sample(chord_list, 1)[0])
        b.append(random.sample(beats_list, 1)[0])
        data.append(b)
    return np.array(data)


# split dataset into _t_ and _t+1_ components
def split_dataset(chunk, look_back=1):
    input_code = []
    target_code = []
    for i in range(len(chunk) - look_back - 1):
        a = chunk[i: i + look_back]
        input_code.append(a)
        target_code.append(chunk[i + look_back])
    return np.array(input_code), np.array(target_code)


# LSTM Model
def create_model():
    global music_model
    music_model = Sequential()
    music_model.add(LSTM((4), batch_input_shape=(None, 1, 4), return_sequences=True))
    music_model.add(LSTM((4), return_sequences=False))
    music_model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])


def train(datablock):
    global music_model
    # shape of dataset = (number_of_samples, number_of_features)
    datablock = scaler.fit_transform(datablock)
    trainX, trainY = split_dataset(datablock)
    music_model.fit(trainX, trainY, epochs=20)


def predict(starting_msg, music_length):
    global music_model
    generationOutput = []
    individual = starting_msg
    for i in range(music_length):
        trainPredict = music_model.predict(individual)
        individual = np.array([trainPredict])
        trainPredict = scaler.inverse_transform(trainPredict)  # un-normalize data
        # print(trainPredict.shape)
        generationOutput.append(trainPredict)
    generationOutput = np.array(generationOutput)

    print("Generated Output = {}".format(generationOutput))
    plt.plot(music_model.history['loss'])
    plt.show()
