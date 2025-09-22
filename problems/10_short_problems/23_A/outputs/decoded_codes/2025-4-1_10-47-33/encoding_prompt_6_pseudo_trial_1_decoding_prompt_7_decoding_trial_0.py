# Start of the program
# Read a line of input from the user and remove the trailing newline character
line = input().rstrip()  # Remove the last character (newline)
length_of_line = len(line)  # Get the length of the line
repeat_length = 0  # Initialize variable to track the longest repeat length

# Loop through lengths from 0 to length_of_line - 1
for length in range(length_of_line):  # length goes from 0 to length_of_line - 1

    # Check for all starting positions of substring of this length
    for start_position in range(length_of_line):  # start_position goes from 0 to length_of_line - 1
        
        # Extract the current substring from the line
        current_substring = line[start_position:start_position + length + 1]  # Adjust the slice to include the current length

        # Check if this substring appears again in line starting from the next character
        if current_substring in line[start_position + 1:]:  # Check in the line after the start_position
            # Update repeat_length to be the current length if a repeat is found
            repeat_length = length + 1  # Update the repeat length
            break  # Break out of the inner loop if a repeat is found

    # Break out of the outer loop if a repeat has been found
    if repeat_length != 0:  # If repeat_length is not zero, break the outer loop
        break

# Output the longest length of the repeated substring found
print(repeat_length)  # Print the repeat_length
