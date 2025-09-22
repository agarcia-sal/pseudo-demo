def calculateGroups(number, groupSize):
    # Determine how many complete groups can be formed and the remainder
    completeGroups, remainder = divmod(number, groupSize)
    # If there are any leftover items, account for them by adding an extra group
    if remainder > 0:
        return remainder * (completeGroups + 1)
    else:
        return number  # If no leftovers, return the original number

# Read input values: total items for the first and second count, and the group size
totalItems1 = int(input())
totalItems2 = int(input())
groupSize = int(input())

# Calculate groups for the first and second total items
groupsForFirstCount = calculateGroups(totalItems1, groupSize)
groupsForSecondCount = calculateGroups(totalItems2, groupSize)

# Output the product of the two group counts
print(groupsForFirstCount * groupsForSecondCount)
