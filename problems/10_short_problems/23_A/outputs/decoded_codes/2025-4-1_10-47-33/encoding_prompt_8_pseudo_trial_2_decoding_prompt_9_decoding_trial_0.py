# Start the program
# Define Input
input_line = input()[:-1]  # Read a line of text and exclude the last character

# Initialize Variables
length_of_line = len(input_line)
longest_repeated_length = 0  # Keep track of the longest repeating substring length

# Outer Loop for each potential substring length
for current_length in range(length_of_line):
    # Inner Loop for each possible starting position in the string
    for start_index in range(length_of_line):
        # Extract Substring
        substring = input_line[start_index:start_index + current_length]
        
        # Check for Repetition
        if substring in input_line[start_index + 1:]:
            longest_repeated_length = current_length
            break  # Exit the inner loop as we found repetition for the current length

# Output Result
print(longest_repeated_length)
