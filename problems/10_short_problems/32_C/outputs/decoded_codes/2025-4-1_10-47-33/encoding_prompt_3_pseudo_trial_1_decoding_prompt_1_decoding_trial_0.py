def mc(totalItems, size):
    # Calculate how many full groups can fit
    fullGroups = totalItems // size  # Integer division to get full groups
    remainder = totalItems % size  # Modulus to find remainder items
    
    # Determine the effective item count based on remainder
    if remainder > 0:
        return remainder * (fullGroups + 1)  # Count remainder items with an additional group
    else:
        return totalItems  # No remainder, return total item count

# Read input values for the total items n, another total m, and the group size s
totalItems_n = int(input())
additionalTotal_m = int(input())
groupSize_s = int(input())

# Calculate and print the product of the processed item counts for n and m
print(mc(totalItems_n, groupSize_s) * mc(additionalTotal_m, groupSize_s))
