def mc(number, divisor):
    # Calculate quotient and remainder of the division
    quotient = number // divisor
    remainder = number % divisor
    
    # If remainder is greater than 0, return adjusted remainder
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return number

# Read three integers from input
n = int(input())
m = int(input())
s = int(input())

# Calculate results using the mc function
result1 = mc(n, s)
result2 = mc(m, s)

# Print the product of the two results
print(result1 * result2)
