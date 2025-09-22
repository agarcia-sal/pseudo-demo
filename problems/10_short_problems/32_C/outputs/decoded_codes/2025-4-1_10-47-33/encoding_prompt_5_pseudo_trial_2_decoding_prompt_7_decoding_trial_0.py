def CalculateAdjustedGroups(value, groupSize):
    # Divide value into groups of the specified size
    quotient, remainder = divmod(value, groupSize)  # divmod gives both quotient and remainder
    # Check if there is a remainder
    if remainder > 0:
        # If there is a remainder, include one extra group for it
        return remainder * (quotient + 1)
    else:
        # If there is no remainder, return the original value
        return value

# Read input values for n, m, and s from the user
n = int(input())  # First number
m = int(input())  # Second number
s = int(input())  # Size of groups

# Calculate the adjusted group values for n and m
adjustedN = CalculateAdjustedGroups(n, s)
adjustedM = CalculateAdjustedGroups(m, s)

# Calculate the product of the two adjusted values
product = adjustedN * adjustedM

# Output the result of the product
print(product)
