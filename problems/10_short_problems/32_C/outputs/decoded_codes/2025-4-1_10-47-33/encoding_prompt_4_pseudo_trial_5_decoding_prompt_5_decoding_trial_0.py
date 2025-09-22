def mc(number, segment_size):
    # Calculate the quotient and remainder of number divided by segment_size
    quotient, remainder = divmod(number, segment_size)
    
    # If there is a remainder, return remainder multiplied by (quotient + 1)
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number

# Read input values n, m, and s from standard input
n = int(input())
m = int(input())
s = int(input())

# Calculate the adjusted values using the mc function
result1 = mc(n, s)
result2 = mc(m, s)

# Print the product of the two results
print(result1 * result2)
