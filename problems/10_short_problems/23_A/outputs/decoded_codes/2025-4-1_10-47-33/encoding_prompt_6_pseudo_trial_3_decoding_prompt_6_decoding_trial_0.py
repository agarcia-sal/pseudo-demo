# Begin the program execution

# Read a line of input from the user
input_line = input().strip()  # Removing any trailing newline or spaces

# Determine the length of the input line
length_of_line = len(input_line)

# Initialize a variable to hold the result
longest_repeated_substring_length = 0

# Loop through possible substring lengths from 0 to length_of_line - 1
for substring_length in range(length_of_line):  # Looping through possible lengths

    # Loop through each starting position in the input line
    for start_index in range(length_of_line):  # Looping through each starting index
        
        # Extract a substring from the input line
        current_substring = input_line[start_index:start_index + substring_length + 1]
        
        # Check if the current substring can be found elsewhere in the line after its starting position
        if current_substring in input_line[start_index + 1:]:  # Check if exists in the remaining part
            # If found, update the longest repeated substring length
            longest_repeated_substring_length = substring_length + 1  # +1 because range is exclusive
            break  # Stop checking other starting indices for this substring length

# Output the length of the longest repeated substring found
print(longest_repeated_substring_length)
