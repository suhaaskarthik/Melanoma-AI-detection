import tkinter as tk
from tkinter import filedialog
from tkinter import colorchooser
from PIL import Image, ImageOps, ImageTk, ImageFilter
from tkinter import ttk
from tkinter import Text,Label
import tensorflow as tf
import random
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from tensorflow import keras
import os
import time
from tkinter import *
res = ''
def load_and_prep(filename, img_shape = 224):
  img = tf.io.read_file(filename)
  img = tf.image.decode_image(img)
  img = tf.image.resize(img, size = [img_shape, img_shape])
  img = img/225.
  return img
loadmodel = tf.keras.models.load_model('melanoma3')
root = tk.Tk()
root.geometry("2000x1200")
root.title("Melanoma diagnosis")
root.config(bg="white")


pen_color = "black"
pen_size = 5
file_path = ""
cat_to_name = {0:'benign', 1:'malignant'}

def add_image():
    global file_path
    global res
    file_path = filedialog.askopenfilename(
        initialdir="D:/codefirst.io/Tkinter Image Editor/Pictures")
    val = round(loadmodel.predict(tf.expand_dims(load_and_prep(file_path),axis = 0))[0][0]*100,2)
    res = cat_to_name[round(loadmodel.predict(tf.expand_dims(load_and_prep(file_path),axis = 0))[0][0])].upper()
    title2.config(text = 'The lesion is:' , bg = 'white', fg = 'black')
    if val>40 and val<60:
    	lab.config(text = "The model isn't able to properly distinguish, please consult a doctor", bg = '#692206', fg = '#e84302',font =("calbri", 15))
    else:
	    if res == 'MALIGNANT':
	    	lab.config(text = str(val)+ '% '+ res, bg = '#6e0519', fg = '#fc1e1e',font =("calbri", 20))
	    if res == 'BENIGN':
	    	lab.config(text = str(100-val)+ '% '+res, bg = '#043d0f', fg = '#09d931',font =("calbri", 20))
    from PIL import Image
    image = Image.open(file_path)
    width, height = int(image.width / 2), int(image.height / 2)
    image = image.resize((width, height))
    canvas.config(width=image.width, height=image.height)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")
    # pb.start()
    # root.after(3000, pb.stop())
def change_color():
    global pen_color
    pen_color = colorchooser.askcolor(title="Select Pen Color")[1]


def change_size(size):
    global pen_size
    pen_size = size


def draw(event):
    x1, y1 = (event.x - pen_size), (event.y - pen_size)
    x2, y2 = (event.x + pen_size), (event.y + pen_size)
    canvas.create_oval(x1, y1, x2, y2, fill=pen_color, outline='')
    

def clear_canvas():
    canvas.delete("all")
    canvas.create_image(0, 0, image=canvas.image, anchor="nw")


def apply_filter(filter):
    image = Image.open(file_path)
    width, height = int(image.width / 2), int(image.height / 2)
    image = image.resize((width, height), Image.ANTIALIAS)
    if filter == "Black and White":
        image = ImageOps.grayscale(image)
    elif filter == "Blur":
        image = image.filter(ImageFilter.BLUR)
    elif filter == "Sharpen":
        image = image.filter(ImageFilter.SHARPEN)
    elif filter == "Smooth":
        image = image.filter(ImageFilter.SMOOTH)
    elif filter == "Emboss":
        image = image.filter(ImageFilter.EMBOSS)
    image = ImageTk.PhotoImage(image)
    canvas.image = image
    canvas.create_image(0, 0, image=image, anchor="nw")
from PIL import ImageTk, Image
left_frame = tk.Frame(root, width=200, height=600, bg="white")
left_frame.pack(side="top", fill="y")
# bg = ImageTk.PhotoImage(Image.open("bg.png"))
# label1 = Label( root, image = bg)
# label1.place(x = 300, y = 0)
b_frame = tk.Frame(root, width=200, height=600, bg="white")
b_frame.pack(side="bottom", fill="y")
title = Label(left_frame,text = "M e l a n o m a  A I  d i a g n o s i s")
title.config(font =("calbri", 40, 'bold'))
title.pack()
title = Label(left_frame,text = "")
title.config(font =("calbri", 18),fg='#574e59', bg = 'white')
title.pack()
title = Label(left_frame,text = "Melanoma is a deadly skin cancer. Once present, it will rapidly take over the body,so early detection and treatment is a MUST!")
title.config(font =("calbri", 16),fg='#574e59')
title.pack()
title = Label(left_frame,text = "A hospital diagnosis will take around 3 weeks with just an 86% accuracy" )
title.config(font =("calbri", 16),fg='#574e59')
title.pack()
title = Label(left_frame,text = "Instead we can wield the power of convolutional neural networks to solve this issue in just seconds" )
title.config(font =("calbri", 16),fg='#574e59')
title.pack()
title = Label(left_frame,text = "This program has a powerful AI in its backend, which can diagnose melanoma with 92% accuracy" )
title.config(font =("calbri", 16),fg='#574e59')
title.pack()
title = Label(left_frame,text = "Just need to upload a clear picture of the lesion (damaged part of the skin), and the AI will work its magic" )
title.config(font =("calbri", 16), fg='#574e59')
title.pack()
title = Label(left_frame,text = "")
title.config(font =("calbri", 16),fg='#574e59', bg = 'white')
title.pack()
# pb = ttk.Progressbar(
#     b_frame,
#     orient='horizontal',
#     mode='indeterminate',
#     length=280
# )
# # place the progressbar
# pb.pack()
title2 = Label(b_frame,text = "")
title2.config(font =("calbri", 14),fg='#574e59', bg = 'white')
title2.pack()
lab = Label(b_frame,text = res)
lab.config(font =("calbri", 20), bg='white')
lab.pack()

lab1 = Label(b_frame,text = '')
lab1.config(font =("calbri", 30), bg='white')
lab1.pack()
lab1 = Label(b_frame,text = '')
lab1.config(font =("calbri", 30), bg='white')
lab1.pack()
lab1 = Label(b_frame,text = '')
lab1.config(font =("calbri", 30), bg='white')
lab1.pack()
lab1 = Label(b_frame,text = '')
lab1.config(font =("calbri", 30), bg='white')
lab1.pack()

# Create text widget and specify size.
 
# Create label

# Import Required Module
from tkinter import *
from tkinter.ttk import *
 
style = Style()
 
style.configure('TButton', font =
               ('calibri', 15, ),
                    borderwidth = '4')
image_button = Button(left_frame, text="Upload lesion",
                         command=add_image, style = 'TButton')
image_button.pack()



canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()
canvas.bind("<B1-Motion>", draw)

root.mainloop()
