def CalculateExcessItems(totalItems, segmentSize):
    quotient = totalItems // segmentSize
    remainder = totalItems % segmentSize
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return totalItems

totalItemsFromInput = int(input())
anotherVariable = int(input())
segmentSizeFromInput = int(input())

resultForTotalItems = CalculateExcessItems(totalItemsFromInput, segmentSizeFromInput)
resultForAnotherVariable = CalculateExcessItems(anotherVariable, segmentSizeFromInput)

FINAL_RESULT = resultForTotalItems * resultForAnotherVariable

print(FINAL_RESULT)
