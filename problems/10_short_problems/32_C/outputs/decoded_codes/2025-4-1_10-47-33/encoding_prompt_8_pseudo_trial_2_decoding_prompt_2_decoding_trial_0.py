def calculateGroups(totalQuantity, groupSize):
    # Calculate the number of full groups
    fullGroups = totalQuantity // groupSize  # Use integer division
    remainder = totalQuantity % groupSize     # Get the remainder

    # Determine effective groups based on the remainder
    if remainder > 0:
        return remainder * (fullGroups + 1)   # Extra items lead to effective group calculation
    else:
        return totalQuantity                    # No extra items, return total quantity

# Main program
quantity1 = int(input())  # Read the first quantity from input
quantity2 = int(input())  # Read the second quantity from input
groupSize = int(input())   # Read the group size from input

# Calculate effective group values for both quantities
effectiveGroups1 = calculateGroups(quantity1, groupSize)
effectiveGroups2 = calculateGroups(quantity2, groupSize)

# Multiply the two effective group values
finalResult = effectiveGroups1 * effectiveGroups2

# Output the final result
print(finalResult)
