def read_input_line():
    """Read a line from standard input and return it stripped of trailing newlines."""
    return input().rstrip('\n')

def substring_exists(line, start_position, length):
    """Check if a substring of a given length starting from start_position exists later in the line."""
    if start_position + length > len(line):
        return False
    substring = line[start_position:start_position + length]
    # Check if the substring appears again in the line after the starting position
    return line.find(substring, start_position + 1) != -1

def find_longest_repeated_substring_length():
    """Determine the length of the longest repeated substring in the input line."""
    input_line = read_input_line()
    line_length = len(input_line)
    longest_repeated_length = 0
    
    # Iterate over all possible substring lengths
    for substring_length in range(1, line_length):  # Start from 1 to avoid length 0
        for starting_position in range(line_length):
            if substring_exists(input_line, starting_position, substring_length):
                longest_repeated_length = substring_length
                break  # Found a repeated substring, break inner loop
        else:
            continue  # Continue if no repeated substring found in this length
        break  # Exit both loops if a repeated substring is found
    
    print(longest_repeated_length)

# Call the function to execute the logic
find_longest_repeated_substring_length()
