def find_longest_repetition():
    # Read a line of input and strip any trailing newline characters
    string_line = input().strip()
    
    # Determine the length of the input line
    length_of_line = len(string_line)

    # Initialize a variable to store the length of the longest repeated substring
    longest_repetition_length = 0

    # Loop over all possible lengths for repeated substrings
    for current_length in range(1, length_of_line):  # Start from 1 to avoid zero-length substrings
        # Loop through the string to check for repeated substrings
        for start_index in range(length_of_line - current_length):
            # Extract the substring of the current length starting from start_index
            substring = string_line[start_index:start_index + current_length]

            # Check if the substring appears again in the string after its starting index
            if substring in string_line[start_index + current_length:]:
                # If found, update the longest repetition length
                longest_repetition_length = current_length
                break  # Exit the inner loop early if a repetition is found

    # Output the length of the longest repeated substring
    print(longest_repetition_length)

# Call the function to execute it
find_longest_repetition()
