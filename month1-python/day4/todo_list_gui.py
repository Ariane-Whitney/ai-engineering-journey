import tkinter as tk
from tkinter import messagebox

tasks = []

# ---------------- FUNCTIONS ---------------- #

def add_task():
    task = entry.get()
    if task:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        tasks.pop(selected_index)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# ---------------- WINDOW SETUP ---------------- #

window = tk.Tk()
window.title("To-Do List App")
window.geometry("400x400")

# Entry field
entry = tk.Entry(window, width=30)
entry.pack(pady=10)

# Add button
add_button = tk.Button(window, text="Add Task", width=15, command=add_task)
add_button.pack(pady=5)

# Task list display
listbox = tk.Listbox(window, width=40, height=10)
listbox.pack(pady=10)

# Delete button
delete_button = tk.Button(window, text="Delete Task", width=15, command=delete_task)
delete_button.pack(pady=5)

# Run app
window.mainloop()