# Start Program

# Read a line of text from the standard input excluding the last character.
input_line = input()[:-1]

# Initialize Variables
length_of_line = len(input_line)  # Getting the length of the input line
longest_repeated_length = 0  # To keep track of the longest repeating substring length

# Outer Loop: Checking each potential substring length from 0 to length_of_line - 1
for current_length in range(length_of_line):  # current_length goes from 0 to length_of_line - 1

    # Inner Loop: Checking each possible starting position in the string
    for start_index in range(length_of_line):  # start_index goes from 0 to length_of_line - 1
        
        # Extract Substring
        substring = input_line[start_index:start_index + current_length]  # Extracting the substring

        # Check for Repetition
        if substring in input_line[start_index + 1:]:  # Checking if substring is found after start_index
            longest_repeated_length = current_length  # Update longest repeated length
            break  # Exit the inner loop since we found a repetition

# Output Result
print(longest_repeated_length)  # Printing the value of longest_repeated_length
