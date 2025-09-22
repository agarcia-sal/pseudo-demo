def can_transform_string():
    # Gather input strings
    first_input = input()  # Read the first string
    second_input = input()  # Read the second string

    # Process strings to remove spaces
    first_string = [char for char in first_input if char != ' ']
    second_string = [char for char in second_input if char != ' ']

    # Initialize frequency differences list
    frequency_differences = [0] * ASCII_RANGE  # Using a constant to define array length

    # Define ASCII range for characters 'A' to 'z'
    ASCII_RANGE = 123  # According to a valid range

    # Calculate frequency differences
    for char_code in range(65, ASCII_RANGE):  # Loop from 'A' (65) to 'z' (122)
        first_count = first_string.count(chr(char_code))
        second_count = second_string.count(chr(char_code))

        # Store the difference in frequencies
        frequency_differences[char_code] = first_count - second_count

    # Determine validity of transformation
    can_transform = all(diff >= 0 for diff in frequency_differences)

    # Output the result
    if can_transform:
        print("YES")
    else:
        print("NO")

# Call the function
can_transform_string()
