# print("/////**************** CALCULATOR ****************/////")
# print("Please sellect the operator which you want and then you have to calculate this & for exit you have to type the -1 in the operator's place .")


# while True:
#     number1=int(input("Enter the first number : "))
#     number2=int(input("Enter the second number : "))
#     n=input("Enter the operation which you want to do : ")
#     if n=="+":
#         print(number1+number2)
#     elif n=="-":
#         print(number1-number2)
#     elif n=="*":
#         print(number1*number2)
#     elif n=="/":
#         print(number1/number2)
#     elif n=="//":
#         print(number1//number2)
#     elif n=="%":
#         print(number1%number2)
#     elif n=="-1":
#         exit()

import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()

        if operation == "+":
            result.set(num1 + num2)
        elif operation == "-":
            result.set(num1 - num2)
        elif operation == "*":
            result.set(num1 * num2)
        elif operation == "/":
            result.set(num1 / num2)
        elif operation == "//":
            result.set(num1 // num2)
        elif operation == "%":
            result.set(num1 % num2)
        elif operation == "-1":
            root.destroy()
        else:
            messagebox.showerror("Error", "Invalid operation selected!")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero!")

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x400")
root.configure(bg="#1e1e2f")

# Labels
label1 = tk.Label(root, text="Enter first number:", bg="#1e1e2f", fg="white", font=("Arial", 12))
label1.pack(pady=5)
entry1 = tk.Entry(root, font=("Arial", 12), bg="#f0f0f0", fg="black")
entry1.pack(pady=5)

label2 = tk.Label(root, text="Enter second number:", bg="#1e1e2f", fg="white", font=("Arial", 12))
label2.pack(pady=5)
entry2 = tk.Entry(root, font=("Arial", 12), bg="#f0f0f0", fg="black")
entry2.pack(pady=5)

label3 = tk.Label(root, text="Select Operation:", bg="#1e1e2f", fg="white", font=("Arial", 12))
label3.pack(pady=5)

# Dropdown for operations
operation_var = tk.StringVar()
operation_var.set("+")
operations_menu = tk.OptionMenu(root, operation_var, "+", "-", "*", "/", "//", "%", "-1")
operations_menu.config(font=("Arial", 12), bg="#ffcc00", fg="black")
operations_menu.pack(pady=5)

# Button
calc_button = tk.Button(root, text="Calculate", command=calculate, font=("Arial", 12, "bold"), bg="#008cba", fg="white", padx=10, pady=5)
calc_button.pack(pady=10)

# Result Display
result = tk.StringVar()
result_label = tk.Label(root, textvariable=result, font=("Arial", 14, "bold"), bg="#1e1e2f", fg="#ffcc00")
result_label.pack(pady=10)

# Run application
root.mainloop()
