from tkinter import *

def callback():
    var.set('无用')

root=Tk()

frame1 = Frame(root)
frame2 = Frame(root)

var = StringVar()
var.set('条件需满足')
textLabel = Label(frame1,
                  textvariable=var,
                  justify=LEFT)
textLabel.pack(side=LEFT)

photo = PhotoImage(file='44.gif')
imgLabel = Label(frame1,image=photo)
imgLabel.pack(side=RIGHT)

theButton = Button(frame2, text='条件已满足',command=callback)
theButton.pack()

frame1.pack(padx=10,pady=10)
frame2.pack(padx=10,pady=10)

mainloop()
