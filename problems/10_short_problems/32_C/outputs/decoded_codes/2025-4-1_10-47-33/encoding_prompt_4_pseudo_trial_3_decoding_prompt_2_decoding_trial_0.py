def mc(number, divisor):
    # Divide number by divisor to get quotient and remainder
    quotient = number // divisor
    remainder = number % divisor
    
    # Check if remainder is greater than 0
    if remainder > 0:
        # Return remainder multiplied by (quotient + 1)
        return remainder * (quotient + 1)
    else:
        # Return number if remainder is not greater than 0
        return number

# Read inputs for n, m, s
n = int(input())
m = int(input())
s = int(input())

# Calculate result1 and result2
result1 = mc(n, s)
result2 = mc(m, s)

# Print the product of result1 and result2
print(result1 * result2)
