#!/usr/bin/env python3
"""
Basic Python Calculator GUI
Performs basic arithmetic operations with a graphical interface
"""

import tkinter as tk
from tkinter import messagebox

def add(x, y):
    """Add two numbers"""
    return x + y

def subtract(x, y):
    """Subtract two numbers"""
    return x - y

def multiply(x, y):
    """Multiply two numbers"""
    return x * y

def divide(x, y):
    """Divide two numbers"""
    if y == 0:
        return "Error: Cannot divide by zero"
    return x / y

def power(x, y):
    """Raise x to the power of y"""
    return x ** y

class CalculatorApp:
    """Simple Calculator GUI Application"""
    
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Python Calculator")
        # Allow the window to be resized and maximized
        self.root.resizable(True, True)
        
        # Use root background and a centered content frame for layout
        self.root.configure(bg='black')
        self.center_frame = tk.Frame(root, bg='black')
        self.center_frame.pack(fill=tk.BOTH, expand=True)

        # Content container placed at center and sized relative to window
        self.content = tk.Frame(self.center_frame, bg='black')
        # relwidth makes the content scale with window width
        self.content.place(relx=0.5, rely=0.5, anchor='center', relwidth=0.5)
        # Make grid columns expand
        self.content.grid_columnconfigure(0, weight=1)
        self.content.grid_columnconfigure(1, weight=1)

        # Title
        title = tk.Label(self.content, text="Simple Python Calculator", font=("Arial", 16, "bold"), fg="white", bg='black')
        title.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # Input fields
        tk.Label(self.content, text="First Number:", font=("Arial", 10), fg="white", bg='black').grid(row=1, column=0, sticky='e', padx=(0,8), pady=4)
        self.num1_entry = tk.Entry(self.content, font=("Arial", 10))
        self.num1_entry.grid(row=1, column=1, sticky='ew', pady=4)

        tk.Label(self.content, text="Second Number:", font=("Arial", 10), fg="white", bg='black').grid(row=2, column=0, sticky='e', padx=(0,8), pady=4)
        self.num2_entry = tk.Entry(self.content, font=("Arial", 10))
        self.num2_entry.grid(row=2, column=1, sticky='ew', pady=4)

        # Buttons arranged in grid
        btn_add = tk.Button(self.content, text="Add (+)", command=self.calculate_add)
        btn_sub = tk.Button(self.content, text="Subtract (-)", command=self.calculate_subtract)
        btn_mul = tk.Button(self.content, text="Multiply (*)", command=self.calculate_multiply)
        btn_div = tk.Button(self.content, text="Divide (/)" , command=self.calculate_divide)
        btn_pow = tk.Button(self.content, text="Power (^)" , command=self.calculate_power)
        btn_clr = tk.Button(self.content, text="Clear", command=self.clear_inputs)

        btn_add.grid(row=3, column=0, padx=6, pady=6, sticky='ew')
        btn_sub.grid(row=3, column=1, padx=6, pady=6, sticky='ew')
        btn_mul.grid(row=4, column=0, padx=6, pady=6, sticky='ew')
        btn_div.grid(row=4, column=1, padx=6, pady=6, sticky='ew')
        btn_pow.grid(row=5, column=0, padx=6, pady=6, sticky='ew')
        btn_clr.grid(row=5, column=1, padx=6, pady=6, sticky='ew')

        # Result display
        tk.Label(self.content, text="Result:", font=("Arial", 11, "bold"), fg="white", bg='black').grid(row=6, column=0, columnspan=2, pady=(10,0))
        self.result_label = tk.Label(self.content, text="No calculation yet", font=("Arial", 14, "bold"), fg="white", bg="steelblue", padx=15, pady=15)
        self.result_label.grid(row=7, column=0, columnspan=2, pady=(6,0), sticky='ew')

        # Adjust wraplength on resize so result text wraps to content width
        self.content.bind('<Configure>', self._on_content_resize)

    def _on_content_resize(self, event):
        # Set wraplength slightly smaller than content width
        try:
            wrap = max(100, event.width - 30)
            self.result_label.config(wraplength=wrap)
        except Exception:
            pass
    
    def get_numbers(self):
        """Get and validate input numbers"""
        try:
            num1 = float(self.num1_entry.get())
            num2 = float(self.num2_entry.get())
            return num1, num2
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numeric values.")
            return None, None
    
    def display_result(self, num1, num2, operation, result):
        """Display the calculation result"""
        if isinstance(result, str) and "Error" in result:
            self.result_label.config(text=result, fg="white", bg="red")
        else:
            self.result_label.config(text=f"{num1} {operation} {num2} = {result}", fg="white", bg="darkgreen")
    
    def calculate_add(self):
        num1, num2 = self.get_numbers()
        if num1 is not None:
            result = add(num1, num2)
            self.display_result(num1, num2, "+", result)
    
    def calculate_subtract(self):
        num1, num2 = self.get_numbers()
        if num1 is not None:
            result = subtract(num1, num2)
            self.display_result(num1, num2, "-", result)
    
    def calculate_multiply(self):
        num1, num2 = self.get_numbers()
        if num1 is not None:
            result = multiply(num1, num2)
            self.display_result(num1, num2, "*", result)
    
    def calculate_divide(self):
        num1, num2 = self.get_numbers()
        if num1 is not None:
            result = divide(num1, num2)
            self.display_result(num1, num2, "/", result)
    
    def calculate_power(self):
        num1, num2 = self.get_numbers()
        if num1 is not None:
            result = power(num1, num2)
            self.display_result(num1, num2, "^", result)
    
    def clear_inputs(self):
        """Clear all input fields and results"""
        self.num1_entry.delete(0, tk.END)
        self.num2_entry.delete(0, tk.END)
        self.result_label.config(text="No calculation yet", bg="steelblue")
        self.num1_entry.focus()

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    # Set default window size and center on screen (don't maximize)
    width, height = 900, 900
    screen_w = root.winfo_screenwidth()
    screen_h = root.winfo_screenheight()
    x = (screen_w - width) // 2
    y = (screen_h - height) // 2
    root.geometry(f"{width}x{height}+{x}+{y}")
    root.mainloop()
