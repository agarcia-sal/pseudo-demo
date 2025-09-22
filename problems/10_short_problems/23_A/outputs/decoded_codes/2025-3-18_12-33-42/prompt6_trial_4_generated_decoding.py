# Read a line of input and remove the last character (typically new line)
input_line = input().strip()  # Stripping removes any trailing newline characters

# Set length_of_line to the length of the input line
length_of_line = len(input_line)

# Initialize longest_repeated_length to 0
longest_repeated_length = 0

# Loop through different lengths of substrings
for length_from_zero in range(length_of_line):
    # Check for all starting positions of substrings of the current length
    for start_position in range(length_of_line):
        # Create a substring from the current start position with the current length
        substring = input_line[start_position:start_position + length_from_zero]

        # Check if the substring appears again later in the input line
        if substring in input_line[start_position + 1:]:
            # Update the longest repeated length found
            longest_repeated_length = length_from_zero
            break  # Exit inner loop since a repetition is found

# Output the longest length of repeated substring found
print(longest_repeated_length)
