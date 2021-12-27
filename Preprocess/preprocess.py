import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
from mutagen.mp3 import MP3

DATA_PATH = ".." + os.sep + "data"

size = 25
params = {'legend.fontsize': size,
          'figure.figsize': (25,15),
          'axes.labelsize': size,
          'axes.titlesize': size,
          'xtick.labelsize': size*0.75,
          'ytick.labelsize': size*0.75,
          'axes.titlepad': 25}
plt.rcParams.update(params)

def getAllMusicsTimeInSeconds():
    result = []
    for subdir, dirs, files in os.walk(DATA_PATH):
        for file in tqdm(files):
            file_path = DATA_PATH + os.sep + subdir.split(os.sep)[2] + os.sep + file 
            audio = MP3(file_path)
            result.append(int(audio.info.length))
    return result

def calLossForSplitDuration(durations, splitDuration):
    result = np.array(durations)
    return result%splitDuration

if __name__ == '__main__':
    musicDurationsInSeconds = getAllMusicsTimeInSeconds()
    allDuration = sum(musicDurationsInSeconds)
    result = []
    for i in range(1, 61):
        result.append({"split time" : i, "loss total": sum(calLossForSplitDuration(musicDurationsInSeconds, i)), "number of new data": allDuration // i})
    result = pd.DataFrame(result)
    result.to_csv('split_result.csv')

    plt.plot(result['split time'], result['loss total'], "r-", label='loss')
    plt.plot(result['split time'], result['number of new data'], "b-", label='number of data')
    plt.legend(loc='upper left')
    plt.title('Data split result')
    plt.xlabel('Split duration')
    plt.savefig('split_result', dpi=600)