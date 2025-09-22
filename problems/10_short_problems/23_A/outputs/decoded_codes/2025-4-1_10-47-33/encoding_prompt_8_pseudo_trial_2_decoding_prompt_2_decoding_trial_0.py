# Start Program

# Define Input
line = input()[:-1]  # Read a line of text and exclude the last character

# Initialize Variables
length_of_line = len(line)
longest_repeated_length = 0  # Keep track of the longest repeating substring length

# Outer Loop: for each potential substring length from 0 to n-1
for current_length in range(length_of_line):
    # Inner Loop: for each possible starting position in the string
    for start_index in range(length_of_line):
        # Extract Substring
        substring = line[start_index:start_index + current_length]

        # Check for Repetition
        if substring and substring in line[start_index + 1:]:  # Check in the remaining part of the string
            longest_repeated_length = current_length  # Update longest repeated length
            break  # Exit the inner loop since we found repetition for the current length

# Output Result
print(longest_repeated_length)
