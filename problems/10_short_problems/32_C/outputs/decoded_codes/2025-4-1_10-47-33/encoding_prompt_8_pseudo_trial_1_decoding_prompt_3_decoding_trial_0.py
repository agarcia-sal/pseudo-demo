def calculate_remainder_and_adjustment(number, divisor):
    """
    Calculate the adjusted value based on the remainder of number divided by divisor.
    
    :param number: The number to be adjusted
    :param divisor: The divisor used for the division
    :return: Adjusted value based on the remainder
    """
    quotient, remainder = divmod(number, divisor)  # Calculate quotient and remainder
    
    # If there is a remainder, return the adjusted value
    if remainder > 0:
        return remainder * (quotient + 1)
    
    # If no remainder, return the original number
    return number

# Read the input values for n, m, and s
n = int(input())
m = int(input())
s = int(input())

# Calculate the adjusted values for n and m using the helper function
adjusted_value_for_n = calculate_remainder_and_adjustment(n, s)
adjusted_value_for_m = calculate_remainder_and_adjustment(m, s)

# Compute the final result by multiplying the adjusted values for n and m
final_result = adjusted_value_for_n * adjusted_value_for_m

# Print the final result
print(final_result)
