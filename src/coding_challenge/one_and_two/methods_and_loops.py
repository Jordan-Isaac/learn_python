
FIRST_NUMBER = 110100100
SECOND_NUMBER =  1000101

# # Challenge 1 ; basic functions for mathematical operation

def add(number1: str, number2: str) -> float:
    add = number1 + number2
    return add
# print(add(FIRST_NUMBER,SECOND_NUMBER))

def subtract(number1: str, number2: str) -> float:
    sub = number1 - number2
    return sub
# print(subtract(FIRST_NUMBER,SECOND_NUMBER))

def multiply(number1: str, number2: str) -> float:
    multi = number1 * number2
    return multi
# print(multiply(FIRST_NUMBER,SECOND_NUMBER))


def divide(number1: str, number2: str) -> float:
    div = number1 / number2
    return div
# print(divide(FIRST_NUMBER,SECOND_NUMBER))

def two_dp(number: float) -> float:
    rounded_number = round(number,2)
    return rounded_number
# print(two_dp(FIRST_NUMBER))


# Challenge 2 ; booleans
def is_even(number: int) -> bool:
    return number % 2 == 0

# print(is_even(FIRST_NUMBER))
# print(is_even(SECOND_NUMBER))

# def is_member() -> bool:
#     """Checks if given string is a member of a given list of strings.
    
#     Takes two parameters, first the string to check and second the list of
#     strings to inspect.
    
#     :return bool: True if member, False if not.
#     """

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

def count_vowels(string: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0
    for character in string:
        if character in vowels:
            count += 1
    return count
# print("Number of vowels in TEST_STRING:", count_vowels(string1))
# print("Number of vowels in TEST_STRING_TWO:", count_vowels(string2))

def count_punctuation(string: str) -> int:
    punc = ",.?!():;"
    count = 0
    for character in string:
        if character in punc:
            count += 1
    return count
# print("Number of non alphabetical characters in TEST_STRING:", count_punctuation(string1))
# print("Number of non alphabetical characters in TEST_STRING_TWO:", count_punctuation(string2))



def count_uppercase(string: str) -> int:
    count = 0
    for character in string:
        if character.isupper():
            count += 1
    return count
# print("Number of uppercase characters in TEST_STRING:", count_uppercase(string1))
# print("Number of uppercase characters in TEST_STRING_TWO:", count_uppercase(string2))

def count_lowercase(string: str) -> int:
    count = 0
    for character in string:
        if character.islower():
            count += 1
    return count
# print("Number of lowercase characters in TEST_STRING:", count_lowercase(string1))
# print("Number of lowercase characters in TEST_STRING_TWO:", count_lowercase(string2))

def as_lowercase(string) -> str:
    as_lower = string.lower()
    return as_lower
# print (as_lowercase(TEST_STRING))
# print (as_lowercase(TEST_STRING_TWO))

def as_upper_lower(string: str) -> str:
    result = ""
    for i, character in enumerate(string):
        if i % 2 == 0:
            result += character.upper()
        else:
            result += character.lower()
    return result
#print (as_upper_lower(TEST_STRING_TWO))

def get_first_word(string: str) -> str:
    words = string.split()
    if words:
        return words[0]
    else:
        return None
#print (get_first_word(TEST_STRING_TWO))

# # Bonus round!
def get_word_by_index(word: str) -> str:
    string = TEST_STRING_TWO
    try:
        index = string.index(word)
        print (f"The word '{word}' is found at index {index}.")
    except ValueError:
        print(f"The word '{word}' is not found in this string.")
# print(get_word_by_index("Lorem"))  
    

# # # Challenge 4 ; strings, lists, and booleans
# ROCK_PAPER_SCISSORS = ["rock", "paper", "scissors"]
# from random import randint



# def rps_win_or_lost(player_choice: str) -> bool:
#     cpu_choice = get_cpu_tactic()
#     if player_choice == cpu_choice:
#         print("It's a tie.")
#         return None

#     elif (player_choice == "rock" and cpu_choice == "scissors") or \
#          (player_choice == "scissors" and cpu_choice == "paper") or \
#          (player_choice == "paper" and cpu_choice == "rock"):
#         print (f"The player wins with {player_choice}!")
#         return True
#     else:
#         print(f"The computer wins with {cpu_choice}! Too bad.")
#         return False

# def get_player_choice() -> str:
#     while True:
#         player_choice = input("Enter rock, paper or scissors:").lower()
#         if player_choice in ROCK_PAPER_SCISSORS:
#             return player_choice
#         else:
#             print("Invalid option.")

# def get_cpu_tactic() -> str:
#     random_index = randint(0,2)
#     return ROCK_PAPER_SCISSORS[random_index]


# def main():
#     print("Rock Paper Scissors!")
#     while True:
#         player_choice = get_player_choice()
#         result = rps_win_or_lost(player_choice)
#         if result is None:
#             print("Play again!")
#         else:
#             break
# if __name__ == "__main__":
#     main()
  
# Challenge 5 ; Prime Number Detector :
# create a method which takes one integer as input and returns True or False
# depending on whether or not that number is a prime number.

# HINT ; use the modulus operator :: '%' (if )
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(1, 100):
    if is_prime(i):
        print(i, "is a prime number")