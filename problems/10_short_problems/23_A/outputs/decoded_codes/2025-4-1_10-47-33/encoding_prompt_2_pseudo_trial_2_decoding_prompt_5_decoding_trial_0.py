# Read input from the user
input_line = input().rstrip()  # Remove trailing newline character
line_length = len(input_line)   # Obtain the length of the input line

# Initialize variable to track maximum length of repeating substring
max_length = 0

# Outer loop for each possible substring length
for current_length in range(1, line_length):  # Start from length 1 to line_length - 1
    # Inner loop to explore possible starting indices for substrings
    for current_index in range(line_length):
        # Extract the substring based on current index and length
        sub_string = input_line[current_index:current_index + current_length]
        
        # Check if the substring is found in the remaining part of the string
        if input_line.find(sub_string, current_index + 1) != -1:
            # Update max_length if the substring is repeated
            max_length = current_length
            break  # Exit the inner loop since we found a repetition

# Output the maximum length of the repeating substring 
print(max_length)
