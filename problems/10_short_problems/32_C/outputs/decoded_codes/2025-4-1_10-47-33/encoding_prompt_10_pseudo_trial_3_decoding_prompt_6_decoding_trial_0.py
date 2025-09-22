# Function to calculate the modified value based on the inputs
def mc(n, s):
    # Divide n by s to get quotient and remainder
    quotient, remainder = divmod(n, s)
    
    # Check if remainder is greater than zero
    if remainder > 0:
        # If there is a remainder, calculate and return extended value
        return remainder * (quotient + 1)
    else:
        # If there is no remainder, return n
        return n

# Read input values for n, m, and s
n = int(input())
m = int(input())
s = int(input())

# Calculate the product of mc(n, s) and mc(m, s)
result = mc(n, s) * mc(m, s)

# Output the result
print(result)
