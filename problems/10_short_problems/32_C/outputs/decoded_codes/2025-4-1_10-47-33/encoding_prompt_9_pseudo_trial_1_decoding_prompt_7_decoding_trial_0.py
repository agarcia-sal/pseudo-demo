def calculate_adjusted_value(total_items, divisor):
    # Calculate the quotient and remainder
    quotient = total_items // divisor
    remainder = total_items % divisor
    
    # If there are items left over after forming full groups
    if remainder > 0:
        # Return the product of the remainder and the value (quotient + 1)
        return remainder * (quotient + 1)
    else:
        # Return total_items as is if there's no remainder
        return total_items

# Main logic starts here
# Read integers from user input
total_count1 = int(input())
total_count2 = int(input())
group_size = int(input())

# Calculate the adjusted value for total_count1
adjusted_value1 = calculate_adjusted_value(total_count1, group_size)

# Calculate the adjusted value for total_count2
adjusted_value2 = calculate_adjusted_value(total_count2, group_size)

# Calculate the final result as the product of the two adjusted values
final_result = adjusted_value1 * adjusted_value2

# Print the final result
print(final_result)
