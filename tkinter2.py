from tkinter import *

root = Tk()
buttonList = []

topFrame = Frame(root)
topFrame.pack() #automatically packs at the top
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM) #pack it at the bottom

buttonA = Button(topFrame, text='Button A', fg='magenta', bg="orange")
buttonB = Button(topFrame, text='Button B', fg='red', bg='blue')
buttonC = Button(topFrame, text='Button C', fg='blue')
buttonD = Button(bottomFrame, text='Button D', fg='green', bg='red')

buttonA.pack(side=LEFT)
buttonB.pack(side=LEFT)
buttonC.pack(side=LEFT)
buttonD.pack(side=LEFT)


#this code had to be commented for the tutorials sake
# buttonList.append(buttonA) #yeah I know I can merge lines 11-14 and 16-19
# buttonList.append(buttonB)
# buttonList.append(buttonC)
# buttonList.append(buttonD)

# for b in buttonList: #hot damn is that some pretty code
#     b.pack()


root.mainloop()
