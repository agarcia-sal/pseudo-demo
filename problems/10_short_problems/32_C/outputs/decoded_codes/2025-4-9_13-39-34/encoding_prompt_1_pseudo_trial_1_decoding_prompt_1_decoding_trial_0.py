def calculateAdjustedGroups(number, groupSize):
    # Divide the number into full groups of the specified size
    fullGroups, remainder = divmod(number, groupSize)
    
    # If there is a remainder, meaning there are extra items
    if remainder > 0:
        # Return the total groups including the extra items
        return remainder * (fullGroups + 1)
    else:
        # If everything fits perfectly into groups, return the original number
        return number

# Read the inputs from the user (expected to be three integers)
inputValues = [int(x) for x in input().split()]

# Set n, m, s from input values
n = inputValues[0]  # First value
m = inputValues[1]  # Second value
s = inputValues[2]  # Group size

# Calculate the adjusted group counts for n and m
adjustedGroupsForN = calculateAdjustedGroups(n, s)
adjustedGroupsForM = calculateAdjustedGroups(m, s)

# Calculate and display the product of the adjusted group counts
print(adjustedGroupsForN * adjustedGroupsForM)
