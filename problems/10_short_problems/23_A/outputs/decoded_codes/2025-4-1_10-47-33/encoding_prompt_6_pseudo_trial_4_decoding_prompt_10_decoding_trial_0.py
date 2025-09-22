def find_longest_repeated_substring_length():
    # Read a line of input and remove the trailing newline character
    string_line = input().strip()

    # Determine the length of the input line
    length_of_line = len(string_line)

    # Initialize a variable to store the result for the longest repetition length
    longest_repetition_length = 0

    # Loop over all possible lengths for repeated substrings
    for current_length in range(1, length_of_line):  # start from 1 to avoid empty substring
        # Loop through the string to check for repeated substrings
        for start_index in range(length_of_line - current_length + 1):
            # Extract the substring of the current length starting from start_index
            substring = string_line[start_index:start_index + current_length]

            # Check if the substring appears again in the string after its starting index
            if substring in string_line[start_index + current_length:]:
                # If found, update the longest repetition length
                longest_repetition_length = current_length
                break  # Break out of the inner loop, move to the next length

    # Output the length of the longest repeated substring
    print(longest_repetition_length)

# Call the function to execute the logic
find_longest_repeated_substring_length()
