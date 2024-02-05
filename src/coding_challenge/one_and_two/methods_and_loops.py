"""The first coding challenge.


This coding challenge should introduce you to a fair amount of thinking and
problem solving.

Challenge 2.5 and Challenge 4 are harder than the rest, simply because they are
more complex and require more moving parts.

Note: as this is the first challenge; code style won't be strictly enforced.
"""

FIRST_NUMBER = 110100100
SECOND_NUMBER =  1000101

# Challenge 1 ; basic functions for mathematical operation
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

# Challenge 2 ; booleans
def is_even() -> bool:
    """Checks if integer is even or odd.
    
    :return bool: True if even, False if odd.
    """

# Challenge 2.5 ; strings, lists, and booleans
ROCK_PAPER_SCISSORS = ["rock", "paper", "scissors"]
from random import randint
def rps_win_or_lost() -> bool:
    """Checks if player's hand wins or loses.
    
    Depending on whether 'rock', 'paper', or 'scissors' is passed - check if
    the user beats the computer.
    """

    def get_cpu_tactic() -> str:
        """Generates the computer's move.
        
        Uses the random package's randint() to select a tactic's index from
        ROCK_PAPER_SCISSORS.
        
        :return string: member of ROCK_PAPER_SCISSORS
        """


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

def count_vowels() -> int:
    """Count vowels in a string."""

def count_punctuation() -> int:
    """Count non alphabetical characters in a string."""

def count_uppercase() -> int:
    """Count uppercase characters in a string."""

def count_lowercase() -> int:
    """Count lowercase characters in a string."""

def as_lowercase() -> str:
    """Returns a given string in lowercase."""

def as_upper_lower() -> str:
    """Returns a string where each character alternates uppercase&lowercase."""

# Challenge 4 ; Prime Number Detector :
# create a method which takes one integer as input and returns True or False
# depending on whether or not that number is a prime number.

# HINT ; use the modulus operator :: '%' (if )
def is_prime(n: int) -> bool:
    """Boolean integer detector.
    
    Takes an integer and returns true/false based on whether or not it is a 
    prime number.
    
    :param n: integer input by the user.
    
    :return bool: True if prime, False if not.
    """
