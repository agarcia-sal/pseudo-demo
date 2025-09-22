def get_user_input():
    """Read input from the user."""
    return input()

def split_string(input_string):
    """Split the input string into a list of values."""
    return input_string.split()

def convert_to_integer(value):
    """Convert a string value to an integer."""
    return int(value)

def main():
    # Read two input strings from the user
    first_string = get_user_input()
    second_string = get_user_input()

    # Split the input strings into a list of values
    values_from_first_string = split_string(first_string)
    values_from_second_string = split_string(second_string)

    # Initialize a counter to track differences
    difference_count = 0 

    # Iterate through the first three elements of both lists
    for index in range(3):  # Ensures indices 0 to 2
        # Convert the string values to integers
        value_from_first = convert_to_integer(values_from_first_string[index])
        value_from_second = convert_to_integer(values_from_second_string[index])

        # Check if the two values are different
        if value_from_first != value_from_second:
            # Increment the difference counter
            difference_count += 1 

    # If the count of differences is less than 3
    if difference_count < 3:
        print("YES")  # Output confirms that the two sets are similar
    else:
        print("NO")   # Output indicates significant differences

# Main execution point of the program
if __name__ == "__main__":
    main()
