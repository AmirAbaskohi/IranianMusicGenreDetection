import os
from tqdm import tqdm
from mutagen.mp3 import MP3

DATA_PATH = ".." + os.sep + "data"

def getAllMusicsTimeInSeconds():
    result = []
    for subdir, dirs, files in os.walk(DATA_PATH):
        for file in tqdm(files):
            file_path = DATA_PATH + os.sep + subdir.split(os.sep)[2] + os.sep + file 
            audio = MP3(file_path)
            result.append(int(audio.info.length))
    return result

if __name__ == '__main__':
    print(getAllMusicsTimeInSeconds()[:5])