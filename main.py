import tkinter as tk

# Function to perform word division
def word_divider():
    input_text = input_entry.get()
    divider = divider_entry.get()
    words = input_text.split()
    divided_text = divider.join(words)
    result_label.config(text=divided_text)

# Create the main window
window = tk.Tk()
window.title("Word Divider GUI")

# Create and set up GUI elements
input_label = tk.Label(window, text="Enter a sentence:")
input_label.pack()
input_entry = tk.Entry(window)
input_entry.pack()

divider_label = tk.Label(window, text="Divider character:")
divider_label.pack()
divider_entry = tk.Entry(window)
divider_entry.pack()

divide_button = tk.Button(window, text="Divide", command=word_divider)
divide_button.pack()

result_label = tk.Label(window, text="")
result_label.pack()
window.mainloop()