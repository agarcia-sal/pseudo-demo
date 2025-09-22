def calculate_remainder_count(number, divisor):
    """Calculate the adjusted count based on the remainder."""
    quotient = number // divisor
    remainder = number % divisor
    
    # If there is a remainder, adjust the count accordingly
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number

# Read input values
n = int(input())
m = int(input())
s = int(input())

# Calculate adjusted counts for both n and m based on s
adjusted_count_for_n = calculate_remainder_count(n, s)
adjusted_count_for_m = calculate_remainder_count(m, s)

# Compute the product of the adjusted counts for n and m
result = adjusted_count_for_n * adjusted_count_for_m

# Output the final result
print(result)
