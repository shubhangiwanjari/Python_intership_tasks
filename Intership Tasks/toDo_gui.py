import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected_task = listbox.curselection()[0]
        listbox.delete(selected_task)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# GUI setup
root = tk.Tk()
root.title("To-Do List App")

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=40, height=10, selectmode=tk.SINGLE)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

entry = tk.Entry(root, width=40)
entry.pack(pady=5)

button_frame = tk.Frame(root)
button_frame.pack(pady=5)

add_btn = tk.Button(button_frame, text="Add Task", command=add_task)
add_btn.grid(row=0, column=0, padx=5)

del_btn = tk.Button(button_frame, text="Delete Task", command=delete_task)
del_btn.grid(row=0, column=1, padx=5)

root.mainloop()
