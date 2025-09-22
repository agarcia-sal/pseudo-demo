# Read a line of input and remove the trailing newline character
input_line = input()

# Determine the length of the input line
length_of_input = len(input_line)

# Initialize a variable to hold the result
repeated_length = 0

# Loop through lengths of substrings from 0 to length_of_input - 1
for current_length in range(length_of_input):
    # Check for substrings of the current length
    for start_index in range(length_of_input):
        # Extract a substring from the current start index
        substring = input_line[start_index:start_index + current_length]
        
        # Check if the substring occurs again later in the string
        if substring in input_line[start_index + 1:]:
            # Update the result with the current length
            repeated_length = current_length
            break  # Exit inner loop if a repeat is found

# Output the length of the longest repeated substring
print(repeated_length)
