from tkinter import *


#need 2 new lines before declaring a class
class FirstPythonClass:

    def __init__(self, master): #automatic constructor! master is the root passed in
        frame = Frame(master)
        frame.pack()
        #self creates a var to the class
        self.printButton = Button(frame, text='Print Message', command=self.printMessage)
        self.printButton.pack(side=LEFT)

        self.quitButton = Button(frame, text='Quit', command=frame.quit) #frame.quit breaks the mainloop
        self.quitButton.pack(side=LEFT) #goes to the leftest side it can, in this case its to the right of printButton

    def printMessage(self):
        print('Hey thats pretty good')


root = Tk()
b = FirstPythonClass(root)
root.mainloop()
