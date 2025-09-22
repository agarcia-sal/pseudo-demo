# Function to read input line (simulation of stdin function)
def read_input_line():
    return input().rstrip('\n')  # Reads input and removes trailing newline

# Function to check if there exists a substring of a given length starting from a specific position
def substring_exists(line, start_position, length):
    substring = line[start_position:start_position + length]
    return line.find(substring, start_position + 1) != -1

# Main logic
input_line = read_input_line()  # Read a line of input
line_length = len(input_line)  # Determine the length of the input line

longest_repeated_length = 0  # Initialize longest repeated substring length

# Iterate over all possible substring lengths from 0 to line_length
for substring_length in range(line_length):  # 0 to line_length - 1
    # Check each starting position in the line for the substring of current length
    for starting_position in range(line_length):  # 0 to line_length - 1
        # Check if the substring from the current starting position of the given length is found later in the string
        if substring_exists(input_line, starting_position, substring_length):
            # Update the longest repeated length found
            longest_repeated_length = substring_length
            break  # Exit the inner loop as we found a repeated substring

# Output the length of the longest repeated substring
print(longest_repeated_length)
