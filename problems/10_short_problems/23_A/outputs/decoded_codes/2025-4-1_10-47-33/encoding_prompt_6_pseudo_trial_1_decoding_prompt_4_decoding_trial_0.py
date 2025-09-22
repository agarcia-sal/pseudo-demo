# Read a line of input from the user
line = input().rstrip()  # Remove the trailing newline character
length_of_line = len(line)  # Get the length of the line
repeat_length = 0  # Initialize the maximum repeat length

# Loop through possible substring lengths
for length in range(length_of_line):
    # Check for all starting positions of substring of this length
    for start_position in range(length_of_line):
        # Extract the current substring from the line
        current_substring = line[start_position:start_position + length]

        # Check if the substring appears again in the line from the next character
        if current_substring in line[start_position + 1:]:
            # Update repeat_length if a repeat is found
            repeat_length = length
            break  # Break out of inner loop

    # Break out of the outer loop if a repeat has been found
    if repeat_length != 0:
        break

# Output the longest length of repeated substring found
print(repeat_length)
