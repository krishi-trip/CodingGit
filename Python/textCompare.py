import tkinter as tk
from tkinter import filedialog, Text
import os
from os import path

root = tk.Tk()
root.winfo_toplevel().title("Text Editor")
root.winfo_toplevel().minsize(1400,750)

canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
canvas.pack(fill="both")

frame = tk.Frame(master=root)
frame.place(relwidth=0.3, relheight=0.75, relx=0.1, rely=0.1)

frame2 = tk.Frame(root)
frame2.place(relwidth=0.3, relheight=0.75, relx=0.6, rely=0.1)

passage1 = tk.Text(master=frame, width = 200, height =200, padx=10, pady=10)
passage1.pack(side="left")

passage2 = tk.Text(master=frame2, width = 200, height =200, padx=10, pady=10)
passage2.pack(side="right")


def compare():
    print("Button Clicked")
    #Need to take in the text in both strings and compare for any differences
    #Also need to find out how to highligh or change color of the text
    content1 = passage1.get("1.0",'end-1c')
    content2 = passage2.get("1.0",'end-1c')
    compareStrings(content1, content2)


def compareStrings(string1, string2):
    print("Comparing Messages")
    
    for position in range(0, len(string1) ):
        if(string1[position]!=string2[position]):
            print("Different character is ", string1[position], " and ", string2[position])

    if(string1 == string2):
        print("They are equal")


compareFiles = tk.Button(root, text="Compare", padx=10, pady=5, fg="white", bg="#263D42", command=compare)
compareFiles.pack(side="bottom", pady=10)


root.mainloop()
