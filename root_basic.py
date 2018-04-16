import tkinter
from tkinter import mainloop,Label
root= tkinter.Tk()
w=Label(root,text="This is a beta version. The program comes without guarantee that the results are correct.")
w.pack()
root.mainloop()
print('Gui opened')
##from tkinter import filedialog
from tkinter.filedialog import askopenfilename
filename = askopenfilename()
print(filename)
