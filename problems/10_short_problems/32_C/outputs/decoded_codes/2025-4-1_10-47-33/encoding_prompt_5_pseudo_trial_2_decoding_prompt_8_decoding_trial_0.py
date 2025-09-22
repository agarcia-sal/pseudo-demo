def CalculateAdjustedGroups(value, groupSize):
    quotient = value // groupSize
    remainder = value % groupSize
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return value

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
