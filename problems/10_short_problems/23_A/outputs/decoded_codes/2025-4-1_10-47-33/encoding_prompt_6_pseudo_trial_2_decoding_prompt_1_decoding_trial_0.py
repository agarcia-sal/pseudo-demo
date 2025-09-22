def find_longest_repeated_substring():
    # Read a line of input (excluding newline character)
    line = input()
    length_of_line = len(line)           # Determine the length of the input line
    longest_repeated_length = 0           # Initialize variable for longest repeated substring length

    # Iterate over possible lengths for substrings
    for current_length in range(length_of_line):  # from 0 to length_of_line - 1
        # Check for each starting position within the line
        for start_index in range(length_of_line):  # from 0 to length_of_line - 1
            # Extract the substring of current_length starting at start_index
            substring = line[start_index:start_index + current_length]
            
            # Check if the substring appears again in the line starting from the next character
            if substring in line[start_index + 1:]:
                longest_repeated_length = current_length  # Update longest repeated length
                break   # Exit the inner loop if a repeat is found

    # Output the length of the longest repeated substring
    print(longest_repeated_length)

