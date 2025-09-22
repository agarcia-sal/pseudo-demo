def calculate_groups(total_quantity, group_size):
    # Determine how many full groups can be formed
    full_groups = total_quantity // group_size
    # Find the count of extra items
    remainder = total_quantity % group_size

    # If there is a remainder, calculate effective groups
    if remainder > 0:
        return remainder * (full_groups + 1)  # Extra items contribute to additional groups
    else:
        return total_quantity  # No extra items, return total quantity

# Read input values
quantity1 = int(input())
quantity2 = int(input())
group_size = int(input())

# Calculate effective groups for both quantities
effective_groups1 = calculate_groups(quantity1, group_size)
effective_groups2 = calculate_groups(quantity2, group_size)

# Multiply the two effective group values
final_result = effective_groups1 * effective_groups2

# Output the final result
print(final_result)
