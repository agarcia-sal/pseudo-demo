# Define Function for Group Calculation
def CalculateGroups(totalItems, groupSize):
    quotient = totalItems // groupSize  # Divide totalItems by groupSize
    remainder = totalItems % groupSize    # Find the remainder of totalItems divided by groupSize
    
    if remainder != 0:                     # If there is a remainder
        return remainder * (quotient + 1)  # Return remainder multiplied by (quotient + 1)
    else:
        return totalItems                   # Otherwise, return totalItems

# Input Data
totalA = int(input())  # Read an integer for totalA
totalB = int(input())  # Read an integer for totalB
groupSize = int(input())  # Read an integer for groupSize

# Compute Group Values
valueA = CalculateGroups(totalA, groupSize)  # Calculate for totalA
valueB = CalculateGroups(totalB, groupSize)  # Calculate for totalB

# Calculate and Print Result
result = valueA * valueB  # Multiply the values obtained
print(result)              # Output the resulting product
