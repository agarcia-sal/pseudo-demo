# Read a line of input from standard input
input_line = input().strip()  # Remove any trailing newline characters
length_of_input = len(input_line)  # Get the length of the input line
longest_repeated_length = 0  # Initialize the variable to store the longest repeated substring length

# Iterate through possible lengths of substrings
for current_length in range(length_of_input):  # From 0 to n-1
    # Check for repeated substrings of the current length
    for start_index in range(length_of_input):  # From 0 to n-1
        # Extract the substring of the current length
        substring = input_line[start_index:start_index + current_length]

        # Check if the substring occurs again after the current index
        if substring in input_line[start_index + 1:]:
            longest_repeated_length = current_length  # Update the longest repeated length
            break  # Exit inner loop as we found a repeated substring

# Output the length of the longest repeated substring
print(longest_repeated_length)
