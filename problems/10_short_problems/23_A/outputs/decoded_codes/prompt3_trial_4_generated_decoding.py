def longest_repeated_substring_length():
    # Read a line of input and remove the trailing newline character
    line = input().strip()
    length_of_line = len(line)
    longest_repeated_substring_length = 0

    # Loop through all possible lengths of substrings
    for length in range(length_of_line):
        # Loop through each starting point i for the substring
        for start_index in range(length_of_line):
            # Create the substring from start_index for the current length
            current_substring = line[start_index:start_index + length + 1]
            
            # Check if this substring appears again in the line, starting after startIndex
            if line.find(current_substring, start_index + 1) != -1:
                # Update the longest found repeated substring length
                longest_repeated_substring_length = length + 1
                break  # Break out of inner loop if a repeat is found

    # Output the length of the longest repeated substring found
    print(longest_repeated_substring_length)

# Call the function to execute
longest_repeated_substring_length()
