def calculate_excess_items(total_items, segment_size):
    # Divide total_items by segment_size to get quotient and remainder
    quotient = total_items // segment_size
    remainder = total_items % segment_size
    
    # Check if there is remainder
    if remainder > 0:
        # Return remainder multiplied by (quotient plus one)
        return remainder * (quotient + 1)
    else:
        # Return total_items if there is no remainder
        return total_items

# Read input values from user
total_items_from_input = int(input())
another_variable = int(input())
segment_size_from_input = int(input())

# Calculate results using the CalculateExcessItems function
result_for_total_items = calculate_excess_items(total_items_from_input, segment_size_from_input)
result_for_another_variable = calculate_excess_items(another_variable, segment_size_from_input)

# Calculate the final result
final_result = result_for_total_items * result_for_another_variable

# Output the final result
print(final_result)
