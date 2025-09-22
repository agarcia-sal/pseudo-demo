# Begin the program

# Read a line of input, removing the last character (newline)
line = input().rstrip()  # Use rstrip to remove any trailing newline
line_length = len(line)  # Get the length of the input line
result_value = 0  # Initialize the resultValue to hold the maximum length of repeated substring

# Loop through all possible substring lengths from 0 to line_length - 1
for l in range(line_length):  # l represents the current substring length
    # Loop through each index in the line to check for repeated substrings
    for i in range(line_length):  # i represents the starting index of the substring
        # Extract a substring of length l starting from current index i
        substring = line[i:i + l]  # Get the substring from the line
        
        # Check if this substring occurs again later in the line
        if substring and substring in line[i + 1:]:  # Ensure substring is not empty and check if exists later
            result_value = l  # Update the resultValue to the current length l
            break  # Break out of the inner loop if a repeated substring is found

# Output the maximum length of the found repeated substring
print(result_value)  # Output the result

# End of the program
