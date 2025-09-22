def calculateGroups(totalQuantity, groupSize):
    """
    Calculate the effective number of groups that can be formed 
    from the total quantity based on the group size.
    
    Parameters:
    totalQuantity (int): The total number of items.
    groupSize (int): The size of each group.
    
    Returns:
    int: The effective number of groups.
    """
    # Determine how many full groups can be formed and the remainder
    fullGroups = totalQuantity // groupSize
    remainder = totalQuantity % groupSize

    # If there are extra items, calculate effective groups accordingly
    if remainder > 0:
        return remainder * (fullGroups + 1)  # Include the partial groups
    else:
        return totalQuantity  # No extra items, return total quantity


# Main program
# Read input values for quantities and group size
quantity1 = int(input())
quantity2 = int(input())
groupSize = int(input())

# Calculate effective group values for both quantities
effectiveGroups1 = calculateGroups(quantity1, groupSize)
effectiveGroups2 = calculateGroups(quantity2, groupSize)

# Multiply the two effective group values
finalResult = effectiveGroups1 * effectiveGroups2

# Output the final result
print(finalResult)
