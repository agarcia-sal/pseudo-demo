def adjust_number(total_items, group_size):
    # Calculate how many complete groups can be formed
    complete_groups = total_items // group_size
    # Calculate the remainder of items not fitting into a complete group
    remainder = total_items % group_size
    
    # If there is a remainder, adjust the return value accordingly
    if remainder > 0:
        return remainder * (complete_groups + 1)
    else:
        return total_items

# Input: read three integers from user input
total_items1 = int(input())
total_items2 = int(input())
group_size = int(input())

# Process: call the adjust_number function for both items
adjusted_value1 = adjust_number(total_items1, group_size)
adjusted_value2 = adjust_number(total_items2, group_size)

# Output: calculate and print the product of the adjusted values
final_product = adjusted_value1 * adjusted_value2
print(final_product)
