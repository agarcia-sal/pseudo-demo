# Step 1: Read a line of input and remove the trailing newline character
input_line = input().strip()

# Step 2: Determine the length of the input line
length_of_line = len(input_line)

# Step 3: Initialize a variable to hold the length of the longest repeated substring
repeated_substring_length = 0

# Step 4: Iterate over each possible length of substring
for substring_length in range(1, length_of_line):  # Start from 1 to length_of_line - 1
    # Check each starting index for the substring
    for start_index in range(length_of_line - substring_length + 1):  # Ensure we don't go out of bounds
        # Extract the substring
        substring = input_line[start_index:start_index + substring_length]
        
        # Check if this substring can be found later in the input line
        if substring in input_line[start_index + substring_length:]:
            # Update the length of the longest repeated substring found
            repeated_substring_length = substring_length
            # Exit the inner loop since we found a repeated substring
            break
    
# Step 5: Output the value of repeated_substring_length
print(repeated_substring_length)
