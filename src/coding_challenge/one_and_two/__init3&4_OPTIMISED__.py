# Chat GPT optimised
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

def main():
    # Testing the functions with the provided test strings
    print("Results for TEST_STRING:")
    print(f"Count Vowels: {count_vowels(TEST_STRING)}")
    print(f"Count Punctuation: {count_punctuation(TEST_STRING)}")
    print(f"Count Uppercase: {count_uppercase(TEST_STRING)}")
    print(f"Count Lowercase: {count_lowercase(TEST_STRING)}")
    print(f"As Lowercase: {as_lowercase(TEST_STRING)}")
    print(f"As Upper-Lower: {as_upper_lower(TEST_STRING)}")
    print(f"Get First Word: {get_first_word(TEST_STRING)}")
    print(f"Get Word by Index: {get_word_by_index(TEST_STRING_TWO, 5)}\n")

    # Testing the functions with TEST_STRING_TWO
    print("Results for TEST_STRING_TWO:")
    print(f"Count Vowels: {count_vowels(TEST_STRING_TWO)}")
    print(f"Count Punctuation: {count_punctuation(TEST_STRING_TWO)}")
    print(f"Count Uppercase: {count_uppercase(TEST_STRING_TWO)}")
    print(f"Count Lowercase: {count_lowercase(TEST_STRING_TWO)}")
    print(f"As Lowercase: {as_lowercase(TEST_STRING_TWO)}")
    print(f"As Upper-Lower: {as_upper_lower(TEST_STRING_TWO)}")
    print(f"Get First Word: {get_first_word(TEST_STRING_TWO)}")
    print(f"Get Word by Index: {get_word_by_index(TEST_STRING_TWO, 5)}")

if __name__ == "__main__":
    main()