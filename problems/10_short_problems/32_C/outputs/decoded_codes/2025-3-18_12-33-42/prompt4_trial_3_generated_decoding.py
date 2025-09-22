def calculate_adjusted_value(total, divisor):
    """
    Calculate the adjusted value based on given total and divisor.
    
    Parameters:
    total (int): The total value to be adjusted.
    divisor (int): The divisor to calculate quotient and remainder.
    
    Returns:
    int: The adjusted value based on the logic provided.
    """
    # Calculate quotient and remainder
    quotient, remainder = divmod(total, divisor)
    
    # If there is a remainder, calculate the adjusted value
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return total

# Read input values for n, m, and s
n = int(input())
m = int(input())
s = int(input())

# Calculate the final result by multiplying the adjusted values of n and m
result = calculate_adjusted_value(n, s) * calculate_adjusted_value(m, s)

# Output the result
print(result)
