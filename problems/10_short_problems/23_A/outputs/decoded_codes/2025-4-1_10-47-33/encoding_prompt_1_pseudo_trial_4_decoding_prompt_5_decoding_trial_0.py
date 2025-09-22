# Initialize the program
input_line = input().strip()  # Read and clean the input line
length = len(input_line)  # Store the length of the input line
result = 0  # Initialize result to hold the longest repeating substring length

# Main loop to find the longest repeating substring
for sub_length in range(length):  # For each possible substring length
    for start_index in range(length):  # For each starting position
        # Extract the substring of input_line
        substring = input_line[start_index:start_index + sub_length]
        # Check if the substring appears again in input_line
        if substring in input_line[start_index + 1:]:
            # Update result if a repeating substring is found
            result = sub_length
            break  # Exit the inner loop to check next substring length

# Output the result
print(result)  # Print the length of the longest repeating substring
