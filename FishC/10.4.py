from tkinter import *

root=Tk()

photo = PhotoImage(file='44.gif')
theLabel = Label(root,
                 text='因果循环',
                 justify=LEFT,
                 image=photo,
                 compound=CENTER,
                 fg='white')

theLabel.pack()

mainloop()

