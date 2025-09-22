def calculate_adjusted_value(total_items, divisor):
    """
    Calculate an adjusted value based on total_items and a divisor.
    
    If there are leftover items after forming complete groups, the function
    returns the product of the remainder and (quotient + 1).
    Otherwise, it returns total_items unmodified.
    
    Parameters:
    total_items (int): The total number of items.
    divisor (int): The divisor for grouping items.
    
    Returns:
    int: The adjusted value based on the specified logic.
    """
    quotient = total_items // divisor  # Calculate how many complete groups can be formed
    remainder = total_items % divisor   # Calculate the leftover items
    
    if remainder > 0:
        return remainder * (quotient + 1)  # Return the product of remainder and (quotient + 1)
    else:
        return total_items  # Return total_items as is


# Main logic starts here
# Read three integers from user input
total_count1 = int(input())
total_count2 = int(input())
group_size = int(input())

# Calculate the adjusted values
adjusted_value1 = calculate_adjusted_value(total_count1, group_size)
adjusted_value2 = calculate_adjusted_value(total_count2, group_size)

# Calculate the final result
final_result = adjusted_value1 * adjusted_value2

# Print the final result
print(final_result)
