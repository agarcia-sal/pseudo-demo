# Step 1: Read input
input_line = input().strip()  # Read user input and remove any trailing newline

# Step 2: Initialize variables
length_of_input = len(input_line)  # Length of the input string
max_length = 0  # To track the length of the longest repeated substring

# Step 3: Check for repeated substrings
for current_length in range(1, length_of_input):  # Start from length 1 to length_of_input - 1
    for start_index in range(length_of_input):  # Starting index for substring extraction
        if start_index + current_length <= length_of_input:  # Ensure the substring fits within the input
            substring = input_line[start_index:start_index + current_length]  # Extract substring
            
            # Step 6: Check if the substring appears again after its position
            if input_line.find(substring, start_index + 1) != -1:  # Check if substring found after start_index
                max_length = current_length  # Update max_length
                break  # No need to check further, move to next current_length

# Step 7: Output the result
print(max_length)  # Print the length of the longest repeated substring found
