def mc(n, s):
    # Calculate the quotient and remainder
    quotient = n // s
    remainder = n % s
    
    # If the remainder is greater than zero, calculate the product
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        # Return the original number if no remainder
        return n

# Read input values and convert them to integers
n, m, s = map(int, input().split())

# Calculate the result by multiplying the outputs of the mc function
result = mc(n, s) * mc(m, s)

# Print the final result
print(result)
