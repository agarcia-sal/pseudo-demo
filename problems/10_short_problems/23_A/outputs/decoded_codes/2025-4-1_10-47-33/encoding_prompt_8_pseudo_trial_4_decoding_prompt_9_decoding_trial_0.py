# Step 1: Read input
input_line = input().strip()  # Read a line of text input and eliminate trailing newlines

# Step 2: Initialize variables
length_of_input = len(input_line)  # Get the length of the input string
max_length = 0  # Initialize maxLength to track the longest repeated substring

# Step 3: Check for repeated substrings
for current_length in range(length_of_input):  # Loop through lengths from 0 to length_of_input - 1
    for start_index in range(length_of_input):  # Loop through all possible starting positions
        # Ensure we only extract valid substrings
        if start_index + current_length <= length_of_input:
            substring = input_line[start_index:start_index + current_length]  # Extract the substring
            
            # Step 6: Check if the substring appears again after its position
            if input_line.find(substring, start_index + 1) != -1:  # Check for repeats
                max_length = current_length  # Update maxLength
                break  # No need to check further for this substring length
            
# Step 7: Output the result
print(max_length)  # Print the maximum length of the repeated substring found
