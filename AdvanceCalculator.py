import tkinter as tk
from tkinter import messagebox
import math

def calculate(operation):
    try:
        num1 = float(entry.get())
        num2 = float(entry2.get()) if entry2.get() else None

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
        elif operation == "x^y":
            result.set(num1 ** num2)
        elif operation == "√x":
            result.set(math.sqrt(num1))
        elif operation == "log(x)":
            result.set(math.log10(num1))
        elif operation == "ln(x)":
            result.set(math.log(num1))
        elif operation == "sin(x)":
            result.set(math.sin(math.radians(num1)))
        elif operation == "cos(x)":
            result.set(math.cos(math.radians(num1)))
        elif operation == "tan(x)":
            result.set(math.tan(math.radians(num1)))
        elif operation == "C":
            entry.delete(0, tk.END)
            entry2.delete(0, tk.END)
            result.set("")
        elif operation == "M+":
            memory.set(result.get())  # Store in memory
        elif operation == "MR":
            entry.delete(0, tk.END)
            entry.insert(0, memory.get())  # Recall memory value
        elif operation == "MC":
            memory.set("")  # Clear memory
        elif operation == "Exit":
            root.destroy()
        else:
            messagebox.showerror("Error", "Invalid operation selected!")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers!")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero!")

# Create main window
root = tk.Tk()
root.title("Advanced Calculator")
root.geometry("400x600")
root.configure(bg="#222831")

# Main Frames
display_frame = tk.Frame(root, bg="#222831", padx=10, pady=5)
display_frame.pack(fill="both")

memory_frame = tk.Frame(root, bg="#222831", padx=10, pady=5)
memory_frame.pack(fill="both")

button_frame = tk.Frame(root, bg="#222831")
button_frame.pack(fill="both", expand=True)

# Display Section
result = tk.StringVar()
display_label = tk.Label(display_frame, textvariable=result, font=("Arial", 18, "bold"), bg="#393E46", fg="white", bd=10, relief="ridge", width=20, anchor="e")
display_label.pack(pady=5)

entry = tk.Entry(display_frame, font=("Arial", 14), bg="#EEEEEE", fg="black", bd=5, relief="ridge", justify="left")
entry.pack(pady=5, fill="both")

entry2 = tk.Entry(display_frame, font=("Arial", 14), bg="#EEEEEE", fg="black", bd=5, relief="ridge", justify="left")
entry2.pack(pady=5, fill="both")

# Memory Section
memory = tk.StringVar()
memory_label = tk.Label(memory_frame, text="Memory:", font=("Arial", 12), bg="#222831", fg="white")
memory_label.grid(row=0, column=0, sticky="w", pady=5)

mem_display = tk.Label(memory_frame, textvariable=memory, font=("Arial", 12, "bold"), bg="#393E46", fg="#00ff00", bd=5, relief="ridge", width=15, anchor="e")
mem_display.grid(row=0, column=1, pady=5, padx=10)

# Button Grid
operations = [
    ["7", "8", "9", "+"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "*"],
    ["0", "C", "=", "/"],
    ["x^y", "√x", "log(x)", "%"],
    ["ln(x)", "sin(x)", "cos(x)", "tan(x)"],
    ["//", "M+", "MR", "MC"],
    ["Exit"]
]

for row_idx, row in enumerate(operations):
    button_frame.grid_rowconfigure(row_idx, weight=1)  # Allow row expansion
    for col_idx, op in enumerate(row):
        button_frame.grid_columnconfigure(col_idx, weight=1)  # Allow column expansion
        btn = tk.Button(
            button_frame, text=op, command=lambda op=op: calculate(op) if op != "=" else None,
            font=("Arial", 14, "bold"),
            bg="#00ADB5" if op not in ["=", "Exit", "C"] else ("#FF5722" if op == "C" else "#D32F2F"),
            fg="white", width=5, height=2, relief="raised", bd=3
        )
        btn.grid(row=row_idx, column=col_idx, padx=3, pady=3, sticky="nsew")  # Stretch buttons

# Run application
root.mainloop()


