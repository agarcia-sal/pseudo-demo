def mc(n, s):
    # Calculate quotient and remainder
    q = n // s  # Integer division to get the quotient
    r = n % s   # Modulo operation to get the remainder
    
    # If there is a remainder, adjust the return value accordingly
    if r > 0:
        return r * (q + 1)  # Return adjusted value if remainder exists
    else:
        return n  # Return original value if no remainder

# Main program starts here
# Read inputs n, m, and s from standard input
n = int(input())  # First integer input
m = int(input())  # Second integer input
s = int(input())  # Third integer input

# Call mc function with n and s, and m and s, respectively
result1 = mc(n, s)  # Compute result for n and s
result2 = mc(m, s)  # Compute result for m and s

# Output the product of both results
print(result1 * result2)  # Print the final result
