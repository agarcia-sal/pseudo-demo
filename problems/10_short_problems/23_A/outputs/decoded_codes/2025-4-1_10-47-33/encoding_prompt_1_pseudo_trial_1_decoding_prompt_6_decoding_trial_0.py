# Read a line of input and remove any trailing newline character
input_line = input().strip()

# Determine the length of the input line
length_of_input = len(input_line)

# Initialize a variable to hold the length of the longest repeated substring
longest_repeated_substring_length = 0

# Loop over possible lengths of substrings from 0 to length_of_input - 1
for current_length in range(length_of_input):
    # Loop through each starting position for the substring
    for start_index in range(length_of_input):
        # Extract the substring of the current length starting at start_index
        current_substring = input_line[start_index:start_index + current_length]
        
        # Check if the current substring appears again in the input line after start_index
        if current_substring in input_line[start_index + 1:]:
            # Update longest repeated substring length to current_length
            longest_repeated_substring_length = current_length
            # Exit the inner loop to check the next current length
            break

# Print the length of the longest repeated substring found
print(longest_repeated_substring_length)
