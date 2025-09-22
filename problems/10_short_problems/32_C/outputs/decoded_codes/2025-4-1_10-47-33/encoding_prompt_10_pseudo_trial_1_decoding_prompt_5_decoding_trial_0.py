def mc(n, s):
    # Calculate quotient and remainder
    quotient = n // s
    remainder = n % s
    
    # If there is a remainder, return adjusted value
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return n  # If no remainder, return original value

# Main program starts here
# Read inputs n, m, s from standard input
n = int(input())
m = int(input())
s = int(input())

# Call mc function with n and s, and then with m and s
result1 = mc(n, s)
result2 = mc(m, s)

# Output the product of both results
print(result1 * result2)
