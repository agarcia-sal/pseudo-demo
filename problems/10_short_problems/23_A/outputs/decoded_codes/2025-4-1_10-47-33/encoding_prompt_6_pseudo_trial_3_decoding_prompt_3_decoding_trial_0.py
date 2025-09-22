# Function to find the length of the longest repeated substring
def longest_repeated_substring():
    # Read a line of input from the user
    input_line = input().rstrip()

    # Determine the length of the input line
    length_of_line = len(input_line)

    # Initialize a variable to hold the result
    longest_repeated_substring_length = 0

    # Loop through possible substring lengths
    for substring_length in range(1, length_of_line):  # Start from 1 to avoid empty substrings
        # Loop through each starting position in the input line
        for start_index in range(length_of_line - substring_length + 1):
            # Extract a substring
            current_substring = input_line[start_index:start_index + substring_length]

            # Check if the current substring can be found elsewhere in the line
            if current_substring in input_line[start_index + 1:]:
                # If found, update the longest repeated substring length
                longest_repeated_substring_length = substring_length
                break  # Stop checking other starting indices for this substring length

    # Output the length of the longest repeated substring found
    print(longest_repeated_substring_length)

# Call the function
longest_repeated_substring()
