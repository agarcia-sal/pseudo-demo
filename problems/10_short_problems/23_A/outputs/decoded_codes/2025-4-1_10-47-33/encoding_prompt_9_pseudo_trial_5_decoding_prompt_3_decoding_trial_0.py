def longest_repeated_substring():
    # Get the input string from the user
    input_string = input().strip()
    string_length = len(input_string)
    longest_repeated_substring_length = 0  # Initialize the max length of repeated substring found

    # Iterate over possible substring lengths
    for current_length in range(1, string_length):  # Start from 1 to avoid empty substring
        for start_position in range(string_length - current_length + 1):  # Valid start positions for given length
            # Extract the substring from the current start_position
            substring = input_string[start_position:start_position + current_length]
            # Check for the presence of this substring further in the string
            if substring in input_string[start_position + 1:]:  # Search in the remainder of the string
                longest_repeated_substring_length = current_length  # Update the max length
                break  # Exit the inner loop since we found a valid repeated substring

    # Output the length of the longest repeated substring found
    print(longest_repeated_substring_length)

# Call the function to execute
longest_repeated_substring()
