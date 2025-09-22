# Start Program

# Define Input
line = input()[:-1]  # Read line of text and exclude the last character

# Initialize Variables
length_of_line = len(line)
longest_repeated_length = 0

# Outer Loop (for each potential substring length from 0 to n-1)
for current_length in range(length_of_line):
    found_repetition = False  # Flag to check if repetition is found in this length
    # Inner Loop (for each possible starting position in the string)
    for start_index in range(length_of_line - current_length):
        # Extract Substring
        substring = line[start_index:start_index + current_length + 1]  # current_length + 1 gives the correct substring length

        # Check for Repetition
        if substring in line[start_index + 1:]:  # Check in the remaining part of the string
            longest_repeated_length = current_length + 1  # Update the longest repeated length
            found_repetition = True  # Set flag to true indicating repetition found
            break  # Exit inner loop since we found a repetition for the current length
    if found_repetition:
        continue  # If found, continue to the next length

# Output Result
print(longest_repeated_length)
