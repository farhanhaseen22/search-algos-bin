# 2 lists having some commom items in them
list1 = [1, 6, 7, 4, 5, 2, 3, 8, 9]
list2 = [2, 3, 4, 5, 6, 7, 8, 9, 10]

# merging the two lists
list3 = list1 + list2
print(f"List3: {list3}\n")
# removing the duplicates
list4 = list(set(list3))
print(f"List4: {list4}\n")
# sorting the list
list4.sort()
print(f"Sorted List: {list4}\n")

print("--------------------------------------------------")

# Now give 2 lists with common string items
list1 = ["a", "b", "c", "d", "e"]
list2 = ["c", "d", "e", "f", "g"]
# merging the two lists
list3 = list1 + list2
print(f"List3: {list3}\n")
# removing the duplicates
list4 = list(set(list3))
print(f"List4: {list4}\n")
# sorting the list
list5 = sorted(list4)
print(f"List5: {list5}\n")


# ===================== Fau code shudu uplood korar jonno =====================

# Function to sort a list in ascending and descending order
def sort_list(strings):
    ascending = sorted(strings)
    descending = sorted(strings, reverse=True)
    return ascending, descending

# Example usage:
strings = ["banana", "apple", "cherry", "date"]

# Get the sorted lists
ascending_order, descending_order = sort_list(strings)

print(f"Original list: {strings}")
print(f"Ascending order: {ascending_order}")
print(f"Descending order: {descending_order}")


# =====================

import tkinter as tk

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

# Create a textbox for the destination text
destination_textbox = tk.Text(root, height=10, width=40)
destination_textbox.pack(pady=10)

# Run the application
root.mainloop()
