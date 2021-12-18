import tkinter as tk
from tkinter import filedialog, Text
import os
from os import path

root = tk.Tk()
root.winfo_toplevel().title("Text Editor")
root.winfo_toplevel().minsize(1400,750)

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack(fill="both")

frame = tk.Frame(root)
frame.place(relwidth=0.75, relheight=0.75, relx=0.1, rely=0.1)

editor = tk.Text(master=frame, width = 500, height =500, padx=10, pady=10)
editor.pack(fill="both")

def openF():
    print("Opening File")

    fileName = title.get("1.0",'end-1c')
    editor.delete("1.0",'end-1c')

    filePath = "/Users/krishitrip/atom/textEditor/textFiles"
    filePath += "/" + fileName + ".txt"

    if(path.exists(filePath)):
        text_file = open(filePath, "r")
        content = text_file.read()
        editor.insert("1.0", content)
    else:
        tk.messagebox.showinfo("Message", "File not found")



openFile = tk.Button(root, text="Open", padx=10, pady=5, fg="white", bg="#263D42", command=openF)
openFile.pack(side="left")

def saveF():
    print("Saving File")

    content = editor.get("1.0",'end-1c')
    fileName = title.get("1.0",'end-1c')

    path = "/Users/krishitrip/atom/textEditor/textFiles"
    path += "/" + fileName + ".txt"
    text_file = open(path, "w")
    text_file.write(content)
    text_file.close()


saveFile = tk.Button(root, text="Save", padx=10, pady=5, fg="white", bg="#263D42", command=saveF)
saveFile.pack(side="left")

title = tk.Text()
title.height = 1
title.pack(side="right")

root.mainloop()
