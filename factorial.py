# Sharon Gibbons, 06-04-2018
# Factorial function
# https://en.wikipedia.org/wiki/Factorial

# Python function that finds the factorial of a single input/argument.

# defines function
def factorial(x):
    """This function returns the factorial of a single input/argument."""

    # check if input value is negative or positive
    if x < 0:
        return print("Factorials do not exist for negative numbers.")
    else:
        y = 1
        for i in range(1, x + 1):
            y = y * i
        return y

# requests input from user
x = int(input("Please enter an integer:"))

# formats output string with variables and expressions 
print(f'The factorial of {x} is {factorial(x)}.')

# function tests 
print(f'The factorial of 5 is {factorial(5)}.')
print(f'The factorial of 7 is {factorial(7)}.')
print(f'The factorial of 10 is {factorial(10)}.')
