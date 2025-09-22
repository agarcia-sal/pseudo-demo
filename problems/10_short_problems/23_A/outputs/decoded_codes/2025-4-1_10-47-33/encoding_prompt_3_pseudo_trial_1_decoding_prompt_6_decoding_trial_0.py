# Read a line of input from standard input
string_line = input()

# Remove the last character from the string
string_line = string_line[:-1]

# Get the length of the modified string
length_of_string = len(string_line)

# Initialize the variable to store the longest repeated substring length
longest_repeated_substring_length = 0

# Iterate over possible lengths of substrings
for substring_length in range(1, length_of_string):  # Start from 1 to avoid empty substring
    # Check for each starting position of the string
    for starting_index in range(length_of_string):
        # Create a substring of the current length starting from starting_index
        current_substring = string_line[starting_index:starting_index + substring_length]

        # Check if the current substring appears again in the string
        if current_substring in string_line[starting_index + 1:]:
            # Update the longest repeated substring length
            longest_repeated_substring_length = substring_length
            break  # Exit the inner loop when a match is found

# Output the longest length of the repeated substring found
print(longest_repeated_substring_length)
