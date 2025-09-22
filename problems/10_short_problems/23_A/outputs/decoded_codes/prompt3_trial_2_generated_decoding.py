def longest_repeated_substring_length():
    # Read input line from the system input and remove the last character (newline)
    input_line = input().rstrip()  # Use rstrip to remove trailing newline
    line_length = len(input_line)
    longest_repeated_length = 0  # This will store the length of the longest repeated substring

    # Iterate through possible substring lengths from 0 to lineLength - 1
    for length in range(line_length):
        # Iterate through each starting index of the substring in the input line
        for start_index in range(line_length):
            # Check if the current starting index will allow for a valid substring of the desired length
            if start_index + length < line_length:
                # Extract the substring of the current length starting at start_index
                current_substring = input_line[start_index:start_index + length + 1]  # +1 to include the current length

                # Check if the substring occurs later in the string (after startIndex)
                if current_substring in input_line[start_index + 1:]:
                    longest_repeated_length = length + 1  # Update the result (add 1 for length)
                    break  # No need to check further for this length

    # Output the length of the longest repeated substring found
    print(longest_repeated_length)

# Call the function to execute
longest_repeated_substring_length()
