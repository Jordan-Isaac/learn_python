def is_prime(n: int) -> bool:
    """Boolean prime number detector.

    Takes an integer and returns True if it is a prime number, False otherwise.

    :param n: Integer input.
    :return: True if n is prime, False otherwise.
    """
    if n <= 1:
        return False  # 0 and 1 are not prime numbers

    # Check for factors from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False  # n is divisible by i, so it's not prime

    return True  # If no factors were found, n is prime

def main():
    user_input = input("number?: ")
    
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
