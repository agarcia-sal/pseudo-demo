def mc(number, segment_size):
    """Calculate adjusted value based on number and segment size."""
    quotient, remainder = divmod(number, segment_size)
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
