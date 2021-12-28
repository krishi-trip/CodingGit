
#====================
#   Text Compare   ||
#====================


import tkinter as tk
from tkinter import filedialog, Text
import os
from os import path

root = tk.Tk()
root.winfo_toplevel().title("Text Editor")
root.winfo_toplevel().minsize(1200,850)

canvas = tk.Canvas(root, height=700, width=700, bg="#274E13")
canvas.pack(fill="both")

frame = tk.Frame(master=root)
frame.place(relwidth=0.3, relheight=0.5, relx=0.1, rely=0.1)

frame2 = tk.Frame(root)
frame2.place(relwidth=0.3, relheight=0.5, relx=0.6, rely=0.1)

passage1 = tk.Text(master=frame, width = 200, height =200, padx=10, pady=10)
passage1.pack(side="left")

passage2 = tk.Text(master=frame2, width = 200, height =200, padx=10, pady=10)
passage2.pack(side="right")


def compare():
    print("Button Clicked")
    #Also need to find out how to highligh or change color of the text
    content1 = passage1.get("1.0",'end-1c')
    content2 = passage2.get("1.0",'end-1c')
    compareStrings(content1, content2)


def compareStrings(string1, string2):
    print("Comparing Messages")
    
    count=0
    for position in range(0, len(string1) ):
        if(string1[position]!=string2[position]):
            print("Different character is ", string1[position], " and ", string2[position], " at index ", position)
            count+=1

    if(string1 == string2):
        print("They are equal")

    print("There are a total of ", count, " differences.")

compareFiles = tk.Button(root, text="Compare", padx=10, pady=5, fg="white", bg="#263D42", command=compare)
compareFiles.pack(side="left", pady=10)

def reset():
    content1 = passage1.delete("1.0",'end-1c')
    content2 = passage2.delete("1.0",'end-1c')

reset = tk.Button(root, text="Reset", padx=10, pady=5, fg="white", bg="#263D42", command=reset)
reset.pack(side="right", pady=10)



root.mainloop()
