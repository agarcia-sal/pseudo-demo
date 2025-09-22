# Read a line of input from the user and remove the trailing newline character
input_line = input()

# Determine the length of the input line
length_of_line = len(input_line)

# Initialize a variable to hold the result
longest_repeated_substring_length = 0

# Loop through possible substring lengths from 1 to length_of_line
for substring_length in range(1, length_of_line):

    # Loop through each starting position in the input line
    for start_index in range(length_of_line - substring_length + 1):

        # Extract a substring from the input line
        current_substring = input_line[start_index:start_index + substring_length]

        # Check if the current substring exists elsewhere in the line after its starting position
        if current_substring in input_line[start_index + 1:]:

            # If found, update the longest repeated substring length
            longest_repeated_substring_length = substring_length
            break  # Stop checking other starting indices for this substring length

# Output the length of the longest repeated substring found
print(longest_repeated_substring_length)
