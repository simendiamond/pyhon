import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.geometry("400x400")
root.rowconfigure((0,1,2),weight=1,uniform="a")
root.columnconfigure((0,1,2),weight=1,uniform="a")
tk.Button(root, text="button1", bg="red").grid(row=1, column=1,sticky="news")

tk.Button(root, text="s2", bg="red").grid(row=2, column=2,sticky="news")

tk.Button(root, text="s3", bg="red").grid(row=2, column=2,sticky="news")

tk.Button(root, text="s4", bg="red").grid(row=2, column=0,sticky="news")

tk.Button(root, text="s5", bg="red").grid(row=1, column=1,sticky="news")

root.mainloop()
