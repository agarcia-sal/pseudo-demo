# Start of the program

# Read a line of input and remove the trailing newline character
input_line = input()
length_of_input = len(input_line)  # Get the length of the input line
longest_repeated_length = 0  # Variable to store the length of longest repeated substring

# Loop through all possible substring lengths from 0 to (length of input - 1)
for substring_length in range(length_of_input):  # substring_length from 0 to length_of_input - 1
    # Loop through all starting positions of the substring in the input
    for start_index in range(length_of_input):  # start_index from 0 to length_of_input - 1
        # Extract the current substring based on the start_index and substring_length
        current_substring = input_line[start_index:start_index + substring_length]

        # Check if the current substring appears again in the input beyond its starting position
        if (input_line.find(current_substring, start_index + 1) != -1):  # find function checks if the substring exists after start_index
            # If it does, update the length of the longest repeated substring found
            longest_repeated_length = substring_length
            break  # Break out of inner loop since a repeat was found

# Output the length of the longest repeated substring
print(longest_repeated_length)

# End of the program
