def calculate_adjusted_value(total_items, divisor):
    # Calculate the quotient (number of full groups)
    quotient = total_items // divisor
    # Calculate the remainder (items left after full groups)
    remainder = total_items % divisor
    
    # Check if there are any remaining items
    if remainder > 0:
        # Return product of remainder and (quotient + 1)
        return remainder * (quotient + 1)
    else:
        # Return total_items as there are no remainders
        return total_items

# Main logic begins here
# Read three integers from user input
total_count1 = int(input())
total_count2 = int(input())
group_size = int(input())

# Calculate adjusted value for total_count1
adjusted_value1 = calculate_adjusted_value(total_count1, group_size)

# Calculate adjusted value for total_count2
adjusted_value2 = calculate_adjusted_value(total_count2, group_size)

# Calculate the final result
final_result = adjusted_value1 * adjusted_value2

# Print final_result
print(final_result)
