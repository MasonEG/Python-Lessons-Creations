from tkinter import *

root = Tk()

def leftClick(event):
    print('Left')

def rightClick(event):
    print('Right')

def middleClick(event):
    print('Middle')

frame = Frame(root, width=600, height=500)
frame.bind('<Button-1>', leftClick) #set action for left click on the frame
frame.bind('<Button-2>', middleClick) #no middleclick on a laptop :(
frame.bind('<Button-3>', rightClick)
frame.pack()

root.mainloop()
