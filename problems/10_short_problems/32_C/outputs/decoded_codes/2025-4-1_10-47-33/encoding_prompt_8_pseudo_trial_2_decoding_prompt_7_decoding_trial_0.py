def calculateGroups(totalQuantity, groupSize):
    # Determine how many full groups can be formed
    fullGroups = totalQuantity // groupSize  # Integer division
    remainder = totalQuantity % groupSize      # Find the count of extra items

    # Determine the effective number of groups based on the remainder
    if remainder > 0:
        # Additional groups can be formed with the extra items
        return remainder * (fullGroups + 1)    
    else:
        # No extra items, return total quantity as the effective groups
        return totalQuantity                      

# Main program execution starts here
quantity1 = int(input())  # Read the first quantity from input
quantity2 = int(input())  # Read the second quantity from input
groupSize = int(input())   # Read the group size from input

# Calculate the effective group values for both quantities
effectiveGroups1 = calculateGroups(quantity1, groupSize)  # For quantity1
effectiveGroups2 = calculateGroups(quantity2, groupSize)  # For quantity2

# Multiply the two effective group values to get the final result
finalResult = effectiveGroups1 * effectiveGroups2         

# Output the final result
print(finalResult)                                          
