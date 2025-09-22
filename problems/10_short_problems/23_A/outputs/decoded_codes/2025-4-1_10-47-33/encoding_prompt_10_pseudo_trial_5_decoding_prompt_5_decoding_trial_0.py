# Importing sys to read input from standard input
import sys

# Read a line of input and strip any trailing newline characters
input_line = input().strip()
# Set 'n' to the length of the input line
length_of_input = len(input_line)
# Initialize result variable 'rv' to 0
result_value = 0

# Loop over each possible length 'l' from 1 to n
for substring_length in range(1, length_of_input):
    # Loop over each starting index 'i' from 0 to n-1
    for start_index in range(length_of_input):
        # Extract the substring of length 'l' starting from index 'i'
        substring = input_line[start_index:start_index + substring_length]
        # Check if this substring appears again in 'line' starting from index 'i + 1'
        if input_line.find(substring, start_index + 1) != -1:
            # If the substring is found, set 'rv' to the length of the substring
            result_value = substring_length
            # Break out of the inner loop as we've found a match
            break

# Print the result value
print(result_value)
