# Initialize Program
input_line = input().strip()  # Read a line of input and remove trailing newline characters
length = len(input_line)  # Store the length of the input line
result = 0  # Initialize result to 0

# Main Loop
for sub_length in range(length):  # For each possible substring length
    for start_index in range(length):  # For each starting position in the input line
        # Extract substring
        substring = input_line[start_index:start_index + sub_length]
        # Check if this substring appears again in the input line
        if substring in input_line[start_index + 1:]:  # Check if found after the current position
            result = sub_length  # Update result to the current sublength
            break  # Break out of the inner loop to test the next substring length

# Output the Result
print(result)  # Print the length of the longest repeating substring
