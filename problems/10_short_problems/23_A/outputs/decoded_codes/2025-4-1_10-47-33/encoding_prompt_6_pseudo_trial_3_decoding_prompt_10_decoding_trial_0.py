def find_longest_repeated_substring_length():
    # Read a line of input from the user
    input_line = input()

    # Determine the length of the input line
    length_of_line = len(input_line)
    
    # Variable to hold the length of the longest repeated substring found
    longest_repeated_substring_length = 0

    # Loop through possible substring lengths
    for substring_length in range(1, length_of_line):  # Starting from 1 to avoid empty substring
        # Loop through each starting index for the substring
        for start_index in range(length_of_line - substring_length + 1):
            # Extract the current substring
            current_substring = input_line[start_index:start_index + substring_length]
            
            # Check if the current substring exists in the input line after its starting position
            if current_substring in input_line[start_index + 1:]:
                longest_repeated_substring_length = substring_length
                break  # Found a repeated substring of this length, break to check next length
        
    # Output the length of the longest repeated substring found
    print(longest_repeated_substring_length)

# Call the function to execute
find_longest_repeated_substring_length()
