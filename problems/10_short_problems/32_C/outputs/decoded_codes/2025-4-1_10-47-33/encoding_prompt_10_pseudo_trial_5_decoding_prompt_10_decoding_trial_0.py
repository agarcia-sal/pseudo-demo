def calculate_remainder(n, s):
    """Calculate adjusted remainder based on full groups of size s."""
    quotient = n // s
    remainder = n % s
    
    # Adjust remainder based on the presence of a remainder
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return n

# Read input values for n, m, and s from the user
n = int(input())
m = int(input())
s = int(input())

# Calculate results using the defined function for n and m
result1 = calculate_remainder(n, s)
result2 = calculate_remainder(m, s)

# Print the product of the two results
print(result1 * result2)
