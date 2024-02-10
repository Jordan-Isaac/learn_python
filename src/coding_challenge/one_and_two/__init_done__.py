def add(x: float, y: float) -> float:
    """Add two numbers."""
    return x + y

def subtract(x: float, y: float) -> float:
    """Subtract two numbers."""
    return x - y

def multiply(x: float, y: float) -> float:
    """Multiply two numbers."""
    return x * y

def divide(x: float, y: float) -> float:
    """Divide two numbers."""
    if y != 0:
        return x / y
    else:
        raise ValueError("You can't divide by 0 you donut")

def two_dp(number: float) -> float:
    """Rounds numerical types to two decimal places."""
    return round(number, 2)

FIRST_NUMBER = 110100100
SECOND_NUMBER = 1000101

result = add(FIRST_NUMBER, SECOND_NUMBER)
rounded_result = two_dp(result)

print(rounded_result)

# Addition
addition_result = add(FIRST_NUMBER, SECOND_NUMBER)
print(f"add: {addition_result}")

# Subtraction
subtraction_result = subtract(FIRST_NUMBER, SECOND_NUMBER)
print(f"subtract: {subtraction_result}")

# Multiply
multiply_result = multiply(FIRST_NUMBER, SECOND_NUMBER)
print (f"multiply: {multiply_result}")

# Divide
division_result = divide(FIRST_NUMBER, SECOND_NUMBER)
rounded_division_result = two_dp(division_result)
print (f"divided {division_result}")
print (f"divided to 2dp {rounded_division_result}")

# Challenge 2 ; booleans
def is_even(number: int) -> bool:
    """Checks if integer is even or odd.
    
    :return bool: True if even, False if odd.
    """
    return number % 2 == 0

def is_member() -> bool:
    """Checks if given string is a member of a given list of strings.
    
    Takes two parameters, first the string to check and second the list of
    strings to inspect.
    
    :return bool: True if member, False if not.
    """
    return check_string in string_list

# Previous codes with bolted on check if number is odd or even

# addition and even check
print(f"add: {rounded_result}")
print(f"even?: {is_even(int(rounded_result))}")

# subtraction and even check
subtraction_result = subtract(FIRST_NUMBER, SECOND_NUMBER)
print(f"subtract: {subtraction_result}")
print(f"even?: {is_even(int(subtraction_result))}")

# multiply and even check
multiply_result = multiply(FIRST_NUMBER, SECOND_NUMBER)
print(f"multiply: {multiply_result}")
print(f"even?: {is_even(int(multiply_result))}")

# division and even check
division_result = divide(FIRST_NUMBER, SECOND_NUMBER)
rounded_division_result = two_dp(division_result)
print (f"divided {division_result}")
print(f"divided to 2dp: {rounded_division_result}")
print(f"even?: {is_even(int(rounded_division_result))}")