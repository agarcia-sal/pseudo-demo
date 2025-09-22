# Read a single line of input from the user
input_line = input()  # Store user input
input_length = len(input_line)  # Get the length of the input line
longest_repeated_substring_length = 0  # Initialize variable to store the length of the longest repeated substring

# Loop over possible substring lengths from 1 to input_length - 1
for substring_length in range(1, input_length):  # Start from 1 since a substring of length 0 is not meaningful

    # Check all starting positions in the line for substrings of the current length
    for starting_position in range(input_length - substring_length + 1):  # Adjust to avoid index errors

        # Extract the substring of the specified length starting at the current position
        current_substring = input_line[starting_position:starting_position + substring_length]
        
        # Check if the current substring exists in the line after its starting position
        if current_substring in input_line[starting_position + substring_length:]:
            # If a repeated substring is found, update the longest repeated substring length
            longest_repeated_substring_length = substring_length
            break  # Stop searching once a repeat is found

# Output the length of the longest repeated substring found
print(longest_repeated_substring_length)
