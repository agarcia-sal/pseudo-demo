# START

# Read a line of input
input_string = input().strip()  # Remove trailing newline character
length_of_input = len(input_string)
longest_repeated_length = 0

# Loop through all possible substring lengths
for substring_length in range(length_of_input):  # From 0 to length_of_input - 1
    # Check each starting position for the substring
    for starting_position in range(length_of_input):  # From 0 to length_of_input - 1
        # Extract the substring based on current length and starting position
        current_substring = input_string[starting_position:starting_position + substring_length]
        
        # Look for the occurrence of this substring starting after the current position
        if current_substring in input_string[starting_position + 1:]:
            # If found, update the longest repeated length
            longest_repeated_length = substring_length
            break  # Exit the starting position loop

# Output the length of the longest repeating substring found
print(longest_repeated_length)

# END
