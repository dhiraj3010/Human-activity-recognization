import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time

global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Human Action Recognition Using Machine Learning")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 = Image.open('a1.jpg')
image2 = image2.resize((1530, 1000), Image.ANTIALIAS)

background_image = ImageTk.PhotoImage(image2)

background_label = tk.Label(root, image=background_image)

background_label.image = background_image

background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)
#
label_l1 = tk.Label(root, text="Human Action Recognition Using Machine Learning",font=("Times New Roman", 35, 'bold'),
                    background="#152238", fg="white", width=50, height=2)
label_l1.place(x=0, y=0)



################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

def action():
   
    from subprocess import call
    call(["python","GUI_Master.py"])
#################################################################################################################
def window():
    root.destroy()



button1 = tk.Button(root, text="Petrol Pump",command=action, width=20, height=1, bg="#152238", fg="white",font=('times', 20, ' bold '))
button1.place(x=100, y=320)


button2 = tk.Button(root, text="School/College",command=action, width=20, height=1, bg="#152238", fg="white",font=('times', 20, ' bold '))
button2.place(x=300, y=320)


button3 = tk.Button(root, text="Railway",command=action, width=20, height=1, bg="#152238", fg="white",font=('times', 20, ' bold '))
button3.place(x=100, y=520)


button4 = tk.Button(root, text="Hospital",command=action, width=20, height=1, bg="#152238", fg="white",font=('times', 20, ' bold '))
button4.place(x=300, y=520)

exit = tk.Button(root, text="Exit", command=window, width=14, height=1, font=('times', 20, ' bold '), bg="cyan",fg="white")
exit.place(x=140, y=450)

root.mainloop()