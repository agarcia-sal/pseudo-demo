def main():
    # Read input values
    input_values = list(map(int, input().split()))
    total_items = input_values[0]  # This is 'n'
    other_items = input_values[1]   # This is 'm'
    segment_size = input_values[2]   # This is 's'

    # Calculate and print the product
    result = calculate_product(total_items, other_items, segment_size)
    print(result)

def calculate_product(total_count, additional_count, segment_size):
    # Calculate the segments required for total_count
    total_segments = calculate_segments(total_count, segment_size)

    # Calculate the segments required for additional_count
    additional_segments = calculate_segments(additional_count, segment_size)

    # Return the product of segments
    return total_segments * additional_segments

def calculate_segments(item_count, segment_size):
    # Divide item_count into full segments and get remainder
    quotient, remainder = divmod(item_count, segment_size)

    # Calculate the segments based on the remainder
    if remainder > 0:
        return remainder * (quotient + 1)  # Includes the partial segment
    else:
        return item_count  # No partial segment needed

# Call the main function to execute
if __name__ == "__main__":
    main()
