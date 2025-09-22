def calculate_adjusted_value(total_items, divisor):
    quotient = total_items // divisor  # Calculate the quotient
    remainder = total_items % divisor   # Calculate the remainder
    
    if remainder > 0:  # Conditional check for remainder
        return remainder * (quotient + 1)  # Return the product of remainder and (quotient + 1)
    else:
        return total_items  # Return total_items as is

# Main logic begins here
total_count1 = int(input())  # Read total_count1 from user input
total_count2 = int(input())  # Read total_count2 from user input
group_size = int(input())     # Read group_size from user input

# Calculate the adjusted value for total_count1
adjusted_value1 = calculate_adjusted_value(total_count1, group_size)

# Calculate the adjusted value for total_count2
adjusted_value2 = calculate_adjusted_value(total_count2, group_size)

# Calculate the final result
final_result = adjusted_value1 * adjusted_value2

# Print the final result
print(final_result)
