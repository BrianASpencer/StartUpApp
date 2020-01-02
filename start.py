import tkinter as tk

from tkinter import filedialog, Text

import os


###### code here ######

# setting root
root = tk.Tk()

apps = []

#function to add apps to program list
def addApp():
    fileName = filedialog.askopenfile(initialdir = "/", title = "Select File",
                                    filetypes = (("executables", "*.exe"), ("all files", "*.*")))
    apps.append(fileName)
    print(fileName)
    #for app in apps:


# setting window properties and attaching those to our window
canvas = tk.Canvas(root, height = 700, width = 700, bg = "#345beb")
canvas.pack()


# frame
frame = tk.Frame(root, bg="white")
frame.place(relwidth = 0.75, relheight = 0.75, relx = 0.1, rely = 0.1)

# button to open .exe files
openFile = tk.Button(root, text = "Open File", padx = 10, 
                    pady = 5, fg = "white", bg = "#345beb", command = addApp)
openFile.pack()



# button to run apps
runApps = tk.Button(root, text = "Run Apps", padx = 10, 
                    pady = 5, fg = "white", bg = "#345beb")
runApps.pack()






# run
root.mainloop()