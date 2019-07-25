from tkinter import *

import threading

root = Tk()

v = IntVar()

Radiobutton(root, text='One', variable=v, value=1, ).pack(anchor=W)
Radiobutton(root, text='Two', variable=v, value=2, ).pack(anchor=W)
Radiobutton(root, text='Three', variable=v, value=3, ).pack(anchor=W)


def print_var():
    while True:
        print(v.get())


threading.Thread(target=print_var).start()

mainloop()
