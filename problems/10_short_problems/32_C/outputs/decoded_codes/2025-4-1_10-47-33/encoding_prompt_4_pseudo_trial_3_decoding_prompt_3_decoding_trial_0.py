def mc(number, divisor):
    """Calculate a modified value based on the division of number by divisor."""
    quotient, remainder = divmod(number, divisor)  # Get quotient and remainder in one step
    if remainder > 0:
        return remainder * (quotient + 1)  # Adjusted return value for non-zero remainder
    else:
        return number  # Return number directly if no remainder

# Read three integers from input
n = int(input())
m = int(input())
s = int(input())

# Calculate results using the mc function
result1 = mc(n, s)
result2 = mc(m, s)

# Print the product of the two results
print(result1 * result2)
