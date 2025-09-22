def split_string(input_string):
    """Splits the input string into a list based on spaces."""
    return input_string.split()

def convert_to_integer(string_value):
    """Converts a string to an integer safely."""
    try:
        return int(string_value)
    except ValueError:
        raise ValueError(f"Unable to convert '{string_value}' to an integer.")

def do_main():
    """Main procedure to read input, compare values, and output result."""
    # Read two input strings from the user
    first_input = input()
    second_input = input()

    # Split the input strings into lists of substrings
    first_list = split_string(first_input)
    second_list = split_string(second_input)

    # Check if the lists have the expected length
    if len(first_list) != 3 or len(second_list) != 3:
        print("Both inputs must contain exactly 3 elements.")
        return

    # Initialize a counter for differing elements
    difference_count = 0 

    # Iterate over the indices for the lists
    for index in range(3):
        # Convert the elements to integers
        first_number = convert_to_integer(first_list[index])
        second_number = convert_to_integer(second_list[index])

        # Compare the corresponding elements
        if first_number != second_number:
            # Increment the counter if they are different
            difference_count += 1

    # Check how many elements differ
    if difference_count < 3:
        print("YES")  # Output "YES" if less than 3 differences
    else:
        print("NO")   # Output "NO" if 3 or more differences

if __name__ == "__main__":
    do_main()
