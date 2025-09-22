def mc(total_items, size):
    # Calculate how many full groups can fit
    full_groups, remainder = divmod(total_items, size)
    
    # Determine the effective item count based on remainder
    if remainder > 0:
        return remainder * (full_groups + 1)  # Count remainder items with an additional group
    else:
        return total_items  # No remainder, return total item count

# Read input values for the total items n, additional total m, and the group size s
total_items_n = int(input())
additional_total_m = int(input())
group_size_s = int(input())

# Calculate and print the product of the processed item counts for n and m
result = mc(total_items_n, group_size_s) * mc(additional_total_m, group_size_s)
print(result)
