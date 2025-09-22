def calculate_groups(total_items, group_size):
    # Calculate the number of complete groups
    quotient = total_items // group_size
    remainder = total_items % group_size
    
    # Check if there is a remaining group
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return total_items

# Read three integers from the user input
total_a = int(input())
total_b = int(input())
group_size = int(input())

# Compute the group values for total_a and total_b
group_value_a = calculate_groups(total_a, group_size)
group_value_b = calculate_groups(total_b, group_size)

# Calculate the product of the two group values
result = group_value_a * group_value_b

# Output the resulting product
print(result)
