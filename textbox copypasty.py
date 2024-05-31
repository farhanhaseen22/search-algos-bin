import tkinter as tk


def copy_text():
    global copied_text
    # Get the text from the source textbox
    copied_text = source_textbox.get("1.0", tk.END)

def paste_text(destination):
    if copied_text:
        destination.delete("1.0", tk.END)
        destination.insert(tk.END, copied_text)


# Create the main window
root = tk.Tk()
root.title("Text Copier")

# Variable to hold the copied text
copied_text = ""

# Create a textbox for the source text
source_textbox = tk.Text(root, height=10, width=40)
source_textbox.pack(pady=10)

# Create a button that copies the text
copy_button = tk.Button(root, text="Copy Text", command=copy_text)
copy_button.pack(pady=10)

# Create two destination textboxes
destination_textbox1 = tk.Text(root, height=10, width=40)
destination_textbox1.pack(pady=10)

destination_textbox2 = tk.Text(root, height=10, width=40)
destination_textbox2.pack(pady=10)

# Create buttons to paste the text into either textbox
paste_button1 = tk.Button(root, text="Paste to Textbox 1", command=lambda: paste_text(destination_textbox1))
paste_button1.pack(pady=5)

paste_button2 = tk.Button(root, text="Paste to Textbox 2", command=lambda: paste_text(destination_textbox2))
paste_button2.pack(pady=5)


root.mainloop()
