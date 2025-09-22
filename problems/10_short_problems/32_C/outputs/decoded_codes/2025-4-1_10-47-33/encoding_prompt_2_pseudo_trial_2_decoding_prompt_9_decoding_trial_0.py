def mc(n, s):
    # Calculate quotient and remainder
    quotient = n // s
    remainder = n % s
    
    # Check if remainder is greater than zero
    if remainder > 0:
        # Return product of remainder and (quotient + 1)
        return remainder * (quotient + 1)
    else:
        # Return the original number if remainder is zero
        return n

# Read input values - splits the input by spaces and converts to integers
n, m, s = map(int, input().split())

# Calculate the result using the mc function
result = mc(n, s) * mc(m, s)

# Print the final result
print(result)
