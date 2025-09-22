def calculate_groups(total_quantity, group_size):
    # Determine how many full groups can be formed
    full_groups = total_quantity // group_size
    # Find the count of extra items
    remainder = total_quantity % group_size

    # Calculate effective groups based on the remainder
    if remainder > 0:
        return remainder * (full_groups + 1)  # Return effective groups if there are extra items
    else:
        return total_quantity  # Return total quantity if no extra items

# Read input values for quantities and group size
quantity1 = int(input())
quantity2 = int(input())
group_size = int(input())

# Calculate effective groups for both quantities
effective_groups_1 = calculate_groups(quantity1, group_size)
effective_groups_2 = calculate_groups(quantity2, group_size)

# Multiply the two effective group values
final_result = effective_groups_1 * effective_groups_2

# Output the final result
print(final_result)
