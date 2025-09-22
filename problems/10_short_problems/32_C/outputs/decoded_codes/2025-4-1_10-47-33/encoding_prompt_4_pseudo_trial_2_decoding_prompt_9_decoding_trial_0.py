def mc(number, size):
    # Calculate quotient and remainder when dividing number by size
    quotient = number // size
    remainder = number % size
    
    # Check if there is a remainder
    if remainder > 0:
        # Calculate adjusted value if there is a remainder
        return remainder * (quotient + 1)
    else:
        # Return the original number if no remainder
        return number

# Read input values for n, m, and s from input
n = int(input())
m = int(input())
s = int(input())

# Calculate and print the product of adjusted values for n and m
print(mc(n, s) * mc(m, s))
