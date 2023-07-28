# Lab Activity 3: Lists and Basic Algorithms
# Objective: Introduce lists, basic algorithms, and list manipulation in Python.

# Create a list of integers containing at least 10 elements.
my_list = [3, 5, 60, 34, 21, 26, 22, 70, 100, 9]

# Write a function that takes the list as input and returns the maximum and minimum values.
def min_and_max(list_input):

  max = my_list[0]
  min = my_list[0]

  for num in my_list:
    if num > max: max = num
    elif num < min: min = num

  return max, min

max, min = min_and_max(my_list)
print("Maximun:", max)
print("Minimun:", min, "\n")

# Implement a function that reverses the order of the elements in the list.
def reverse_list(list_input):
  return list_input[::-1]

print(reverse_list(my_list), "\n")

# Write a function that searches for a given value in the list and returns its index.
def get_index(list_input, val_input):
  index = list_input.index(val_input)
  return index

print(get_index(my_list, 21), "\n")

# Implement a function that takes a list of numbers and returns a new list with only the even numbers.
def even_numbers(list_input):
    new_list = []
    for num in list_input:
      if num % 2 == 0:
        new_list.append(num)
    return new_list

print(even_numbers(my_list), "\n")