import numpy as np
import os
from PIL import Image
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
import tensorflow as tf
import cv2 as cv
from keras.models import load_model

import warnings
warnings.filterwarnings('ignore')


MODEL_PATH = "chimney_predict_model.h5"
CLASSES = ['Chimney cap damage', 'Guardrail Damage and platform damage', 'Hole', 'Ladder damage', 'Leak', 'Rust']
model = load_model(MODEL_PATH)
model.compiled_metrics == None

def preprocess(img):
    image = Image.open(img.stream)
    img = np.array(image)
    img = cv.cvtColor(img,cv.COLOR_RGB2GRAY)
    img = cv.resize(img, (255, 255))
    img = img / 255.0
    return img

def get_diseases(img_path):
    img = preprocess(img_path)
    img = np.reshape(img,(-1,255,255,1))
    predictions = model.predict(img)
    max_index = np.argmax(predictions)
    print(predictions)
    return CLASSES[max_index],max(predictions[0])

