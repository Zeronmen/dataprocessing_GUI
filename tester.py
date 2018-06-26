try:
    from tkinter import *
except ImportError:
    from Tkinter import *
import page_objects as po
import process_data as pd

root = Tk()

window1 = po.Start_Window(root)
window2 = po.Processing_Window(root)

root.mainloop()

