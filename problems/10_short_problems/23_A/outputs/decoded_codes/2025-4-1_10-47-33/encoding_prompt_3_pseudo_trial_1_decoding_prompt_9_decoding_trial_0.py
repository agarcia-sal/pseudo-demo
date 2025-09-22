# Read a line of input from standard input and remove the last character
string_line = input()[:-1]  # Read input and remove the last character
length_of_string = len(string_line)
longest_repeated_substring_length = 0  # Initialize the length of the longest repeated substring

# Iterate over possible lengths of substrings
for substring_length in range(1, length_of_string):  # Start at 1 to avoid empty substring
    # Check for each starting position of the string
    for starting_index in range(length_of_string - substring_length + 1):
        # Create a substring of the current length starting from starting_index
        current_substring = string_line[starting_index:starting_index + substring_length]
        
        # Check if the current substring appears again in the string
        if current_substring in string_line[starting_index + 1:]:
            # Update the longest repeated substring length
            longest_repeated_substring_length = substring_length
            break  # Exit the inner loop as we found a repeated substring
            
# Output the longest length of the repeated substring found
print(longest_repeated_substring_length)
