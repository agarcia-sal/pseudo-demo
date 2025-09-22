def mc(number, divisor):
    # Perform division to get quotient and remainder
    quotient = number // divisor  # Integer division to get quotient
    remainder = number % divisor   # Modulus operator to find remainder

    # Check if the remainder is greater than 0
    if remainder > 0:
        # Return remainder multiplied by (quotient + 1)
        return remainder * (quotient + 1)
    else:
        # Return the original number if remainder is 0
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
