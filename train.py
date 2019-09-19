import tensorflow as tf
from tensorflow import keras
import numpy as np
import cv2
import os
import glob

input_width = 48
input_height = 48

input_channel = 3
input_shape = (input_height, input_width, input_channel)
n_classes = 4

path_amekaji = glob.glob(
    os.path.join('./', 'data', 'train', 'amekaji', '*.jpg')
)
path_casual = glob.glob(
    os.path.join('./', 'data', 'train', 'casual', '*.jpg')
)
path_dandy = glob.glob(
    os.path.join('./', 'data', 'train', 'dandy', '*.jpg')
)

path_street = glob.glob(
    os.path.join('./', 'data', 'train', 'street', '*.jpg')
)
path_test = glob.glob(
    os.path.join('./', 'data', 'test', '*.jpg')
)

n_train = len(path_amekaji) + len(path_casual) + len(path_dandy) + len(path_street)
n_test = len(path_test)

trainset = np.zeros(
    shape=(n_train, input_height, input_width, input_channel),
    dtype='float32'
)
testset = np.zeros(
    shape=(n_test, input_height, input_width, input_channel),
    dtype='float32'
)
label = np.zeros(
    shape=(n_train, n_classes),
    dtype='float32'
)

path_train = path_amekaji + path_casual + path_dandy + path_street

for i, path in enumerate(path_train):
    try:
        img = cv2.imread(path)
        resized_img = cv2.resize(img, (input_width, input_height))
    except Exception as e:
        print(path)

for i, path in enumerate(path_test):
    try:
        img = cv2.imread(path)
        resized_img = cv2.resize(img, (input_width, input_height))
    except Exception as e:
        print(path)

begin, end = 0, 0
end = len(path_amekaji)
label[begin:end, 0] = 1.0
begin, end = end, end + len(path_casual)
label[begin:end, 1] = 1.0
begin, end = end, end + len(path_dandy)
label[begin:end, 2] = 1.0
begin, end = end, end + len(path_street)
label[begin:end, 3] = 1.0

trainset = trainset / 255.0
testset = testset / 255.0

model = keras.models.Sequential()
model.add(keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(input_shape)))
model.add(keras.layers.MaxPooling2D((2, 2)))
model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(keras.layers.MaxPooling2D((2, 2)))
model.add(keras.layers.Conv2D(64, (3, 3), activation='relu'))
model.add(keras.layers.Flatten())
model.add(keras.layers.Dense(64, activation='relu'))
model.add(keras.layers.Dense(n_classes, activation='softmax'))
model.compile(optimizer='Adam', loss='categorical_crossentropy', metrics=['accuracy'])
model.fit(trainset, label, epochs=10, batch_size=64)
model.save('./model.h5')

result_onehot = model.predict(testset)
result_sparse = np.argmax(result_onehot, axis=1)

print(result_onehot)
print('\n', result_sparse)

if int(result_sparse) == 0:
    print('amekaji')
elif int(result_sparse) == 1:
    print('casual')
elif int(result_sparse) == 2:
    print('dandy')
elif int(result_sparse) == 3:
    print('street')