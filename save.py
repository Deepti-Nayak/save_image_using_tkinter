from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import ImageTk, Image, ImageDraw
import cv2
import numpy as np
from numpy import asarray


# --- functions ---

def savefile():
    filename = filedialog.asksaveasfile(mode='wb', defaultextension=".png",
                                    filetypes=[
                                        ("png file", ".png"),
                                        ("jpg file",".jpg"),
                                        ("text file",".txt"),
                                        ("All files", ".*"),
                                    ])    
                                    
                                        
                           
                                    
    if not filename:
         return
    edge.save(filename)


    
# --- main ---

root = tk.Tk()
root.filename = filedialog.askopenfilename(initialdir="/", title="Select A file",
                                           filetypes=(("png files", ".png"),
                                                      ("jpeg files", ".jpg"),
                                                      ("all files", "*")))
#my_label = Label(root, text=root.filename).pack()
#mageTk.PhotoImage(Image.open(root.filename))
#upload_img_label = Label(image=upload_img).pack()


my_img1 = Image.open(root.filename)
data = asarray(my_img1)
edge = Image.fromarray(data)
tk_edge = ImageTk.PhotoImage(edge)
label = tk.Label(root, image=tk_edge)
label.pack()

button1= tk.Button(root, text="save as", command=savefile)
button2=tk.Button(root,text="cancel",command=root.destroy)
button1.pack()
button2.pack()

root.mainloop()