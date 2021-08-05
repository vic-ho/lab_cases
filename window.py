import tkinter
print(tkinter.TkVersion)

from tkinter import *

window = Tk()
window.title("Lunch Cash Bag")
screenwidth = window.winfo_screenwidth()
screenhigh = window.winfo_screenheight()
win_w = 600
win_h = 400
pos_x = (screenwidth-win_w)/2
pos_y = (screenhigh-win_h)/2
window.geometry("%dx%d+%d+%d" % (win_w, win_h, pos_x, pos_y))
window.maxsize(800, 600)
window.minsize(300, 200)
# root.config(bg="Blue")
# root.state("zoomed")
# root.iconify()
# root.iconbitmap("xx.ico")

window.mainloop()