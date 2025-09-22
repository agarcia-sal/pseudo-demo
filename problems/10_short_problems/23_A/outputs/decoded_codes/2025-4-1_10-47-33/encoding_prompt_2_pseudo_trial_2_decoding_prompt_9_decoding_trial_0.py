# Read input from standard input and remove trailing newline
input_line = input().strip()
line_length = len(input_line)

# Initialize variable to track maximum length of substring found with repetitions
max_length = 0

# Outer loop for each possible substring length
for current_length in range(1, line_length):  # start from 1 to avoid empty substring
    # Inner loop for each character index
    for current_index in range(line_length - current_length + 1):  
        # Extract substring
        sub_string = input_line[current_index:current_index + current_length]
        
        # Check for repetition of the substring
        if input_line.find(sub_string, current_index + current_length) != -1:
            # Update maximum length if the substring is found again
            max_length = current_length
            break  # Exit inner loop as we found a repetition

# Output the result
print(max_length)
