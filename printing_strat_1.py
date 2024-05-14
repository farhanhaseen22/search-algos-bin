
import time

start = time.time()

for i in range(1, 6):
  # for k in range(1, 6):
    # print(f"br{i} size{k}")
  print(f"br{i} size{i}")

end = time.time()
print(f"Using regular code, we get: {end - start}")

# #########################################################################

start = time.time()

def descending_numbers(input_str):
  # Split the input string into branch and size
  branch, size = input_str.split()

  # Split size into characters
  size_chars = list(size)

  # Extract numbers from size_chars
  numbers = [int(char) for char in size_chars if char.isdigit()]

  # Sort the numbers in descending order
  numbers.sort(reverse=True)

  # Replace the numbers in size_chars with sorted numbers
  index = 0
  for i, char in enumerate(size_chars):
    if char.isdigit():
      size_chars[i] = str(numbers[index])
      index += 1

  # Reconstruct the size string
  sorted_size = ''.join(size_chars)

  return f"{branch} {sorted_size}"

# Generate input strings from "br1 size1" to "br5 size5"
inputs = [f"br{i} size{i}" for i in range(1, 6)]

# Process each input and print the result
for input_str in inputs:
  result = descending_numbers(input_str)
  print(result)

end = time.time()
print(f"Using ChatGPT's code, we get: {end - start}")
