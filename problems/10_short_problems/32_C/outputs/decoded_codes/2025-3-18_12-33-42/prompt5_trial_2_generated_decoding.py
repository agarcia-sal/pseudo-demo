def calculate_groups(total_items, group_size):
    # Calculate full groups and remainder items
    full_groups = total_items // group_size
    remainder = total_items % group_size
    
    # If there's leftover items, we need to account for an extra group
    if remainder > 0:
        return remainder * (full_groups + 1)
    else:
        return total_items  # No remainder means no additional group

# Read input values for n (total items in first category),
# m (total items in second category), and s (size of each group)
n = int(input())
m = int(input())
s = int(input())

# Calculate the number of effective groups for both categories
effective_groups_for_n = calculate_groups(n, s)
effective_groups_for_m = calculate_groups(m, s)

# Output the product of effective groups for both n and m
result = effective_groups_for_n * effective_groups_for_m
print(result)
