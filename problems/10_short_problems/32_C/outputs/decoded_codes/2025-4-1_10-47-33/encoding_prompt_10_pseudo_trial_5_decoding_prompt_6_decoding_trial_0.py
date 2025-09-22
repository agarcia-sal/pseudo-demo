# Function to calculate the adjusted remainder
def calculate_remainder(n, s):
    # Calculate how many full groups of size s can be made from n
    quotient = n // s  # Integer division
    remainder = n % s   # Remainder of n divided by s
    
    # If there is a remainder, return the adjusted value
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return n

# Read input values for n, m, and s from user
n = int(input())  # Input for n
m = int(input())  # Input for m
s = int(input())  # Input for s

# Calculate results using the defined function for n and m
result1 = calculate_remainder(n, s)  # Calculate for n
result2 = calculate_remainder(m, s)  # Calculate for m

# Print the product of the two results
print(result1 * result2)  # Output the product
