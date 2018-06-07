from tkinter import *

root=Tk()

textLabel = Label(root, text='未闻其祥',
                  justify=LEFT,
                  padx=10)
textLabel.pack(side=LEFT)

photo = PhotoImage(file='44.gif')
imgLabel = Label(root,image=photo)
imgLabel.pack(side=RIGHT)

mainloop()
