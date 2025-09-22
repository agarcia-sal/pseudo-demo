# Read a line of input from the user
input_line = input().rstrip()  # Remove the trailing newline character
length_of_line = len(input_line)  # Get the length of the line
repeat_length = 0  # This will hold the length of the longest repeating substring

# Iterate over possible lengths of substrings
for substring_length in range(length_of_line):  # Iterate from 0 to length - 1
    # Check each starting index for the substring
    for start_index in range(length_of_line):  # Iterate from 0 to length - 1
        # Extract the substring of the current length starting at start_index
        current_substring = input_line[start_index:start_index + substring_length]
        
        # Check if this substring appears again in the line starting after start_index
        if current_substring in input_line[start_index + 1:]:  # Check in the remaining string
            # If found, update the longest repeating substring length
            repeat_length = substring_length
            break  # Exit the inner loop if we found a repeat

# Output the length of the longest repeating substring
print(repeat_length)
