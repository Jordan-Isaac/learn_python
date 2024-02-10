#Chat GPT Optimised
#Changes made:
#1 - Adjusted the condition n <= 1 to n < 2 for clarity.
#2 - Changed the prompt message for better user understanding.
#3 - Added comments to enhance code readability.
#4 - Adjusted spacing and formatting for consistency.
#5 - Improved variable names for better clarity.

def is_prime(n: int) -> bool:
    """Boolean prime number detector.

    Takes an integer and returns True if it is a prime number, False otherwise.

    :param n: Integer input.
    :return: True if n is prime, False otherwise.
    """
    if n < 2:
        return False  # Numbers less than 2 are not prime

    # Check for factors from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # n is divisible by i, so it's not prime

    return True  # If no factors were found, n is prime

def main():
    user_input = input("Enter a number: ")
    
    try:
        number = int(user_input)
        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
