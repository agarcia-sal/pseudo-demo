# Begin the program

# Read a line of input from the user and strip the newline character
input_line = input().strip()

# Determine the length of the input line
length_of_line = len(input_line)
result_variable = 0  # Initialize the result variable

# Loop through all possible lengths of substrings from 0 to length_of_line - 1
for substring_length in range(length_of_line):
    # Loop through the starting index of the substring
    for start_index in range(length_of_line):
        # Create a substring from start_index of length substring_length
        substring = input_line[start_index:start_index + substring_length + 1]
        
        # Check if the substring exists later in the string
        if input_line.find(substring, start_index + 1) != -1:
            result_variable = substring_length  # Update result variable with the current length
            break  # Exit the inner loop
    else:
        continue  # Go to the next substring length if not found
    break  # Exit the outer loop if a match was found

# Print the result variable indicating the length of the substring found
print(result_variable)

# End the program
