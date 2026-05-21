import tkinter as tk

# Create main window
root = tk.Tk()

# Window title
root.title("My First Python App")

# Window size
root.geometry("400x300")

# Label
label = tk.Label(root, text="Hello Palash!", font=("Arial", 18))
label.pack(pady=20)

# Button function
def clicked():
    label.config(text="Button Clicked!")

# Button
button = tk.Button(root, text="Click Me", command=clicked)
button.pack()

# Run application
root.mainloop()