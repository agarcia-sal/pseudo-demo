def calculate_excess_items(total_items, segment_size):
    # Calculate quotient and remainder from the division of total_items by segment_size
    quotient = total_items // segment_size
    remainder = total_items % segment_size
    
    # If there's a remainder, calculate excess items
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return total_items

# Read inputs
total_items_from_input = int(input())
another_variable = int(input())
segment_size_from_input = int(input())

# Calculate excess items for both total_items and another_variable
result_for_total_items = calculate_excess_items(total_items_from_input, segment_size_from_input)
result_for_another_variable = calculate_excess_items(another_variable, segment_size_from_input)

# Calculate final result as the product
final_result = result_for_total_items * result_for_another_variable

# Output the final result
print(final_result)
