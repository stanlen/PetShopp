from statistics import geometric_mean
from tkinter import *
import tkinter as tk
from webbrowser import BackgroundBrowser

root = tk.Tk()
root.geometry("600x600")
root.configure(background='blue')
image = tk.PhotoImage(file='cad_pet.png')
image = image.subsample(1,1)
labelimage = tk.Label(image = image, background='blue')
labelimage.place(x=0,y=0,relwidth=1.0,relheight=1.0)

root.mainloop()