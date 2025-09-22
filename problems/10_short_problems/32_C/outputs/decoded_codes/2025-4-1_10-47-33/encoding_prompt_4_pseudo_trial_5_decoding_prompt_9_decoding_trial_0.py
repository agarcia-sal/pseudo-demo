def mc(number, segment_size):
    # Calculate quotient and remainder from the division
    quotient = number // segment_size
    remainder = number % segment_size
    
    # If there is a remainder, return the adjusted value
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number

# Read input values from standard input
n = int(input())
m = int(input())
s = int(input())

# Calculate results using the mc function
result1 = mc(n, s)
result2 = mc(m, s)

# Print the product of the two results
print(result1 * result2)
