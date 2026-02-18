import tkinter as tk

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = operator_var.get()

        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            result = num1 / num2

        result_label.config(text="Result: " + str(result))

    except:
        result_label.config(text="Error")

window = tk.Tk()
window.title("Simple Calculator")
window.geometry("300x250")

entry1 = tk.Entry(window)
entry1.pack()

entry2 = tk.Entry(window)
entry2.pack()

operator_var = tk.StringVar(value="+")
operator_menu = tk.OptionMenu(window, operator_var, "+", "-", "*", "/")
operator_menu.pack()


calc_button = tk.Button(window, text="Calculate", command=calculate)
calc_button.pack()


result_label = tk.Label(window, text="Result: ")
result_label.pack()

window.mainloop()
