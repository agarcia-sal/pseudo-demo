def find_longest_repeated_substring():
    # Read a line of input and remove any trailing newline characters
    line = input().strip()
    length_of_line = len(line)  # Determine the length of the input line
    longest_repeated_length = 0  # Initialize variable to track the longest repeated substring length

    # Iterate over possible lengths for substrings
    for current_length in range(1, length_of_line):  # Start from length 1 to avoid empty substrings
        found = False  # Flag to check if a repeat is found
        # Check for each starting position within the line
        for start_index in range(length_of_line - current_length + 1):
            # Extract the substring of current_length starting at start_index
            substring = line[start_index:start_index + current_length]

            # Check if the substring appears again in the line starting from the next character
            if substring in line[start_index + 1:]:
                longest_repeated_length = current_length  # Update longest repeated length
                found = True  # Update found flag
                break  # Exit the inner loop if a repeat is found
        
        if found:  # If a repeated substring was found, move on to the next length
            continue

    # Output the length of the longest repeated substring
    print(longest_repeated_length)

# Example call to the function to test it
find_longest_repeated_substring()
