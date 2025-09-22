def calculateGroups(totalQuantity, groupSize):
    fullGroups = totalQuantity // groupSize  # Determine how many full groups can be formed
    remainder = totalQuantity % groupSize     # Find the count of extra items

    if remainder > 0:
        return remainder * (fullGroups + 1)  # Return effective groups if there are extra items
    else:
        return totalQuantity                   # Return total quantity if no extra items

quantity1 = int(input())
quantity2 = int(input())
groupSize = int(input())

effectiveGroups1 = calculateGroups(quantity1, groupSize)  # Calculate effective groups for quantity1
effectiveGroups2 = calculateGroups(quantity2, groupSize)  # Calculate effective groups for quantity2
finalResult = effectiveGroups1 * effectiveGroups2          # Multiply the two effective group values
print(finalResult)                                          # Output the final result
