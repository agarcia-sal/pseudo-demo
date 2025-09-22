def mc(number, size):
    quotient = number // size        # Integer division to get the quotient
    remainder = number % size        # Modulo operation to find the remainder
    if remainder > 0:                # Check if remainder is greater than 0
        return remainder * (quotient + 1)  # Calculate adjusted value
    else:
        return number                # Return the original number if no remainder

# Read input values for n, m, and s
n = int(input())                     # Read n from input and convert to int
m = int(input())                     # Read m from input and convert to int
s = int(input())                     # Read s from input and convert to int

# Calculate and print the product of adjusted values for n and m
print(mc(n, s) * mc(m, s))          # Print the result of the product
