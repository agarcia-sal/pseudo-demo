def read_input_line():
    # Function to read a line input and return it
    return input().rstrip()  # Remove the trailing newline character

def substring_exists(line, start_position, length):
    # Extract the substring based on given start position and length
    substring = line[start_position:start_position + length]
    # Check if the substring appears later in the line
    return line.find(substring, start_position + 1) != -1

# Read a line of input from standard input
input_line = read_input_line()

# Determine the length of the input line
line_length = len(input_line)

# Initialize a variable to keep track of the longest repeated substring length
longest_repeated_length = 0

# Iterate over all possible substring lengths from 0 to line_length - 1
for substring_length in range(1, line_length):  # Start from 1 to avoid length 0
    # Check each starting position in the line for the substring of current length
    for starting_position in range(0, line_length - substring_length + 1):
        # Check if the substring exists
        if substring_exists(input_line, starting_position, substring_length):
            # Update the longest repeated length found
            longest_repeated_length = substring_length
            break  # Exit the inner loop as we found a repeated substring

# Output the length of the longest repeated substring
print(longest_repeated_length)
