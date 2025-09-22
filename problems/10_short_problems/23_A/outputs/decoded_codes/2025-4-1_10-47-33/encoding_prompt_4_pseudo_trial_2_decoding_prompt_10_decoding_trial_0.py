def read_input_line():
    """Read a line of input from standard input and return it without the newline character."""
    return input().rstrip('\n')

def substring_exists(line, start_position, length):
    """
    Check if there exists a substring of specified length starting from a specific position
    that appears later in the string.
    
    Parameters:
    line (str): The string to search in.
    start_position (int): The starting index for the substring.
    length (int): The length of the substring to check.
    
    Returns:
    bool: True if the substring appears later, False otherwise.
    """
    # Extract the substring based on given start position and length
    substring = line[start_position:start_position + length]
    # Check if the substring appears later in the line
    return line.find(substring, start_position + 1) != -1

def find_longest_repeated_substring_length():
    """Determines the length of the longest repeated substring in the input line."""
    input_line = read_input_line() # Read the input line
    line_length = len(input_line)   # Determine the length of the input line

    longest_repeated_length = 0      # Initialize the longest repeated substring length

    # Iterate over all possible substring lengths
    for substring_length in range(1, line_length):  # Start from length 1 to avoid empty substring
        # Iterate over all starting positions in the line
        for starting_position in range(line_length - substring_length + 1):
            # Check for the existence of the substring
            if substring_exists(input_line, starting_position, substring_length):
                longest_repeated_length = substring_length
                break  # Exit the inner loop since we found a repeated substring
        else:
            continue  # Continue to the next length if no substring was found
        break  # Exit the outer loop if a substring was found for the current length

    print(longest_repeated_length)  # Output the length of the longest repeated substring

# Execute the function to find the longest repeated substring length
find_longest_repeated_substring_length()
