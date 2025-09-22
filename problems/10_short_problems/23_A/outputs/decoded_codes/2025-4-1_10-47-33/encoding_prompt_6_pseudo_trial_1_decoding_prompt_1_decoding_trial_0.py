# Begin execution

# Read a line of input from the user and remove the trailing newline character
line = input()
line = line[:-1]  # Remove the last character
length_of_line = len(line)  # Set length_of_line to the length of line
repeat_length = 0  # Initialize repeat_length to 0

# Loop through lengths from 0 to length_of_line - 1
for length in range(length_of_line):  # Equivalent to FOR length from 0 to length_of_line - 1
    # Check for all starting positions of substring of this length
    for start_position in range(length_of_line):  # Equivalent to FOR start_position from 0 to length_of_line - 1
        # Extract the current substring from the line
        current_substring = line[start_position:start_position + length + 1]  # Get substring from start_position to (start_position + length)

        # Check if this substring appears again in line starting from the next character
        if current_substring in line[start_position + 1:]:  # Look for current_substring in the rest of the line
            # Update repeat_length to be the current length if a repeat is found
            repeat_length = length
            break  # Break out of inner loop

    # Break out of the outer loop if a repeat has been found
    if repeat_length != 0:  # Check if repeat_length is not equal to 0
        break  # Break out of outer loop

# Output the longest length of repeated substring found
print(repeat_length)  # Print repeat_length

# End execution
