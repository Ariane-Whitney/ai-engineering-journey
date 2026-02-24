# Day 5 - Student Manager (GUI)
# Concepts: Dictionaries, Tkinter, Data Storage

import tkinter as tk
from tkinter import messagebox

students = {}  # dictionary to store student data

# ---------------- FUNCTIONS ---------------- #

def add_student():
    name = name_entry.get()
    grade = grade_entry.get()

    if name and grade:
        students[name] = grade
        update_listbox()
        name_entry.delete(0, tk.END)
        grade_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter both name and grade.")

def delete_student():
    try:
        selected = listbox.get(listbox.curselection())
        name = selected.split(" - ")[0]
        del students[name]
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Select a student to delete.")

def update_listbox():
    listbox.delete(0, tk.END)
    for name, grade in students.items():
        listbox.insert(tk.END, f"{name} - {grade}")

# ---------------- WINDOW ---------------- #

window = tk.Tk()
window.title("Student Manager")
window.geometry("450x400")

title = tk.Label(window, text="Student Record Manager", font=("Arial", 14))
title.pack(pady=10)

name_label = tk.Label(window, text="Student Name:")
name_label.pack()

name_entry = tk.Entry(window, width=30)
name_entry.pack(pady=5)

grade_label = tk.Label(window, text="Grade:")
grade_label.pack()

grade_entry = tk.Entry(window, width=30)
grade_entry.pack(pady=5)

add_button = tk.Button(window, text="Add Student", width=20, command=add_student)
add_button.pack(pady=5)

listbox = tk.Listbox(window, width=40, height=10)
listbox.pack(pady=10)

delete_button = tk.Button(window, text="Delete Student", width=20, command=delete_student)
delete_button.pack(pady=5)

window.mainloop()