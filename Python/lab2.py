# Lab Activity 2: Functions and File Handling
# Objective: Introduce functions and basic file handling operations in Python.

# Write a function that takes two parameters, `num1` and `num2`, and returns their sum.
def sum_nums(num1, num2):
  return num1 + num2

print(sum_nums(3,6), "\n")

# Create a text file named "numbers.txt" and write a few numbers, each on a new line.
with open("numbers.txt", "w") as file:
  for num in range(8):
    file.write(str(num) + "\n")


# Write a function that reads the numbers from the file and calculates their average.
def get_average(file_name):
  sum_numbers = 0
  total_lines = 0

  with open(file_name, "r") as file:
    for line in file:
      num = int(line)
      sum_numbers += num
      total_lines += 1

  if total_lines > 0:
    avg = sum_numbers / total_lines
    return avg
  else:
    return None

print(get_average("numbers.txt"))

# Implement a function that takes a string as input and writes it to the end of the "numbers.txt" file.
def append_input(file_name, str_input):
  with open(file_name, "a") as file:
    file.write(str_input + "\n")

append_input("numbers.txt", "Estef")

# Call the functions and print the results.