def mc(totalItems, size):
    # Calculate how many full groups can fit
    fullGroups = totalItems // size  # Integer division for full groups
    remainder = totalItems % size      # Calculate remaining items
    
    # Determine the effective item count based on remainder
    if remainder > 0:
        return remainder * (fullGroups + 1)  # Count remainder items with an additional group
    else:
        return totalItems  # No remainder, return total item count

# Read input values for the total items n, additional total m, and the group size s
totalItems = int(input())
additionalTotal = int(input())
groupSize = int(input())

# Calculate and print the product of the processed item counts for n and m
result = mc(totalItems, groupSize) * mc(additionalTotal, groupSize)
print(result)
