# Start Program

# Define Input
input_line = input()[:-1]  # Read a line of text and exclude the last character

# Initialize Variables
length_of_line = len(input_line)  # Get the length of the input line
longest_repeated_length = 0  # To track the longest repeating substring length

# Outer Loop (for each potential substring length)
for current_length in range(1, length_of_line):  # Start from 1 to consider non-zero length substrings

    # Inner Loop (for each possible starting position in the string)
    for start_index in range(length_of_line - current_length + 1):  # Ensure the substring fits
        # Extract Substring
        substring = input_line[start_index:start_index + current_length]

        # Check for Repetition
        if substring in input_line[start_index + 1:]:  # Check for repetition after the current start index
            longest_repeated_length = current_length  # Update the longest repeating length
            break  # Exit the inner loop since we found a repeat

# Output Result
print(longest_repeated_length)
