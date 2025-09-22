def calculate_remainder_and_quotient(input_number, divisor):
    """
    Calculate the quotient and remainder when dividing input_number by divisor.
    If there is a remainder, return the product of the remainder and one more than the quotient.
    If there is no remainder, return the original input_number.
    
    Args:
    input_number (int): The number to be divided.
    divisor (int): The number by which to divide.
    
    Returns:
    int: The computed result based on the condition of the remainder.
    """
    quotient, remainder = divmod(input_number, divisor)
    
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        # If there is no remainder, return the original input_number
        return input_number


# Read integers n, m, and s from user input
n = int(input())
m = int(input())
s = int(input())

# Calculate results for n and m with respect to s
result = calculate_remainder_and_quotient(n, s) * calculate_remainder_and_quotient(m, s)

# Output the final result
print(result)
