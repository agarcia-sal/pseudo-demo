def CalculateExcessItems(totalItems, segmentSize):
    # Calculate the quotient and remainder when dividing totalItems by segmentSize
    quotient = totalItems // segmentSize
    remainder = totalItems % segmentSize
    
    # If there is a remainder, return it adjusted by (quotient + 1)
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return totalItems  # If no remainder, return totalItems

# Read inputs from the user
totalItemsFromInput = int(input())
anotherVariable = int(input())
segmentSizeFromInput = int(input())

# Calculate results for totalItems and anotherVariable
resultForTotalItems = CalculateExcessItems(totalItemsFromInput, segmentSizeFromInput)
resultForAnotherVariable = CalculateExcessItems(anotherVariable, segmentSizeFromInput)

# Final result is the product of the two calculations
FINAL_RESULT = resultForTotalItems * resultForAnotherVariable

# Output the final result
print(FINAL_RESULT)
