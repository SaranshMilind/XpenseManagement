import tkinter as tk
import math

# Functions
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def equalpress():
    try:
        global expression
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set(" error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def sq_root():
    try:
        global expression
        result = str(math.sqrt(eval(expression)))
        equation.set(result)
        expression = result
    except:
        equation.set(" error ")
        expression = ""

def power():
    global expression
    expression += "**"
    equation.set(expression)

def factorial():
    try:
        global expression
        result = str(math.factorial(int(eval(expression))))
        equation.set(result)
        expression = result
    except:
        equation.set(" error ")
        expression = ""

def sin_func():
    try:
        global expression
        result = str(math.sin(math.radians(float(eval(expression)))))
        equation.set(result)
        expression = result
    except:
        equation.set(" error ")
        expression = ""

def cos_func():
    try:
        global expression
        result = str(math.cos(math.radians(float(eval(expression)))))
        equation.set(result)
        expression = result
    except:
        equation.set(" error ")
        expression = ""

def tan_func():
    try:
        global expression
        result = str(math.tan(math.radians(float(eval(expression)))))
        equation.set(result)
        expression = result
    except:
        equation.set(" error ")
        expression = ""

def log_func():
    try:
        global expression
        result = str(math.log10(eval(expression)))
        equation.set(result)
        expression = result
    except:
        equation.set(" error ")
        expression = ""

def pi_func():
    global expression
    expression += str(math.pi)
    equation.set(expression)


# Main GUI
if __name__ == "__main__":
    gui = tk.Tk()
    gui.configure(background="lightgray")
    gui.title("Scientific Calculator")
    gui.geometry("700x550")

    expression = ""
    equation = tk.StringVar()

    # Display
    expression_field = tk.Entry(gui, textvariable=equation, font=("Arial", 20), bd=10, relief="sunken", justify="right")
    expression_field.grid(columnspan=6, ipadx=8, ipady=8, padx=10, pady=10)

    # Buttons
    buttons = [
        ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
        ('sin', 1, 4), ('cos', 1, 5),

        ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
        ('tan', 2, 4), ('log', 2, 5),

        ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
        ('√', 3, 4), ('^', 3, 5),

        ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
        ('n!', 4, 4), ('π', 4, 5),
    ]

    for (text, row, col) in buttons:
        if text == "=":
            b = tk.Button(gui, text=text, fg="white", bg="green",
                          command=equalpress, height=2, width=7, font=("Arial", 14))
        elif text == "√":
            b = tk.Button(gui, text=text, bg="lightblue",
                          command=sq_root, height=2, width=7, font=("Arial", 14))
        elif text == "^":
            b = tk.Button(gui, text=text, bg="lightblue",
                          command=power, height=2, width=7, font=("Arial", 14))
        elif text == "n!":
            b = tk.Button(gui, text=text, bg="lightblue",
                          command=factorial, height=2, width=7, font=("Arial", 14))
        elif text == "sin":
            b = tk.Button(gui, text=text, bg="lightblue",
                          command=sin_func, height=2, width=7, font=("Arial", 14))
        elif text == "cos":
            b = tk.Button(gui, text=text, bg="lightblue",
                          command=cos_func, height=2, width=7, font=("Arial", 14))
        elif text == "tan":
            b = tk.Button(gui, text=text, bg="lightblue",
                          command=tan_func, height=2, width=7, font=("Arial", 14))
        elif text == "log":
            b = tk.Button(gui, text=text, bg="lightblue",
                          command=log_func, height=2, width=7, font=("Arial", 14))
        elif text == "π":
            b = tk.Button(gui, text=text, bg="lightblue",
                          command=pi_func, height=2, width=7, font=("Arial", 14))
        else:
            b = tk.Button(gui, text=text, bg="lightgray",
                          command=lambda t=text: press(t), height=2, width=7, font=("Arial", 14))
        b.grid(row=row, column=col, padx=5, pady=5)

    # Clear button
    clear_button = tk.Button(gui, text="C", fg="white", bg="red",
                             command=clear, height=2, width=46, font=("Arial", 14))
    clear_button.grid(row=5, column=0, columnspan=6, padx=5, pady=10)

    gui.mainloop()
