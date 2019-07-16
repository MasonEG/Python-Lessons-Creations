from tkinter import *

root = Tk()

def printName(event): #remove event if you uncomment line 8
    print('mason')

# button_1 = Button(root, text='Print Name', command=printName)

button_1 = Button(root, text='Print Name')
button_1.bind('<Button-1>', printName) #<Button-1> is left click
button_1.pack()

root.mainloop()
