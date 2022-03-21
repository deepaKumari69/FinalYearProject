#!/usr/bin/env python
# coding: utf-8

# In[34]:


def determine_character(res,acc):
    print(res)
    if res == 0:
        print('prediction : अ')
        character.configure(text= 'अ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 4:
        print('prediction : आ')
        character.configure(text= 'आ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 5:
        print('prediction : इ')
        character.configure(text= 'इ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 6:
        print('prediction : ई')
        character.configure(text= 'ई,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 7:
        print('prediction : उ')
        character.configure(text= 'उ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 8:
        print('prediction : ऊ')
        character.configure(text= 'ऊ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 9:
        print('prediction : ए')
        character.configure(text= 'ए,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 10:
        print('prediction : ऐ')
        character.configure(text= 'ऐ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 11:
        print('prediction : ओ')
        character.configure(text= 'ओ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 1:
        print('prediction : औ')
        character.configure(text= 'औ,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 2:
        print('prediction : अं')
        character.configure(text= 'अं,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 3:
        print('prediction : अः')
        character.configure(text= 'अः,')
        accuracy.configure(text=str(acc) + '%')


# In[3]:


import tensorflow as tf
from keras.preprocessing import image
from keras.models import load_model


# In[4]:


pip install h5py


# In[21]:


import numpy as np


# # MAIN CODE BELOW

# In[44]:


import tensorflow as tf
from keras.preprocessing import image
from keras.models import load_model
pip install h5py
import numpy as np

classifier = tf.keras.models.load_model('CNN_vowel_model.h5')

test_img = image.load_img('C:/Users/dipsb/Data Science/image.png', target_size = (32, 32, 3))

def single_prediction(test_img):
    
    test_img_arr = image.img_to_array(test_img)
    test_img_arr = np.expand_dims(test_img_arr, axis = 0)
    
    prediction = classifier.predict(test_img_arr)
    
    result = np.argmax(prediction[0])
    
    acc = round(prediction[0][np.argmax(prediction[0])]*100,3)
    #print(acc)
    
    res = classifier.predict([test_img_arr])[0]
    #print(res, np.argmax(res), max(res))
    return np.argmax(res)

print(single_prediction(test_img))


# In[ ]:




