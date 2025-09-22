def CalculateGroups(totalItems, groupSize):
    # Calculate the complete groups that can be formed
    quotient = totalItems // groupSize
    remainder = totalItems % groupSize

    # If there is a remainder, calculate the modified group count
    if remainder != 0:
        return remainder * (quotient + 1)
    else:
        return totalItems

# Input data
totalA = int(input())
totalB = int(input())
groupSize = int(input())

# Compute group values
valueA = CalculateGroups(totalA, groupSize)
valueB = CalculateGroups(totalB, groupSize)

# Calculate and print result
result = valueA * valueB
print(result)
