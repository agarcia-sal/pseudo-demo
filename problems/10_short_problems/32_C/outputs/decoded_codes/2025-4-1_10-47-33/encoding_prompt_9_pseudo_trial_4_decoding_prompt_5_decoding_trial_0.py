def calculate_groups(total_items, group_size):
    # Calculate how many complete groups can be formed
    quotient = total_items // group_size
    remainder = total_items % group_size
    
    # If there is a remainder, return remainder multiplied by (quotient + 1)
    if remainder != 0:
        return remainder * (quotient + 1)
    else:
        return total_items

# Read input values
total_a = int(input())
total_b = int(input())
group_size = int(input())

# Compute group values for totalA and totalB
value_a = calculate_groups(total_a, group_size)
value_b = calculate_groups(total_b, group_size)

# Calculate and print the result
result = value_a * value_b
print(result)
