# Function to perform the specified calculations
def mc(n, s):
    # Calculate quotient
    quotient = n // s
    # Calculate remainder
    remainder = n % s
    
    # Check if there is a remainder
    if remainder > 0:
        # If remainder exists, return adjusted value
        return remainder * (quotient + 1)
    else:
        # If no remainder, return original value
        return n

# Main program starts here
# Read inputs for n, m, and s
n = int(input())
m = int(input())
s = int(input())

# Call mc function with n and s, and m and s
result1 = mc(n, s)
result2 = mc(m, s)

# Output the product of both results
print(result1 * result2)
