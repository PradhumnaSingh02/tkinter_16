from tkinter import *

def upload():
    status.set("Busy....")
    sbar.update()
    import time
    time.sleep(2)
    status.set("Ready")
root = Tk()
root.geometry('644x456')
root.title('GUI Work page')

status = StringVar()
status.set("Ready")
sbar = Label(root, textvariable=status, relief=SUNKEN)
sbar.pack(side=BOTTOM, fill=X, anchor='nw')

Button(root, text='Upload', command=upload).pack()


root.mainloop()