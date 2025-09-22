# BEGIN

# Read a line of input from the user and remove any trailing newline character
line = input().rstrip('\n')
length_of_line = len(line)
longest_repeating_length = 0

# Loop through all possible lengths of substrings
for substring_length in range(length_of_line):
    # Check for each starting position in the string
    for starting_position in range(length_of_line):
        # Extract the substring from the current starting_position of length substring_length
        current_substring = line[starting_position:starting_position + substring_length]

        # Check if the current substring exists anywhere after the current starting position
        if line.find(current_substring, starting_position + 1) != -1:
            longest_repeating_length = substring_length
            break  # Exit the inner loop since we found a repeating substring of this length

# Output the length of the longest repeating substring found
print(longest_repeating_length)

# END
