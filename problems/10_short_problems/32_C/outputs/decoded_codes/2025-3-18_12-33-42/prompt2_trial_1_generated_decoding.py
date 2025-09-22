# Define a Function
def CalculateRemainderAdjustedTotal(totalItems, groupSize):
    # Calculate the number of full groups
    fullGroups = totalItems // groupSize
    # Calculate the remaining items
    remainingItems = totalItems % groupSize
    
    # Check if there are remaining items
    if remainingItems > 0:
        return remainingItems * (fullGroups + 1)
    else:
        return totalItems

# Read Input Values
totalItemsN = int(input())
totalItemsM = int(input())
groupSizeS = int(input())

# Calculate
adjustedTotalN = CalculateRemainderAdjustedTotal(totalItemsN, groupSizeS)
adjustedTotalM = CalculateRemainderAdjustedTotal(totalItemsM, groupSizeS)

# Output the Result
finalResult = adjustedTotalN * adjustedTotalM
print(finalResult)
