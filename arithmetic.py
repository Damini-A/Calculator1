"""Math functions for calculator."""

# Errors
# "Those aren't numbers" message when no space between first two numbers..? + 12
# "Not enough inputs" message when no space between + and proceeding numbers +12
# Prints 10 every time regardless of which numbers are used
# Error message "enter operator followed by two ints" when we have +1 2
# If input is not a number or symbol then it says "not enough inputs"

# num1 = int(input("Enter a first number: "))
# num2 = int(input("Enter a second number: "))

def add(num1, num2):
    """Return the sum of the two inputs."""

    addition = num1 + num2
    return addition
    # return 5


def subtract(num1, num2):
    """Return the second number subtracted from the first."""
    subtraction = num1 - num2
    return subtraction

def multiply(num1, num2):
    """Multiply the two inputs together."""
    multiplication = num1 * num2
    return multiplication


def divide(num1, num2):
    """Divide the first input by the second and return the result."""
    division = num1/num2
    return division

def square(num1):
    """Return the square of the input."""
    square_num = num1**2
    return square_num

def cube(num1):
    """Return the cube of the input."""
    cube_num = num1**3
    return cube_num

def power(num1, num2):
    """Raise num1 to the power of num2 and return the value."""
    power_num = num1 ** num2
    return power_num


def mod(num1, num2):
    """Return the remainder of num1 / num2."""
    modulo_nums = num1 % num2
    return modulo_nums
print(add(2,2))
print(subtract(2,2))
print(multiply(2,3))
print(divide(3,2))
print(square(2))
print(power(2, 3))
print(cube(2))