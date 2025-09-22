def calculate_remainder(n, s):
    """
    Calculate the adjusted value based on the remainder of the division
    of n by s, according to specific rules.

    Parameters:
    n (int): The number to be divided.
    s (int): The divisor.

    Returns:
    int: The adjusted value.
    """
    quotient = n // s  # Calculate the quotient
    remainder = n % s   # Calculate the remainder

    if remainder > 0:
        # If there is a remainder, return it multiplied by (quotient + 1)
        return remainder * (quotient + 1)
    else:
        # If there is no remainder, return n
        return n


# Read three integers from input
n = int(input())
m = int(input())
s = int(input())

# Calculate the adjusted values using the calculate_remainder function
adjusted_value_for_n = calculate_remainder(n, s)
adjusted_value_for_m = calculate_remainder(m, s)

# Calculate the final result by multiplying the two adjusted values
final_result = adjusted_value_for_n * adjusted_value_for_m

# Output the final result
print(final_result)
