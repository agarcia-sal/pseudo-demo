def calculate_remainder(n, s):
    # Calculate how many full groups of size s can be made from n
    quotient = n // s  # Integer division to get the quotient
    remainder = n % s   # Modulo operation to get the remainder
    
    # If there is a remainder, return the adjusted value
    if remainder > 0:
        return remainder * (quotient + 1)  # Adjusted value
    else:
        return n  # No remainder, return n

# Read input values for n, m, and s from user
n = int(input())  # Input for n
m = int(input())  # Input for m
s = int(input())  # Input for s

# Calculate results using the defined function for n and m
result1 = calculate_remainder(n, s)  # Result from n
result2 = calculate_remainder(m, s)  # Result from m

# Print the product of the two results
print(result1 * result2)  # Output product of result1 and result2
