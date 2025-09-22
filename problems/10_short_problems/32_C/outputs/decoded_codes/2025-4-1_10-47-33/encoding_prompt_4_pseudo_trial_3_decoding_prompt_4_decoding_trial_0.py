def mc(number, divisor):
    # Calculate quotient and remainder
    quotient, remainder = divmod(number, divisor)
    
    # If there's a remainder, return remainder multiplied by (quotient + 1)
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number

# Read integers n, m, s from input
n = int(input())
m = int(input())
s = int(input())

# Calculate results using the mc function
result1 = mc(n, s)
result2 = mc(m, s)

# Print the product of the two results
print(result1 * result2)
