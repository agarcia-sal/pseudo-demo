# Initialize Program
input_line = input().strip()  # Read input and remove any trailing newline characters
length_of_input = len(input_line)  # Store the length of the input line
result = 0  # Initialize result to 0

# Main Loop
for sub_length in range(length_of_input):  # Iterate over possible substring lengths
    for start_index in range(length_of_input):  # Iterate over start positions for substrings
        substring = input_line[start_index:start_index+sub_length]  # Extract substring
        
        # Check if the substring appears again starting from start_index + 1
        if substring and substring in input_line[start_index + 1:]:
            result = sub_length  # Update result with current substring length
            break  # Break inner loop to check the next substring length

# Output the Result
print(result)  # Print the length of the longest repeating substring
