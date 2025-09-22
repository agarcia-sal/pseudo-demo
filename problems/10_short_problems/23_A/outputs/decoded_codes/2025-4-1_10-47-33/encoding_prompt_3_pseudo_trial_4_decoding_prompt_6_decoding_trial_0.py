# Begin program

# Read a line of input from standard input
line = input()

# Calculate the length of the line
line_length = len(line)

# Initialize result value to 0
result_value = 0

# Loop through all possible substring lengths from 0 to line_length - 1
for substring_length in range(line_length):
    
    # Loop through each index in the line to check for repeated substrings
    for index in range(line_length):
        
        # Extract a substring of the current length starting from the current index
        substring = line[index:index + substring_length]
        
        # Check if this substring exists again later in the line
        if substring in line[index + 1:]:
            # Update the result_value to the current length if a repeat is found
            result_value = substring_length
            break  # Exit the inner loop if a repeat is found
    
# Output the maximum length of the found repeated substring
print(result_value)

# End program
