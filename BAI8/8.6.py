print("Nguyễn Xuân Dịu")
print("235752021610078")
from tkinter import *

def NewFile():
    print("New File!")

def OpenFile():
    print("Open File!")

def Exit():
    print("Exit Program!")
    root.quit()

def InsText():
    print("Insert Text!")

def InsPic():
    print("Insert Picture!")

def About():
    print("This is a simple example of a menu")

root = Tk()
menu = Menu(root)
root.config(menu=menu)

# Menu "File"
filemenu = Menu(menu)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Exit)

# Menu "Insert"
insertmenu = Menu(menu)
menu.add_cascade(label="Insert", menu=insertmenu)
insertmenu.add_command(label="Text", command=InsText)
insertmenu.add_command(label="Picture", command=InsPic)

# Menu "Help"
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)

root.mainloop()
