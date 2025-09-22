def calculate_remainder(n, s):
    # Calculate the quotient of n divided by s
    quotient = n // s
    # Calculate the remainder of n divided by s
    remainder = n % s
    
    # If there is a remainder, return the adjusted value
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return n

# Read input values for n, m, and s from user
n = int(input())
m = int(input())
s = int(input())

# Calculate results using the defined function for n and m
result1 = calculate_remainder(n, s)
result2 = calculate_remainder(m, s)

# Print the product of the two results
print(result1 * result2)
