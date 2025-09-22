def find_longest_repeated_substring():
    # Read a line of input and remove the trailing newline character
    input_line = input().strip()
    length_of_line = len(input_line)
    repeated_substring_length = 0  # Initialize to store the length of the longest repeated substring

    # Loop through all possible lengths of substrings
    for substring_length in range(1, length_of_line):  # Starting from 1 to avoid empty substring
        # Check each starting index for the current substring length
        for start_index in range(length_of_line - substring_length + 1):
            # Extract the substring of the current length
            substring = input_line[start_index:start_index + substring_length]
            # Check if this substring can be found in the rest of the string
            if substring in input_line[start_index + substring_length:]:
                repeated_substring_length = substring_length
                break  # Exit the inner loop once we find a repeated substring
        else:
            continue  # Only executed if the inner loop did NOT break
        break  # Exit the outer loop if we found a repeated substring of this length

    # Output the length of the longest repeated substring
    print(repeated_substring_length)

# Call the function to execute
find_longest_repeated_substring()
