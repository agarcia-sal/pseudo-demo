# Start Program

# Define Input
line = input()[:-1]  # Read a line of text and exclude the last character

# Initialize Variables
length_of_line = len(line)
longest_repeated_length = 0

# Outer Loop
for current_length in range(length_of_line):  # current_length from 0 to length_of_line - 1
    # Inner Loop
    for start_index in range(length_of_line):  # start_index from 0 to length_of_line - 1
        # Extract Substring
        substring = line[start_index:start_index + current_length]
        
        # Check for Repetition
        if substring in line[start_index + current_length:]:  # Check for the substring in the remaining part of the string
            longest_repeated_length = current_length
            break  # Exit the inner loop as we've found a repetition

# Output Result
print(longest_repeated_length)
