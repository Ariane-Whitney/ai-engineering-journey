# Day 6 - Student Manager with JSON Storage
# Concepts: Dictionaries, JSON, File Handling, GUI

import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "students.json"

# ---------------- LOAD DATA ---------------- #

if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r") as file:
        students = json.load(file)
else:
    students = {}

# ---------------- SAVE FUNCTION ---------------- #

def save_data():
    with open(FILE_NAME, "w") as file:
        json.dump(students, file)

# ---------------- FUNCTIONS ---------------- #

def add_student():
    name = name_entry.get()
    grade = grade_entry.get()

    if name and grade:
        students[name] = grade
        save_data()
        update_listbox()
        name_entry.delete(0, tk.END)
        grade_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Enter both name and grade.")

def delete_student():
    try:
        selected = listbox.get(listbox.curselection())
        name = selected.split(" - ")[0]
        del students[name]
        save_data()
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Select a student to delete.")

def update_listbox():
    listbox.delete(0, tk.END)
    for name, grade in students.items():
        listbox.insert(tk.END, f"{name} - {grade}")

# ---------------- GUI ---------------- #

window = tk.Tk()
window.title("Student Manager - JSON Version")
window.geometry("450x400")

title = tk.Label(window, text="Student Record Manager (Saved)", font=("Arial", 14))
title.pack(pady=10)

tk.Label(window, text="Student Name:").pack()
name_entry = tk.Entry(window, width=30)
name_entry.pack(pady=5)

tk.Label(window, text="Grade:").pack()
grade_entry = tk.Entry(window, width=30)
grade_entry.pack(pady=5)

tk.Button(window, text="Add Student", width=20, command=add_student).pack(pady=5)

listbox = tk.Listbox(window, width=40, height=10)
listbox.pack(pady=10)

tk.Button(window, text="Delete Student", width=20, command=delete_student).pack(pady=5)

update_listbox()

window.mainloop()