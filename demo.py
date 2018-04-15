#import os
#rootcwd = os.getcwd()
#print(rootcwd)
print('Opening GUI to choose file')
import tkinter
from tkinter import *
#cwd = os.getcwd()
#print(cwd)
root= tkinter.Tk()
root
#print(root)
#w=Label(root,text="Hello ballllllllllllllllll")
#w.pack()
#root.withdraw()
root.mainloop()
print('Gui opened')
##from tkinter import filedialog
from tkinter.filedialog import askopenfilename
filename = askopenfilename()
print(filename)
