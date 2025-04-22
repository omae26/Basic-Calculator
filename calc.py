#19/04/2025
# Basic calculator
# that can add, subtract, multiply and divide
# We will use the logic of getting inputs from the user to perform the operations

# First, we will store the users input in variables
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
results1 = num1 + num2
print(results1)
# In the case, the result turns out to be 58 (when num1=5 & num2=8),
# since whenever we get an input from the user, by default it is a string, so we need to convert it to an integer or float.

# So we will use the int() function to convert the string to an integer, whole number.
# We will also use the float() function to convert the string to a float, decimal number.
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
results2 = float(num1) + float(num2)
print(results2)

# Now we can perform the operations of addition, subtraction, multiplication and division.
# We will use the input() function to get the operation from the user.
# Subraction
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
results3 = float(num1) - float(num2)
print(results3)


