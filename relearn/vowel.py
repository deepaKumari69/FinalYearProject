import tensorflow as tf
from keras.preprocessing import image
from keras.models import load_model
import numpy as np

classifier = tf.keras.models.load_model('relearn/CNN_vowel_model.h5')
def single_prediction():
    
    test_img = image.load_img('../static/assets/images/input.jpg', target_size = (32, 32, 3))
    test_img_arr = image.img_to_array(test_img)
    test_img_arr = np.expand_dims(test_img_arr, axis = 0)
    prediction = classifier.predict(test_img_arr)
    result = np.argmax(prediction[0])
    acc = round(prediction[0][np.argmax(prediction[0])]*100,3)
    #print(acc)
    res = classifier.predict([test_img_arr])[0]
    #print(res, np.argmax(res), max(res))
    return np.argmax(res)