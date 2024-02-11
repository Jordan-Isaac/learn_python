# Chat GPT optimised the [done] file

def perform_operation_and_check(operation_name: str, result: float) -> None:
    """Perform a mathematical operation and check if the result is even."""
    print(f"{operation_name}: {result}")
    print(f"Is the result even?: {is_even(int(result))}\n")

# Your existing code for calculations
FIRST_NUMBER = 110100100
SECOND_NUMBER = 1000101

# Perform addition and check if the result is even
result = add(FIRST_NUMBER, SECOND_NUMBER)
rounded_result = two_dp(result)
perform_operation_and_check("Addition", rounded_result)

# Perform subtraction and check if the result is even
subtraction_result = subtract(FIRST_NUMBER, SECOND_NUMBER)
perform_operation_and_check("Subtraction", subtraction_result)

# Perform multiplication and check if the result is even
multiply_result = multiply(FIRST_NUMBER, SECOND_NUMBER)
perform_operation_and_check("Multiplication", multiply_result)

# Perform division and check if the result is even
division_result = divide(FIRST_NUMBER, SECOND_NUMBER)
rounded_division_result = two_dp(division_result)
perform_operation_and_check("Division", rounded_division_result)

# Challenge 2 ; booleans
# Your existing code for is_even and is_member

# Perform addition and check if the result is even
perform_operation_and_check("Addition", rounded_result)

# Perform subtraction and check if the result is even
subtraction_result = subtract(FIRST_NUMBER, SECOND_NUMBER)
perform_operation_and_check("Subtraction", subtraction_result)

# Perform multiplication and check if the result is even
multiply_result = multiply(FIRST_NUMBER, SECOND_NUMBER)
perform_operation_and_check("Multiplication", multiply_result)

# Perform division and check if the result is even
division_result = divide(FIRST_NUMBER, SECOND_NUMBER)
rounded_division_result = two_dp(division_result)
perform_operation_and_check("Division", rounded_division_result)