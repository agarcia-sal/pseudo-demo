# Read a line of input from the user
input_line = input()

# Remove the newline character from the end of the input (in Python, input() doesn't include it)
# Calculate the length of the input string
length_of_input = len(input_line)

# Initialize a variable to hold the length of the longest repeated substring
longest_repeated_length = 0

# Loop through substrings of increasing lengths
for length in range(1, length_of_input):  # Starting from 1 to avoid empty substring

    # Check all starting positions for the substring of the current length
    for start_position in range(length_of_input - length + 1):

        # Extract the substring from 'start_position' of 'length'
        current_substring = input_line[start_position:start_position + length]

        # Check if this substring appears again in the string after its starting position
        if input_line.find(current_substring, start_position + 1) != -1:
            # If the substring is found again, update the longest repeated length
            longest_repeated_length = length
            break  # Exit this inner loop as we found a repeat

# Print the length of the longest repeated substring found
print(longest_repeated_length)
