#!/usr/bin/env python
# coding: utf-8

# In[7]:


def determine_character(res,acc):
    print(res)
    if res == 0:
        print('prediction : অ')
        character.configure(text= 'অ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 1:
        print('prediction : ও')
        character.configure(text= 'ও,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 2:
        print('prediction : ঔ')
        character.configure(text= 'ঔ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 3:
        print('prediction : ক')
        character.configure(text= 'ক,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 4:
        print('prediction : খ')
        character.configure(text= 'খ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 5:
        print('prediction : গ')
        character.configure(text= 'গ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 6:
        print('prediction : ঘ')
        character.configure(text= 'ঘ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 7:
        print('prediction : ঙ')
        character.configure(text= 'ঙ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 8:
        print('prediction : চ')
        character.configure(text= 'চ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 9:
        print('prediction : ছ')
        character.configure(text= 'ছ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 10:
        print('prediction : জ')
        character.configure(text= 'জ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 11:
        print('prediction : আ')
        character.configure(text= 'আ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 12:
        print('prediction : ঝ')
        character.configure(text= 'ঝ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 13:
        print('prediction : ঞ')
        character.configure(text= 'ঞ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 14:
        print('prediction : ট')
        character.configure(text= 'ট,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 15:
        print('prediction : ঠ')
        character.configure(text= 'ঠ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 16:
        print('prediction : ড')
        character.configure(text= 'ড,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 17:
        print('prediction : ঢ')
        character.configure(text= 'ঢ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 18:
        print('prediction : ণ')
        character.configure(text= 'ণ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 19:
        print('prediction : ত')
        character.configure(text= 'ত,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 20:
        print('prediction : থ')
        character.configure(text= 'থ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 21:
        print('prediction : দ')
        character.configure(text= 'দ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 22:
        print('prediction : ই')
        character.configure(text= 'ই,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 23:
        print('prediction : ধ')
        character.configure(text= 'ধ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 24:
        print('prediction : ন')
        character.configure(text= 'ন,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 25:
        print('prediction : প')
        character.configure(text= 'প,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 26:
        print('prediction : ফ')
        character.configure(text= 'ফ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 27:
        print('prediction : ব')
        character.configure(text= 'ব,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 28:
        print('prediction : ভ')
        character.configure(text= 'ভ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 29:
        print('prediction : ম')
        character.configure(text= 'ম,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 30:
        print('prediction : য')
        character.configure(text= 'য,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 31:
        print('prediction : র')
        character.configure(text= 'র,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 32:
        print('prediction : ল')
        character.configure(text= 'ল,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 33:
        print('prediction : ঈ')
        character.configure(text= 'ঈ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 34:
        print('prediction : শ')
        character.configure(text= 'শ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 35:
        print('prediction : ষ')
        character.configure(text= 'ষ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 36:
        print('prediction : স')
        character.configure(text= 'স,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 37:
        print('prediction : হ')
        character.configure(text= 'হ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 38:
        print('prediction : ড়')
        character.configure(text= 'ড়,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 39:
        print('prediction : ঢ়')
        character.configure(text= 'ঢ়,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 40:
        print('prediction : য়')
        character.configure(text= 'য়,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 44:
        print('prediction : উ')
        character.configure(text= 'উ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 46:
        print('prediction : ০')
        character.configure(text= '০,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 47:
        print('prediction : ১')
        character.configure(text= '১,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 48:
        print('prediction : ২')
        character.configure(text= '২,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 49:
        print('prediction : ৩')
        character.configure(text= '৩,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 50:
        print('prediction : ৪')
        character.configure(text= '৪,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 51:
        print('prediction : ৫')
        character.configure(text= '৫,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 52:
        print('prediction : ৬')
        character.configure(text= '৬,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 53:
        print('prediction : ৭')
        character.configure(text= '৭,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 54:
        print('prediction : ৮')
        character.configure(text= '৮,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 55:
        print('prediction : ঊ')
        character.configure(text= 'ঊ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 56:
        print('prediction : ৯')
        character.configure(text= '৯,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 81:
        print('prediction : ম্ম')
        character.configure(text= 'ম্ম,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 82:
        print('prediction : ণ্ঠ')
        character.configure(text= 'ণ্ঠ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 83:
        print('prediction : ঐ')
        character.configure(text= 'ঐ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 66:
        print('prediction : ঋ')
        character.configure(text= 'ঋ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 77:
        print('prediction : এ')
        character.configure(text= 'এ,')
        accuracy.configure(text=str(acc) + '%')


# In[9]:


import tensorflow as tf
from keras.preprocessing import image
from keras.models import load_model

pip install h5py

import numpy as np

import PIL
from PIL import ImageTk, ImageDraw, Image, ImageOps
from tkinter import *
import os

classifier = tf.keras.models.load_model('CNN_model_bengali.h5')

test_img = image.load_img('C:/Users/dipsb/Data Science/image.jpg', target_size = (32, 32, 3))

def b_single_prediction(test_img):
    
    test_img_arr = image.img_to_array(test_img)
    test_img_arr = np.expand_dims(test_img_arr, axis = 0)
    
    prediction = classifier.predict(test_img_arr)
    
    result = np.argmax(prediction[0])
    
    acc = round(prediction[0][np.argmax(prediction[0])]*100,3)
    print(acc)
    
    res = classifier.predict([test_img_arr])[0]
    print(res, np.argmax(res), max(res))
    
   


# In[ ]:




