# Lab Activity 1: Variables and Control Flow
# Objective: Introduce variables, data types, and control flow statements in Python.

# Declare two variables, `num1` and `num2`, and assign them with integer values.
num1 = 16
num2 = 26

# Write a program that checks if `num1` is greater than `num2` and prints the result.
if num1 > num2:
  print("Number", num1, "is greater than", num2, "\n")
elif num1 < num2:
  print("Number", num2, "is greater than", num1, "\n")
else:
  print("Number", num1, "is equal to", num2, "\n")

# Use an `if-else` statement to determine if the values of `num1` and `num2` are equal or not, and print an appropriate message.
num1 = 10
num2 = 2

if num1 == num2:
  print("Number", num1, "is equal to", num2, "\n")
else:
  print("Number", num1, "is not equal to", num2, "\n")

# Prompt the user to enter a number and store it in a variable.
val = input("Enter a number: ")

# Use a loop to print all the numbers from 1 to the user-input number.
for num in range(1, int(val) + 1):
  print(num)