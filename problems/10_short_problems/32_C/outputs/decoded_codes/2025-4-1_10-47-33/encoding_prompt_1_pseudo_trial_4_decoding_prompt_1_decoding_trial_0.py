def CalculateExcessItems(totalItems, segmentSize):
    quotient, remainder = divmod(totalItems, segmentSize)  # Get quotient and remainder
    if remainder > 0:  # Check if remainder is greater than zero
        return remainder * (quotient + 1)  # Return modified result if there's a remainder
    else:
        return totalItems  # Return totalItems if no remainder is present

totalItemsFromInput = int(input())  # Read totalItems
anotherVariable = int(input())  # Read anotherVariable
segmentSizeFromInput = int(input())  # Read segmentSize

resultForTotalItems = CalculateExcessItems(totalItemsFromInput, segmentSizeFromInput)
resultForAnotherVariable = CalculateExcessItems(anotherVariable, segmentSizeFromInput)

FINAL_RESULT = resultForTotalItems * resultForAnotherVariable  # Calculate final result

print(FINAL_RESULT)  # Output the final result
