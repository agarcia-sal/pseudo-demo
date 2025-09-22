def calculate_excess_items(total_items, segment_size):
    quotient = total_items // segment_size
    remainder = total_items % segment_size
    
    # If there are excess items left over from integer division,
    # return the adjusted count based on how many full segments are possible
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return total_items

# Read input values
total_items_from_input = int(input())
another_variable = int(input())
segment_size_from_input = int(input())

# Calculate excess items for both inputs
result_for_total_items = calculate_excess_items(total_items_from_input, segment_size_from_input)
result_for_another_variable = calculate_excess_items(another_variable, segment_size_from_input)

# Final result is the product of both calculations
final_result = result_for_total_items * result_for_another_variable

# Output the final result
print(final_result)
