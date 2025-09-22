def calculate_remainder(n, s):
    """
    Function to calculate the adjusted remainder based on quotient and remainder.
    If there is a remainder, return it multiplied by (quotient + 1), otherwise return n.
    """
    # Calculate quotient and remainder of n divided by s
    quotient = n // s
    remainder = n % s
    
    # Check if there is a remainder
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
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
