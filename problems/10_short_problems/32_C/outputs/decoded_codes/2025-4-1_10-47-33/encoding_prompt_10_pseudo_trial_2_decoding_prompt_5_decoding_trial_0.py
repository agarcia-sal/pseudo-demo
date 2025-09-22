def mc(n, s):
    # Divide n by s to get the quotient and remainder
    quotient, remainder = divmod(n, s)
    
    # Check if there is a remainder
    if remainder > 0:
        # Return modified value if there's a remainder
        return remainder * (quotient + 1)
    else:
        # Return n if no remainder
        return n

# Main Block
# Read integers n, m, s from user input
n, m, s = map(int, input().split())

# Calculate results of mc(n, s) and mc(m, s)
result1 = mc(n, s)
result2 = mc(m, s)

# Print the product of both results
print(result1 * result2)

# Test cases can be added here if needed
# Example: If the user inputs "10 20 3", it should calculate and print the product of mc(10, 3) and mc(20, 3)
