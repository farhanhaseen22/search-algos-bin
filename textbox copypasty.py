import tkinter as tk


# ////////// Prototype pasting function ////////////////

def paste_text(destination):
    if copied_text:
        destination.delete("1.0", tk.END)
        destination.insert(tk.END, copied_text)

# //////////////////////////

def copy_text():
    # Get the text from the source textbox
    text = source_textbox.get("1.0", tk.END)
    # Set the text to the destination textbox
    destination_textbox.delete("1.0", tk.END)
    destination_textbox.insert(tk.END, text)

# Create the main window
root = tk.Tk()
root.title("Text Copier")

# Create a textbox for the source text
source_textbox = tk.Text(root, height=10, width=40)
source_textbox.pack(pady=10)

# Create a button that copies the text
copy_button = tk.Button(root, text="Copy Text", command=copy_text)
copy_button.pack(pady=10)

# Extra button that pastes the given text
copy_button = tk.Button(root, text="Paste Text", command=paste_text)
copy_button.pack(pady=15)

# Create a textbox for the destination text
destination_textbox = tk.Text(root, height=10, width=40)
destination_textbox.pack(pady=10)

# Run the application
root.mainloop()

