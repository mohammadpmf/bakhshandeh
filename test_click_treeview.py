import tkinter as tk
from tkinter import ttk

def OnDoubleClick(event):
    item = tree.selection()[0]
    print("you clicked on", tree.item(item,"text"))

root = tk.Tk()
tree = ttk.Treeview()
tree.pack()
for i in range(10):
    tree.insert("", "end", text=f"Item {i}")
tree.bind("<Double-1>", OnDoubleClick)
root.mainloop()
