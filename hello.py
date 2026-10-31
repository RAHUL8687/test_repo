import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    calculator()
    def on_calculate():
        try:
            num1 = float(entry_num1.get())
            num2 = float(entry_num2.get())
            choice = operation_var.get()
            
            if choice == 'Add':
                result = add(num1, num2)
            elif choice == 'Subtract':
                result = subtract(num1, num2)
            elif choice == 'Multiply':
                result = multiply(num1, num2)
            elif choice == 'Divide':
                result = divide(num1, num2)
            else:
                messagebox.showerror("Error", "Invalid operation")
                return
            
            messagebox.showinfo("Result", f"The result is: {result}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers")

    root = tk.Tk()
    root.title("Simple Calculator")

    operation_var = tk.StringVar(value='Add')

    tk.Label(root, text="First Number:").grid(row=0, column=0)
    entry_num1 = tk.Entry(root)
    entry_num1.grid(row=0, column=1)

    tk.Label(root, text="Second Number:").grid(row=1, column=0)
    entry_num2 = tk.Entry(root)
    entry_num2.grid(row=1, column=1)

    tk.Label(root, text="Select Operation:").grid(row=2, column=0)
    tk.OptionMenu(root, operation_var, 'Add', 'Subtract', 'Multiply', 'Divide').grid(row=2, column=1)

    tk.Button(root, text="Calculate", command=on_calculate).grid(row=3, columnspan=2)

    root.mainloop()