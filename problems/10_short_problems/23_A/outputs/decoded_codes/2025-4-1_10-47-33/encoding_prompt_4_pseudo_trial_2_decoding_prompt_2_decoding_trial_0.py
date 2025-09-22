def read_input_line():
    # Read a line of input from standard input and remove the trailing newline
    return input().rstrip('\n')

def substring_exists(line, start_position, length):
    # Extract the substring based on the given start position and length
    substring = line[start_position:start_position + length]
    # Use a search method to check if the substring appears later in the line
    return line.find(substring, start_position + 1) != -1

# Read a line of input and determine the length of the input line
input_line = read_input_line()
line_length = len(input_line)

# Initialize a variable to keep track of the longest repeated substring length
longest_repeated_length = 0

# Iterate over all possible substring lengths from 0 to line_length - 1
for substring_length in range(line_length):
    # Check each starting position in the line for the substring of the current length
    for starting_position in range(line_length):
        # Check if the substring from the current starting position of the given length is found later in the string
        if substring_exists(input_line, starting_position, substring_length):
            # Update the longest repeated length found
            longest_repeated_length = substring_length
            break  # Exit the inner loop as we found a repeated substring

# Output the length of the longest repeated substring
print(longest_repeated_length)
