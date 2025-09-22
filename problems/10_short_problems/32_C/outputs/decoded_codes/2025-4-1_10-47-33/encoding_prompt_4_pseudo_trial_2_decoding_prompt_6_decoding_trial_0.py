def mc(number, size):
    # Compute the quotient and remainder of number divided by size
    quotient = number // size
    remainder = number % size
    
    # If there is a remainder, calculate the adjusted value
    if remainder > 0:
        return remainder * (quotient + 1)  # Adjusted value based on remainder
    else:
        return number  # Return the original number if there is no remainder

# Read input values for n, m, and s
n = int(input())
m = int(input())
s = int(input())

# Calculate and print the product of adjusted values for n and m
result = mc(n, s) * mc(m, s)
print(result)  # Output the final result
