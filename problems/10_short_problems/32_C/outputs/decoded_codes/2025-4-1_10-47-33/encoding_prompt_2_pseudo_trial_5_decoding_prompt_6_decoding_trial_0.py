# Define a function that calculates adjusted remainder based on segment size
def calculate_remainder_with_adjustment(total_quantity, segment_size):
    # Calculate how many full segments fit into the total quantity
    full_segments_count = total_quantity // segment_size
    # Calculate the remaining quantity after full segments
    remaining_quantity = total_quantity % segment_size
    
    # If there is a remainder, return the product of remaining quantity and one more than full segments count
    if remaining_quantity > 0:
        return remaining_quantity * (full_segments_count + 1)
    else:
        # If there is no remainder, return total quantity as is
        return total_quantity

# Get input values
total_items_n = int(input())
total_items_m = int(input())
segment_size_s = int(input())

# Calculate adjusted remainders for both total items
adjusted_n = calculate_remainder_with_adjustment(total_items_n, segment_size_s)
adjusted_m = calculate_remainder_with_adjustment(total_items_m, segment_size_s)

# Compute final output by multiplying adjusted_n and adjusted_m
final_result = adjusted_n * adjusted_m

# Display the result
print(final_result)
