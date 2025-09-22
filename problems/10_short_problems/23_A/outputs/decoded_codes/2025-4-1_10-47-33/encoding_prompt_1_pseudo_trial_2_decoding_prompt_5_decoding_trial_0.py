# Read a line of input and remove the trailing newline character
input_line = input().strip()

# Determine the length of the input line
length_of_line = len(input_line)

# Initialize a variable to hold the length of the longest repeated substring
repeated_substring_length = 0

# Loop over each possible substring length
for substring_length in range(1, length_of_line):  # Starting from 1 as 0 length doesn't count
    # Check for each starting index in the input line
    for start_index in range(length_of_line - substring_length + 1):
        # Extract the substring
        substring = input_line[start_index:start_index + substring_length]
        
        # Check if this substring appears later in the string
        if substring in input_line[start_index + substring_length:]:
            repeated_substring_length = substring_length  # Update the length of the longest repeated substring
            break  # Exit the inner loop as we found a repeated substring of current length

# Output the length of the longest repeated substring
print(repeated_substring_length)
