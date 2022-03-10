#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow as tf


# In[2]:


import PIL
from PIL import ImageTk, ImageDraw, Image, ImageOps
from tkinter import *
from keras.preprocessing import image
import os


# In[3]:


def determine_character(res,acc):
    print(res)
    if res == 10:
        print('prediction : क')
        character.configure(text= 'क,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 21:
        print('prediction : ख')
        character.configure(text= 'ख,')
        accuracy.configure(text=str(acc) + '%')
    
    elif res == 29:
        print('prediction : ग')
        character.configure(text= 'ग,')
        accuracy.configure(text=str(acc) + '%')
    
    elif res == 30:
        print('prediction : घ')
        character.configure(text= 'घ,')
        accuracy.configure(text=str(acc) + '%')        

    elif res == 31:
        print('prediction : ङ')
        character.configure(text= 'ङ,')
        accuracy.configure(text=str(acc) + '%')
        
    elif res == 32:
        print('prediction : च')
        character.configure(text= 'च,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 33:
        print('prediction : छ')
        character.configure(text= 'छ,')
        accuracy.configure(text=str(acc) + '%')
        
    elif res == 34:
        print('prediction : ज')
        character.configure(text= 'ज,')
        accuracy.configure(text=str(acc) + '%')
        
    elif res == 35:
        print('prediction : झ')
        character.configure(text= 'झ,')
        accuracy.configure(text=str(acc) + '%')
        
    elif res == 0:
        print('prediction : ञ')
        character.configure(text= 'ञ,')
        accuracy.configure(text=str(acc) + '%')
        
    elif res == 1:
        print('prediction : ट')
        character.configure(text= 'ट,')
        accuracy.configure(text=str(acc) + '%')
        
    elif res == 2:
        print('prediction : ठ')
        character.configure(text= 'ठ,')
        accuracy.configure(text=str(acc) + '%')
        
    elif res == 3:
        print('prediction : ड')
        character.configure(text= 'ड,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 4:
        print('prediction : ढ')
        character.configure(text= 'ढ,')
        accuracy.configure(text=str(acc) + '%')    
    
    elif res == 5:
        print('prediction : ण')
        character.configure(text= 'ण,')
        accuracy.configure(text=str(acc) + '%')
        
    elif res == 6:
        print('prediction : त')
        character.configure(text= 'त,')
        accuracy.configure(text=str(acc) + '%')
        
    elif res == 7:
        print('prediction : थ')
        character.configure(text= 'थ,')
        accuracy.configure(text=str(acc) + '%')        
        
    elif res == 8:
        print('prediction : द')
        character.configure(text= 'द,')
        accuracy.configure(text=str(acc) + '%')        
        
    elif res == 9:
        print('prediction : ध')
        character.configure(text= 'ध,')
        accuracy.configure(text=str(acc) + '%')        
        
    elif res == 11:
        print('prediction : न')
        character.configure(text= 'न,')
        accuracy.configure(text=str(acc) + '%')        
        
    elif res == 12:
        print('prediction : प')
        character.configure(text= 'प,')
        accuracy.configure(text=str(acc) + '%')    
    elif res == 13:
        print('prediction : फ')
        character.configure(text= 'फ,')
        accuracy.configure(text=str(acc) + '%')        
        
    elif res == 14:
        print('prediction : ब')
        character.configure(text= 'ब,')
        accuracy.configure(text=str(acc) + '%')           
        
    elif res == 15:
        print('prediction : भ')
        character.configure(text= 'भ,')
        accuracy.configure(text=str(acc) + '%')           
        
    elif res == 16:
        print('prediction : म')
        character.configure(text= 'म,')
        accuracy.configure(text=str(acc) + '%')           
        
    elif res == 17:
        print('prediction : य')
        character.configure(text= 'य,')
        accuracy.configure(text=str(acc) + '%')           
        
    elif res == 18:
        print('prediction : र')
        character.configure(text= 'र,')
        accuracy.configure(text=str(acc) + '%')           
        
    elif res == 19:
        print('prediction : ल')
        character.configure(text= 'ल,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 20:
        print('prediction : व')
        character.configure(text= 'व,')
        accuracy.configure(text=str(acc) + '%')           
        
    elif res == 22:
        print('prediction : श')
        character.configure(text= 'श,')
        accuracy.configure(text=str(acc) + '%')           
        
    elif res == 23:
        print('prediction : ष')
        character.configure(text= 'ष,')
        accuracy.configure(text=str(acc) + '%')           
        
    elif res == 24:
        print('prediction : स')
        character.configure(text= 'स,')
        accuracy.configure(text=str(acc) + '%')           
        
    elif res == 25:
        print('prediction : ह')
        character.configure(text= 'ह,')
        accuracy.configure(text=str(acc) + '%')           
        
    elif res == 26:
        print('prediction : क्ष')
        character.configure(text= 'क्ष,')
        accuracy.configure(text=str(acc) + '%')           
        
    elif res == 27:
        print('prediction : त्र')
        character.configure(text= 'त्र,')
        accuracy.configure(text=str(acc) + '%')  
    elif res == 28:
        print('prediction : ज्ञ')
        character.configure(text= 'ज्ञ,')
        accuracy.configure(text=str(acc) + '%')           
        
    elif res == 36:
        print('prediction : ०')
        character.configure(text= '०,')
        accuracy.configure(text=str(acc) + '%')           
        
    elif res == 37:
        print('prediction : १')
        character.configure(text= '१,')
        accuracy.configure(text=str(acc) + '%')           
        
    elif res == 38:
        print('prediction : २')
        character.configure(text= '२,')
        accuracy.configure(text=str(acc) + '%')           
        
    elif res == 39:
        print('prediction : ३')
        character.configure(text= '३,')
        accuracy.configure(text=str(acc) + '%')           
        
    elif res == 40:
        print('prediction : ४')
        character.configure(text= '४,')
        accuracy.configure(text=str(acc) + '%')           
        
    elif res == 41:
        print('prediction : ५')
        character.configure(text= '५,')
        accuracy.configure(text=str(acc) + '%')
    elif res == 42:
        print('prediction : ६')
        character.configure(text= '६,')
        accuracy.configure(text=str(acc) + '%')           
        
    elif res == 43:
        print('prediction : ७')
        character.configure(text= '७,')
        accuracy.configure(text=str(acc) + '%')           
        
    elif res == 44:
        print('prediction : ८')
        character.configure(text= '८,')
        accuracy.configure(text=str(acc) + '%')           
        
    elif res == 45:
        print('prediction : ९')
        character.configure(text= '९,')
        accuracy.configure(text=str(acc) + '%')           


# In[4]:


from tkinter import *
import PIL
from PIL import Image, ImageDraw


def save():
    global image_number
    img_path = "C:/Users/dipsb/Desktop/TE_PROJECT - FINAL/images/image.png"
#     filename = f'image_{image_number}.png'   # image_number increments by 1 at every save
    image1.save(img_path)
    image_number += 1


def activate_paint(e):
    global lastx, lasty
    cv.bind('<B1-Motion>', paint)
    lastx, lasty = e.x, e.y


def paint(e):
    global lastx, lasty
    x, y = e.x, e.y
    cv.create_line((lastx, lasty, x, y), fill='white', width=15)
    #  --- PIL
    draw.line((lastx, lasty, x, y), fill='white', width=15)
    lastx, lasty = x, y


root = Tk()

lastx, lasty = None, None
image_number = 0

cv = Canvas(root, width=200, height=200, bg='black')
# --- PIL
image1 = PIL.Image.new('RGB', (200, 200), 'black')
draw = ImageDraw.Draw(image1)

cv.bind('<1>', activate_paint)
cv.pack(expand=YES, fill=BOTH)

btn_save = Button(text="save", command=save)
btn_save.pack()

root.mainloop()


# In[5]:


import numpy as np
import matplotlib.pyplot as plt
from tkinter import *
import tkinter as tk
# loading Python Imaging Library 
from PIL import ImageTk, Image 
from keras.models import load_model
from tkinter import filedialog


# In[6]:


pip install h5py


# In[7]:


classifier = tf.keras.models.load_model('Model_CNN_DevanagariHandWrittenCharacterRecognition.h5')


# In[11]:


#same file path
#classifier = load_model('CNN_DevanagariHandWrittenCharacterRecognition.json')
#classifier.load_weights('CNN_DevanagariHandWrittenCharacterRecognition.h5')
# Import tkinter,PIL
from tkinter import *
import PIL
from PIL import Image, ImageDraw


# Delete image
def delete_created_image():
    os.remove('C:/Users/dipsb/Data Science/image.jpg')
    
    
# Clear image from canvas
def clear():
    delete_created_image()
    path = "C:/Users/dipsb/Data Science/placeholder.jpg"
    img = Image.open(path) 
    img = img.resize((200, 200), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img) 
    panel = Label(root, image = img) 

    # set the image as img  
    panel.image = img 
    panel.grid(row = 1, pady=2, padx=2)
    character.configure(text="")
    accuracy.configure(text="Upload / Draw")


# Open image from folder
def open_img(): 
    # Select the Imagename  from a folder  
    x = openfilename() 
    print(x)
    # opens the image 
    img = Image.open(x) 
      
    # resize the image and apply a high-quality down sampling filter 
    img = img.resize((200, 200), Image.ANTIALIAS)
    
    #img = ImageOps.invert(img)
    filename = 'C:/Users/dipsb/Data Science/image.jpg'
    img.save(filename)
    # PhotoImage class is used to add image to widgets, icons etc 
    img = ImageTk.PhotoImage(img) 
    panel = Label(root, image = img) 
      
    # set the image as img  
    panel.image = img 
    panel.grid(row = 1, pady=5, padx=5)

# Open file dialog
def openfilename(): 
    # open file dialog box to select image 
    filename = filedialog.askopenfilename(title ='Upload/ Draw Image') 
    return filename 
    
    
# Save handwritten image
def save():
#     global image_number
    img_path = 'C:/Users/dipsb/Data Science/image.jpg'
    image1.save(img_path)
#     image_number += 1


# X,Y Coordinates
lastx, lasty = None, None
# image_number = 0

# Activating canvas
def activate_paint(e):
    global lastx, lasty
    cv.bind('<B1-Motion>', paint)
    lastx, lasty = e.x, e.y

    
# Creating canvas
def paint(e):
    global lastx, lasty
    x, y = e.x, e.y
    cv.create_line((lastx, lasty, x, y), fill='white', width=15)
    #  --- PIL
    draw.line((lastx, lasty, x, y), fill='white', width=15)
    lastx, lasty = x, y
    
# Predicting an image
def single_prediction(test_img):
    
    test_img_arr = image.img_to_array(test_img)
    test_img_arr = np.expand_dims(test_img_arr, axis = 0)
    
    prediction = classifier.predict(test_img_arr)
    
    result = np.argmax(prediction[0])
    
    acc = round(prediction[0][np.argmax(prediction[0])]*100,3)
    print(acc)
    
    res = classifier.predict([test_img_arr])[0]
    print(res, np.argmax(res), max(res))
    
    determine_character(result, str(acc))
    
    
# Prediction function
def model():
    accuracy.configure(text="Predicting...")
    test_img = image.load_img('C:/Users/dipsb/Data Science/image.jpg', target_size = (32, 32, 3))
    single_prediction(test_img)
    plt.imshow(test_img)

    
# Create a window 
root = Tk() 

# Set Title as Image Loader 
root.title("r-Elearn: Handwritten Character Recognition") 
root.resizable(0,0)

# Set the resolution of window 
root.geometry("640x360+300+150") 
root['bg'] = '#000'

cv = Canvas(root, width=200, height=200, bg='black')
image1 = PIL.Image.new('RGB', (200, 200), 'black')
draw = ImageDraw.Draw(image1)

cv.bind('<1>', activate_paint)
# cv.pack(expand=YES, fill=BOTH)
cv.grid(row = 1, pady=5, padx=5)

# btn_save = Button(text="save", command=save)
# btn_save.pack()

icon = PhotoImage(file = "C:/Users/dipsb/Data Science/icon.png") 
  
# Setting icon of master window 
character = tk.Label(root, text="", font=("Helvetica", 70), bg="black", fg="white")
character.grid(row=1, column=2,pady=2, padx=2)

accuracy = tk.Label(root, text="     Upload / Draw    ", font=("Helvetica", 38), bg="black", fg="white")
accuracy.grid(row=1, column=5,pady=2, padx=2)

#functions
btnPredict=tk.Button(text="Predict",command=model, height=2, width=30, relief=GROOVE, bg="white", fg="black")
btnPredict.grid(row=3, column=5, pady=2, padx=5)

btnClear=tk.Button(text="Clear",command=clear, height=2, width=30, relief=GROOVE, bg="white", fg="black")
btnClear.grid(row=2, column=0, pady=2)

btnSave = Button(root, text ='Save', command = save, pady=2, padx=2, height=2, width=30, relief=GROOVE, bg="white", fg="black")
btnSave.grid(row=3, column=0, pady=2)

btnOpenImg = Button(root, text ='Open Image', command = open_img, pady=2, padx=2, height=2, width=30, relief=GROOVE, bg="white", fg="black")
btnOpenImg.grid(row=0, column=0, pady=2)

root.mainloop()


# In[9]:


import PIL
from PIL import Image, ImageDraw


def save():
    global image_number
    img_path = "C:/Users/dipsb/Data Science/image.png"
#     filename = f'image_{image_number}.png'   # image_number increments by 1 at every save
    image1.save(img_path)
    image_number += 1
    root.destroy()


def activate_paint(e):
    global lastx, lasty
    cv.bind('<B1-Motion>', paint)
    lastx, lasty = e.x, e.y


def paint(e):
    global lastx, lasty
    x, y = e.x, e.y
    cv.create_line((lastx, lasty, x, y), fill='white', width=15)
    #  --- PIL
    draw.line((lastx, lasty, x, y), fill='white', width=15)
    lastx, lasty = x, y

root = Tk()

lastx, lasty = None, None
image_number = 0

cv = Canvas(root, width=200, height=200, bg='black')
# --- PIL
image1 = PIL.Image.new('RGB', (200, 200), 'black')
draw = ImageDraw.Draw(image1)

cv.bind('<1>', activate_paint)
cv.pack(expand=YES, fill=BOTH)

btn_save = Button(text="save", command=save,)
btn_save.pack()

root.mainloop()


# In[ ]:




