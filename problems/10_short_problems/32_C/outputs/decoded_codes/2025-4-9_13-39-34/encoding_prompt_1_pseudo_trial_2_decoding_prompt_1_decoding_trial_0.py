def CalculateMaxItems(num1, size):
    fullGroups1 = num1 // size  # Divide num1 by size (integer division)
    leftovers1 = num1 % size     # Calculate the remainder

    if leftovers1 > 0:
        return leftovers1 * (fullGroups1 + 1)  # Calculate new max items including leftover
    else:
        return num1  # If no leftover, return the original number


# Main Program:
totalItems1 = int(input())
totalItems2 = int(input())
groupSize = int(input())

result1 = CalculateMaxItems(totalItems1, groupSize)  # Calculate for the first set
result2 = CalculateMaxItems(totalItems2, groupSize)  # Calculate for the second set

print(result1 * result2)  # Output the final result
