def mc(totalItems, size):
    # Calculate how many full groups can fit
    fullGroups, remainder = divmod(totalItems, size)
    
    # Determine the effective item count based on remainder
    if remainder > 0:
        return remainder * (fullGroups + 1)  # Count remainder items with an additional group
    else:
        return totalItems  # No remainder, return total item count

# Read input values for the total items n, another total m, and the group size s
n = int(input())
m = int(input())
s = int(input())

# Calculate and print the product of the processed item counts for n and m
print(mc(n, s) * mc(m, s))
