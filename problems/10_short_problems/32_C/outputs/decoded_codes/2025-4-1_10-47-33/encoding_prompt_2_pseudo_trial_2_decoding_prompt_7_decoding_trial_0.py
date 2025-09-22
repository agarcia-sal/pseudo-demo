def mc(n, s):
    # Calculate the quotient and remainder
    quotient = n // s  
    remainder = n % s  
    
    # Check if there is a remainder
    if remainder > 0:
        # Return product of remainder and (quotient + 1)
        return remainder * (quotient + 1)
    else:
        # If there is no remainder, return the original number
        return n

# Read input values and convert them to integers
n, m, s = map(int, input().split())

# Calculate the result by multiplying the outputs of mc for n and m with s
result = mc(n, s) * mc(m, s)

# Print the final result
print(result)
