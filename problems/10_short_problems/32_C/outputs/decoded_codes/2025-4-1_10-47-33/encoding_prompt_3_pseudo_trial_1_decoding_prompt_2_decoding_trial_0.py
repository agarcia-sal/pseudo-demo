def mc(totalItems, size):
    # Calculate how many full groups can fit
    fullGroups, remainder = divmod(totalItems, size)
    
    # Determine the effective item count based on remainder
    if remainder > 0:
        return remainder * (fullGroups + 1)  # Count remainder items with an additional group
    else:
        return totalItems  # No remainder, return total item count

# Read input values for total items n, additional total m, and group size s
totalItems_n = int(input())
additionalTotal_m = int(input())
groupSize_s = int(input())

# Calculate and print the product of the processed item counts for n and m
print(mc(totalItems_n, groupSize_s) * mc(additionalTotal_m, groupSize_s))
