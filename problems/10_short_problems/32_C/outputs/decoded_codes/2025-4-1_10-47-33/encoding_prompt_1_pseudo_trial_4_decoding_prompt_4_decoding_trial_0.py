def calculate_excess_items(total_items, segment_size):
    """
    Calculate the number of excess items when dividing total_items into segments of segment_size.

    :param total_items: Total number of items.
    :param segment_size: Size of each segment.
    :return: The number of excess items based on segments.
    """
    quotient, remainder = divmod(total_items, segment_size)
    
    if remainder > 0:
        return remainder * (quotient + 1)
    else:
        return total_items


# Read inputs
total_items_from_input = int(input())
another_variable = int(input())
segment_size_from_input = int(input())

# Calculate results for the input variables
result_for_total_items = calculate_excess_items(total_items_from_input, segment_size_from_input)
result_for_another_variable = calculate_excess_items(another_variable, segment_size_from_input)

# Calculate the final result
final_result = result_for_total_items * result_for_another_variable

# Output the final result
print(final_result)
