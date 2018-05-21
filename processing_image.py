import os
import sys
import shutil

from keras.models import Sequential

from keras.layers import Input, Dense, Convolution2D, MaxPooling2D, AveragePooling2D, ZeroPadding2D, Dropout, Flatten, merge, Reshape, Activation
from keras.layers.normalization import BatchNormalization
from keras.models import Model
from keras import backend as K
from keras.callbacks import ModelCheckpoint
import glob
from custom_layers.scale_layer import Scale
from keras.optimizers import Nadam
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

LABELS = {0:'T0_018', 1:'T0_019', 2:'T0_020'}
tmp =[]
def processing(images):
    # print(images)
    img_rows, img_cols = 224, 224
    model = load_model('/home/buiduchanh/WorkSpace/demo_jestson/model/weights.21-0.88502994.hdf5', custom_objects={"Scale": Scale})
    nadam = Nadam(lr=1e-06, beta_1=0.9, beta_2=0.999, epsilon=1e-08, schedule_decay=0.004)
    model.compile(optimizer=nadam, loss='categorical_crossentropy', metrics=['accuracy'])
    print(type(model))
    image_=[]
    img = image.load_img(images,target_size=(img_cols, img_rows))
    x = image.img_to_array(img)
    image_.append(x)
    # print(x)
    y_proba = model.predict(np.array(image_))
    print(y_proba)
    # y_classes = y_proba.argmax(axis=-1)
    for result in y_proba:
        tmp.append('{} : {} "\n"'.format("Labels", result))
    # return np.array2string(y_proba)
    # print(tmp)
    str1 = ''.join(tmp)
    return str1