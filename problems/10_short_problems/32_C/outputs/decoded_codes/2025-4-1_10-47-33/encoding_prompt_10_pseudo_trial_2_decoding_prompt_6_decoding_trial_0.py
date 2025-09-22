# Define the function to perform the division and calculate the result
def mc(n, s):
    # Calculate quotient and remainder
    quotient = n // s  # Integer division for quotient
    remainder = n % s   # Modulus operation for remainder

    # Check if there is a remainder
    if remainder > 0:
        return remainder * (quotient + 1)  # Return modified value if there's a remainder
    else:
        return n  # Return n if there's no remainder

# Begin Main Block
# Read three integers from user input
n = int(input())
m = int(input())
s = int(input())

# Calculate the result of mc(n, s) and mc(m, s)
result1 = mc(n, s)  # Calculate for n
result2 = mc(m, s)  # Calculate for m

# Print the product of both results
print(result1 * result2)  # Output the final product
