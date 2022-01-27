# IranianMusicGenreDetection
This is the final project of Machine Learning course of University of Tehran.

## Prerequisite

Install `ffmpeg` on Debian/Linux using bellow command:
```
apt-get install ffmpeg 
```

Then you have to install any library required based on the file you want to use.

## Data
About 270 `mp3` file were gathered for this project. Then we splitted files to 30 seconds frames in `wav` format.
After having files with equal length, we extracted features using `librosa` with different feature extraction methods like `MFCC` and `Zero Crossing Rate`.
Using this, our data was model readable data.

## Models
* Classification
  * SVM
  * MLP
  * KNN

* Clustring
  * DBSCAN
  * KMeans
  * K Medoids

## Results
![image](https://user-images.githubusercontent.com/50926437/151443349-4580d546-9b2e-4828-aca7-1e3d9205cc2f.png)
![image](https://user-images.githubusercontent.com/50926437/151443359-971bf895-8b7e-46ca-a928-f8cbb8ffc9ff.png)
