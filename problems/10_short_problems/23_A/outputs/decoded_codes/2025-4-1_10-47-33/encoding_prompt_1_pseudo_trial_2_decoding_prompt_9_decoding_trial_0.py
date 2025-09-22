# Read a line of input and remove the trailing newline character
input_line = input().rstrip()

# Determine the length of the input line
length_of_line = len(input_line)

# Initialize a variable to hold the length of the longest repeated substring
repeated_substring_length = 0

# Iterate over all possible substring lengths
for substring_length in range(1, length_of_line):  # start from 1 to eliminate empty substring
    # Iterate over all possible starting indices
    for start_index in range(length_of_line - substring_length + 1):
        # Extract the substring
        substring = input_line[start_index:start_index + substring_length]
        
        # Check if substring is found again later in the input line
        if substring in input_line[start_index + substring_length:]:
            repeated_substring_length = substring_length
            break  # Exit inner loop if a repeated substring is found

# Output the length of the longest repeated substring
print(repeated_substring_length)
