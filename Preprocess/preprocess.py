import os
import numpy as np
from numpy.lib.utils import source
import pandas as pd
import matplotlib.pyplot as plt
from tqdm import tqdm
from mutagen.mp3 import MP3
from pydub import AudioSegment

DATA_PATH = ".." + os.sep + "data"
FINAL_DATA_PATH = ".." + os.sep + "final_data"

size = 25
params = {'legend.fontsize': size,
          'figure.figsize': (25,15),
          'axes.labelsize': size,
          'axes.titlesize': size,
          'xtick.labelsize': size*0.75,
          'ytick.labelsize': size*0.75,
          'axes.titlepad': 25}
plt.rcParams.update(params)

def createDirectoryIfDoesNotExists(path):
    if not os.path.exists(path):
        os.makedirs(path)

def getAllMusicsTimeInSeconds():
    result = []
    for subdir, dirs, files in os.walk(DATA_PATH):
        for file in tqdm(files):
            filePath = DATA_PATH + os.sep + subdir.split(os.sep)[2] + os.sep + file 
            audio = MP3(filePath)
            result.append(int(audio.info.length))
    return result

def calLossForSplitDuration(durations, splitDuration):
    result = np.array(durations)
    return result%splitDuration

def getReportOfDataSet():
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

def splitMusics(lengthInMilliseconds):
    result = []
    for subdir, dirs, files in os.walk(DATA_PATH):
        for file in tqdm(files):
            splittedFile = file.split('.')
            fileName = ".".join(splittedFile[:-1])
            directory = subdir.split(os.sep)[2]
            filePath = DATA_PATH + os.sep + directory + os.sep + file

            sound = AudioSegment.from_file(filePath)
            soundLength = len(sound)
            numberOfParts = soundLength // lengthInMilliseconds
            loss = soundLength - numberOfParts * lengthInMilliseconds
            skipEnd = loss // 2
            skipStart = loss - skipEnd

            start = skipStart + 1
            for i in range(numberOfParts):
                partFilePath = FINAL_DATA_PATH + os.sep + directory + os.sep + fileName + "_" + str(i+1) + ".wav"
                part = sound[start: start+lengthInMilliseconds+1]

                createDirectoryIfDoesNotExists(FINAL_DATA_PATH + os.sep + directory)

                part.export(partFilePath , format="wav")
                start = start+lengthInMilliseconds+1

if __name__ == '__main__':
    splitMusics(30000)