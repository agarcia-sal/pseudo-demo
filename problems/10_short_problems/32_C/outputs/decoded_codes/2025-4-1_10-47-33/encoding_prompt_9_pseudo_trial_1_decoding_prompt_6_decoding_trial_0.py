def calculate_adjusted_value(total_items, divisor):
    # Calculate the quotient of total_items divided by divisor
    quotient = total_items // divisor
    # Calculate the remainder of total_items divided by divisor
    remainder = total_items % divisor
    
    # Check if there are any items left after forming full groups
    if remainder > 0:
        # Return the product of remainder and (quotient + 1)
        return remainder * (quotient + 1)
    else:
        # Return total_items if there are no leftovers
        return total_items

# Main logic starts here
# Read three integers from user input
total_count1 = int(input())
total_count2 = int(input())
group_size = int(input())

# Calculate the adjusted value for total_count1
adjusted_value1 = calculate_adjusted_value(total_count1, group_size)

# Calculate the adjusted value for total_count2
adjusted_value2 = calculate_adjusted_value(total_count2, group_size)

# Calculate the final result by multiplying the adjusted values
final_result = adjusted_value1 * adjusted_value2

# Print the final result
print(final_result)
