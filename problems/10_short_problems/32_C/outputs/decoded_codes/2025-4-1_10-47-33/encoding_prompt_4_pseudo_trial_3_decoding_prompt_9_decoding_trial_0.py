def mc(number, divisor):
    # Calculate quotient and remainder
    quotient = number // divisor
    remainder = number % divisor

    # Check the remainder to determine return value
    if remainder > 0:
        return remainder * (quotient + 1)  # Return altered value based on remainder
    else:
        return number  # If remainder is 0, return original number

# Read three integers from input
n = int(input())
m = int(input())
s = int(input())

# Calculate results using the mc function
result1 = mc(n, s)
result2 = mc(m, s)

# Print the product of the results
print(result1 * result2)
