def find_longest_repetition():
    # Read a line of input and remove the trailing newline character
    string_line = input().strip()

    # Determine the length of the input line
    length_of_line = len(string_line)

    # Initialize a variable to store the result
    longest_repetition_length = 0

    # Loop over all possible lengths for repeated substrings
    for current_length in range(length_of_line):
        # Loop through the string to check for repeated substrings
        for start_index in range(length_of_line):
            # Extract the substring of the current length starting from start_index
            if start_index + current_length < length_of_line:
                substring = string_line[start_index:start_index + current_length + 1]
                
                # Check if the substring appears again in the string after its starting index
                if substring in string_line[start_index + current_length + 1:]:
                    # If found, update the longest repetition length
                    longest_repetition_length = current_length + 1
                    break  # Move to the next length since we've found a repetition

    # Output the length of the longest repeated substring
    print(longest_repetition_length)

# Test the function after defining it
find_longest_repetition()
