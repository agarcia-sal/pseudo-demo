def mc(number, size):
    quotient, remainder = divmod(number, size)  # Using divmod to calculate quotient and remainder
    if remainder > 0:
        return remainder * (quotient + 1)  # Calculate adjusted value
    else:
        return number  # Return the original number if no remainder

# Read input values for n, m, and s
n, m, s = map(int, input().split())  # Assume input is space-separated integers

# Calculate and print the product of adjusted values for n and m
print(mc(n, s) * mc(m, s))
