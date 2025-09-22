# Step 1: Read input from user and remove trailing newline character
input_line = input().strip()

# Step 2: Determine the length of the input line
line_length = len(input_line)

# Step 3: Initialize variable to track maximum length of repeated substring
max_length = 0

# Step 4: Outer loop to iterate through possible substring lengths
for current_length in range(line_length):
    # Inner loop to iterate through each character index
    for current_index in range(line_length):
        # Step 6: Ensure we don't go out of bounds when extracting substring
        if current_index + current_length > line_length:
            break
        
        # Extract the substring
        sub_string = input_line[current_index:current_index + current_length]
        
        # Check for repetition of sub_string in the remaining part of the input_line
        if sub_string in input_line[current_index + 1:]:
            # Update maximum length if we found a repeated substring
            max_length = current_length + 1  # +1 because current_length is 0-indexed
            break  # Exit inner loop if repetition is found

# Step 7: Output the result, length of the longest repeated substring
print(max_length)
