def mc(number, size):
    # Calculate the quotient and remainder when dividing number by size
    quotient, remainder = divmod(number, size)
    
    # If there is a remainder, calculate the adjusted value
    if remainder > 0:
        return remainder * (quotient + 1)  # Calculate adjusted value
    else:
        return number  # Return the original number if no remainder

# Read input values for n, m, and s
n = int(input())
m = int(input())
s = int(input())

# Calculate and print the product of adjusted values for n and m
result = mc(n, s) * mc(m, s)
print(result)

# Test cases (uncomment for testing):
# n = 10, m = 5, s = 3 should return 20
# n = 7, m = 8, s = 2 should return 24
# n = 0, m = 0, s = 1 should return 0
