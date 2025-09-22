def CalculateAdjustedGroups(value, groupSize):
    # Divide value into groups of the specified size and adjust the remainder
    quotient = value // groupSize
    remainder = value % groupSize
    
    if remainder > 0:
        return remainder * (quotient + 1)  # If there’s a remainder, include one extra group for it
    else:
        return value  # If there’s no remainder, return the original value

# Read input values for n, m, and s from the user
n = int(input())
m = int(input())
s = int(input())

# Calculate the adjusted group values for n and m
adjustedN = CalculateAdjustedGroups(n, s)
adjustedM = CalculateAdjustedGroups(m, s)

# Calculate the product of the two adjusted values
product = adjustedN * adjustedM

# Output the result of the product
print(product)
