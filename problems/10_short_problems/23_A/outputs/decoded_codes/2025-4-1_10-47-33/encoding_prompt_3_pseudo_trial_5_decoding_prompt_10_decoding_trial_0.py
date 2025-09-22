def find_longest_repeating_substring():
    # Read input line from standard input
    input_line = input().rstrip()  # Remove trailing newline
    line_length = len(input_line)
    repeat_index = 0  # Initialize the repeat index

    # Loop over lengths of possible substrings
    for length in range(1, line_length):  # Starting from 1 to avoid empty substring
        # Inner loop to check each starting position of the substring
        for start_index in range(line_length - length):  # Adjusted to prevent out of range
            # Create a substring of current length starting at start_index
            current_substring = input_line[start_index:start_index + length]

            # Check if the substring appears in the rest of the string after start_index
            if current_substring in input_line[start_index + 1:]:
                # Update repeat_index to the current length if a repeat is found
                repeat_index = length

    # Output the highest length of the repeated substring found
    print(repeat_index)


# Call the main function to execute the code
if __name__ == "__main__":
    find_longest_repeating_substring()
