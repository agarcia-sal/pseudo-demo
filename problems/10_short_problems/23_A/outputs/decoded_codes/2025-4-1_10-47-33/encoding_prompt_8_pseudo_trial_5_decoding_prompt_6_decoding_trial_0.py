# Start of the program

# Read the input line from the user and remove the last character (newline).
input_line = input().rstrip()  # rstrip() removes any trailing newline characters

# Calculate the length of the input line.
length_of_input = len(input_line)

# Initialize a variable to keep track of the maximum length of substrings found.
longest_repeated_substring_length = 0

# Loop through all possible lengths of substrings, starting from 0 to length of input line - 1.
for substring_length in range(length_of_input):  # from 0 to length_of_input - 1

    # Loop through each starting position in the string for a substring of the current length.
    for start_index in range(length_of_input - substring_length):  # Valid starting indices
        
        # Extract the substring from the input string starting at start_index with the current length.
        current_substring = input_line[start_index:start_index + substring_length + 1]

        # Check if this substring appears again in the input string,
        # starting from the position after start_index.
        if input_line.find(current_substring, start_index + 1) != -1:  # If found
            # If found, update the longest substring length variable.
            longest_repeated_substring_length = substring_length + 1  # +1 because we want length not index
            # Break out of the loop as we only need the longest length for this size.
            break

# Output the maximum length of the repeated substring found.
print(longest_repeated_substring_length)

# End of the program
