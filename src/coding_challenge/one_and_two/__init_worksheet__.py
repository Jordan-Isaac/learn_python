# this is just the worksheet I used to work on everything - the finished products are seperated

def add() -> float:
    """Add two numbers."""

def subtract() -> float:
    """Subtract two numbers."""

def multiply() -> float:
   """Multiply two numbers."""

def divide() -> float:
    """Divide two numbers."""

def two_dp() -> float:
    """Rounds numerical types to two decimal places."""

FIRST_NUMBER = 110100100
SECOND_NUMBER =  1000101

print (add(FIRST_NUMBER+SECOND_NUMBER))

#// FIXED
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
print (f"times'd together: {multiply_result}")

# Divide
division_result = divide(FIRST_NUMBER, SECOND_NUMBER)
rounded_division_result = two_dp(division_result)
print (f"divided {division_result}")
print (f"divided to 2dp {rounded_division_result}")

#//

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

# Example usage for is_even
number_to_check = 10
print(f"{number_to_check} is even: {is_even(number_to_check)}")

# Example usage for is_member
word_to_check = "apple"
word_list = ["banana", "orange", "apple", "grape"]
print(f"{word_to_check} is a member: {is_member(word_to_check, word_list)}")

# Your existing code for calculations
FIRST_NUMBER = 110100100
SECOND_NUMBER = 1000101

result = add(FIRST_NUMBER, SECOND_NUMBER)
rounded_result = two_dp(result)

# Output the result of addition and check if it's even
print(f"Addition Result: {rounded_result}")
print(f"Is the result even?: {is_even(int(rounded_result))}")

# Output the result of subtraction and check if it's even
subtraction_result = subtract(FIRST_NUMBER, SECOND_NUMBER)
print(f"Subtraction Result: {subtraction_result}")
print(f"Is the result even?: {is_even(int(subtraction_result))}")

# Output the result of multiplication and check if it's even
multiply_result = multiply(FIRST_NUMBER, SECOND_NUMBER)
print(f"Multiplication Result: {multiply_result}")
print(f"Is the result even?: {is_even(int(multiply_result))}")

# Output the result of division and check if it's even
division_result = divide(FIRST_NUMBER, SECOND_NUMBER)
rounded_division_result = two_dp(division_result)
print(f"Division Result: {rounded_division_result}")
print(f"Is the result even?: {is_even(int(rounded_division_result))}")
    
# Challenge 3 ;  string manipulation
TEST_STRING = ("ASLIKJFBA:EODGUBAS:ODIGBNSD:LKJGBNV IPWUEHTF)*"
             "(A&DGB:SOIJFDBG:SMD)OPIAHDFws98dgfy")

TEST_STRING_TWO = (
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, "
    "sed do eiusmod tempor incididunt ut labore et dolore magna"
    " aliqua. Ut enim ad minim veniam, quis nostrud "
    "exercitation ullamco laboris nisi ut aliquip ex ea commodo"
    " consequat. Duis aute irure dolor in reprehenderit in"
    " voluptate velit esse cillum dolore eu fugiat nulla "
    " pariatur. Excepteur sint occaecat cupidatat non proident,"
    " sunt in culpa qui officia deserunt mollit anim id est"
    " laborum."
    )

def count_vowels(test_string: str) -> int:
    """Count vowels in a string."""
    vowels = "aeiouAEIOU"
    return sum(char in vowels for char in test_string)

def count_punctuation(test_string: str) -> int:
    """Count non-alphabetical characters in a string."""
    return sum(not char.isalnum() and not char.isspace() for char in test_string)

def count_uppercase(test_string: str) -> int:
    """Count uppercase characters in a string."""
    return sum(char.isupper() for char in test_string)

def count_lowercase(test_string: str) -> int:
    """Count lowercase characters in a string."""
    return sum(char.islower() for char in test_string)

def as_lowercase(test_string: str) -> str:
    """Returns a given string in lowercase."""
    return test_string.lower()

def as_upper_lower(test_string: str) -> str:
    """Returns a string where each character alternates uppercase & lowercase."""
    return ''.join(c.upper() if i % 2 == 0 else c.lower() for i, c in enumerate(test_string))

def get_first_word(test_string: str) -> str:
    """Gets the first word in a string."""
    words = test_string.split()
    return words[0] if words else ""

# Bonus round!
def get_word_by_index(test_string: str, index: int) -> str:
    """Gets the nth word in a string."""
    words = test_string.split()
    return words[index] if 0 <= index < len(words) else ""

# Testing the functions with the provided test strings
print(count_vowels(TEST_STRING))
print(count_punctuation(TEST_STRING))
print(count_uppercase(TEST_STRING))
print(count_lowercase(TEST_STRING))
print(as_lowercase(TEST_STRING))
print(as_upper_lower(TEST_STRING))
print(get_first_word(TEST_STRING))
print(get_word_by_index(TEST_STRING_TWO, 5))
#For test string 2
print(count_vowels(TEST_STRING_TWO))
print(count_punctuation(TEST_STRING_TWO))
print(count_uppercase(TEST_STRING_TWO))
print(count_lowercase(TEST_STRING_TWO))
print(as_lowercase(TEST_STRING_TWO))
print(as_upper_lower(TEST_STRING_TWO))
print(get_first_word(TEST_STRING_TWO))
print(get_word_by_index(TEST_STRING_TWO, 5))