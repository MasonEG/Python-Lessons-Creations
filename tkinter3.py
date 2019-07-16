from tkinter import *

root = Tk()

one = Label(root, text='One', fg='yellow', bg= 'blue')
one.pack()
two = Label(root, text="Two", bg='green', fg='red')
two.pack(fill=X) #fills to whatever x value the window is, run it to understand
button = Button(root, text='button')
button.pack(fill=Y, side=RIGHT)
three = Label(root, text='Three', fg='white', bg='black')
three.pack(side=LEFT, fill=Y)
testFrame = Frame(root, width=600, height=600)
testFrame.pack(side=BOTTOM)
testLabel = Label(testFrame, text='Testing', bg='Black', fg='White')
testLabel.pack(expand=1)

root.mainloop()
