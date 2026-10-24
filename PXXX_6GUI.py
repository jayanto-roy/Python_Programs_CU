
# Practical 6: Display Text Using Tkinter

import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Text Display Application")
root.geometry("400x250")

# Function to display entered text
def display_text():
    text = entry.get()
    label.config(text=text)

# Create a text box
entry = tk.Entry(root, width=30)
entry.pack(pady=20)

# Create a button
button = tk.Button(
    root,
    text="Display Text",
    command=display_text
)
button.pack(pady=10)

# Create a label
label = tk.Label(root, text="Your text will appear here")
label.pack(pady=20)

# Run the application
root.mainloop()
