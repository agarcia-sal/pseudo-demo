def calculate_remainder(n, s):
    # Calculate how many full groups of size s can be made from n
    quotient = n // s  # Integer division to get the quotient
    remainder = n % s   # Modulo operation to get the remainder

    # If there is a remainder, return the adjusted value
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return n

# Read input values for n, m, and s from user
n = int(input())
m = int(input())
s = int(input())

# Ensure s is not zero to prevent division by zero error
if s <= 0:
    raise ValueError("s must be greater than 0")

# Calculate results using the defined function for n and m
result1 = calculate_remainder(n, s)
result2 = calculate_remainder(m, s)

# Print the product of the two results
print(result1 * result2)
