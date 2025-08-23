import tkinter as tk

def click(event):
    global expression
    text = event.widget.cget("text")
    if text == "=":
        try:
            expression = expression.replace(":", "/").replace("x", "*")
            result = eval(expression)
            input_var.set(result)
            expression = str(result)
        except Exception as e:
            input_var.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        input_var.set("")
    else:
        expression += text
        input_var.set(expression)

# Initialize main window
root = tk.Tk()
root.title("Calculator")
root.geometry("400x450")
root.resizable(False, False)

expression = ""
input_var = tk.StringVar()

# Entry widget for display
entry = tk.Entry(root, textvar=input_var, font=("Arial", 20), justify="right", bd=8, relief=tk.SUNKEN)
entry.pack(fill=tk.BOTH, ipadx=8, pady=5, padx=5)

# Button frame
button_frame = tk.Frame(root)
button_frame.pack()

# Button layout
buttons = [
    "7", "8", "9", ":",
    "4", "5", "6", "x",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

colors = {
    "C": "#ff7875",  # Red for clear button
    "=": "#52c41a",  # Green for equals button
    ":": "#91d5ff",  # Blue for division
    "x": "#91d5ff",  # Blue for multiplication
    "+": "#ffd666",  # Yellow for addition
    "-": "#ffd666",  # Yellow for subtraction
}

row, col = 0, 0
for button in buttons:
    btn_color = colors.get(button, "#ffffff")  # Default white for other buttons
    btn = tk.Button(button_frame, text=button, font=("Arial", 18), width=5, height=2, bg=btn_color, fg="#000000")
    btn.grid(row=row, column=col, padx=10, pady=10)
    btn.bind("<Button-1>", click)
    col += 1
    if col > 3:
        col = 0
        row += 1

# Run the application
root.mainloop()
