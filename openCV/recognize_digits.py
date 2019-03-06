import numpy as np
from sklearn.svm import LinearSVC
import os
import cv2
import joblib

# Generate training set
TRAIN_PATH = "Numbers/Train"
number_folders = os.listdir(TRAIN_PATH)
trainset = []
for folder in number_folders:
    number_path = os.path.join(TRAIN_PATH, folder)
    files_list = os.listdir(number_path)
    for f in files_list:
        fpath = os.path.join(TRAIN_PATH, folder, f)
        im = cv2.imread(fpath)
        im = cv2.resize(im, (20,20))
        trainset.append(im)
trainset = np.reshape(trainset, (5000, -1))

train_label = []
for i in range(0,10):
    temp = 500*[i]
    train_label += temp

clf = LinearSVC()
clf.fit(trainset, train_label)
print("Training finished")
joblib.dump(clf, "classifier.pkl", compress=3)