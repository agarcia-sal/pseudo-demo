# Start Program

# Define Input
input_line = input().strip()  # Read a line of text and remove the last character

# Initialize Variables
length_of_line = len(input_line)
longest_repeated_length = 0

# Outer Loop: Iterate over possible substring lengths
for current_length in range(1, length_of_line):  # start from 1 to avoid empty substrings
    # Inner Loop: Iterate over possible starting positions
    for start_index in range(length_of_line - current_length + 1):
        # Extract Substring
        substring = input_line[start_index:start_index + current_length]

        # Check for Repetition
        if substring in input_line[start_index + 1:]:
            longest_repeated_length = current_length
            break  # Exit inner loop, as we found a repeating substring

# Output Result
print(longest_repeated_length)
