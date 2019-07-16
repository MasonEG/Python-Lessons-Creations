from tkinter import *

root = Tk()

label_1 = Label(root, text='Name')
label_2 = Label(root, text='Password')
entry_1 = Entry(root)
entry_2 = Entry(root)
c = Checkbutton(root, text='Stay Logged In')#text goes to the right

#sets row and col to 0 by default, sticky is text allign in N, S, E, W
label_1.grid(sticky=E)
label_2.grid(row=1)

entry_1.grid(row=0,column=1) #had to set row to 0 for some reason
entry_2.grid(row=1, column=1)
c.grid(columnspan=2)#take 2 columns

root.mainloop()
