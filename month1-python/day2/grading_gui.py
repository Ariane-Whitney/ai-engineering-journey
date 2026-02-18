import tkinter as tk
from tkinter import messagebox


def calculate_grade():
    try:
        score = int(entry.get())

        if score < 0 or score > 100:
            result_label.config(text="Invalid score (0-100 only)")
        elif score >= 90:
            result_label.config(text="Grade: A")
        elif score >= 80:
            result_label.config(text="Grade: B")
        elif score >= 70:
            result_label.config(text="Grade: C")
        elif score >= 60:
            result_label.config(text="Grade: D")
        else:
            result_label.config(text="Grade: F")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

window = tk.Tk()
window.title("Smart Grading System")
window.geometry("300x200")

title_label = tk.Label(window, text="Enter Score (0-100)", font=("Arial", 12))
title_label.pack(pady=10)

entry = tk.Entry(window)
entry.pack(pady=5)


grade_button = tk.Button(window, text="Calculate Grade", command=calculate_grade)
grade_button.pack(pady=10)


result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)


window.mainloop()
