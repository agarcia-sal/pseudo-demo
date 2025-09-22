# BEGIN

# Read a line of input from the user and remove the newline character
line = input().strip()
length_of_line = len(line)
result_variable = 0

# Iterate over possible substring lengths from 0 to the length of the line
for substring_length in range(length_of_line):  # from 0 to length_of_line - 1

    # Iterate through each character in the line
    for index in range(length_of_line):  # from 0 to length_of_line - 1
        
        # Extract the substring starting at the current index with the current length
        current_substring = line[index:index + substring_length]

        # Check if the current substring appears again in the line after the current index
        if current_substring in line[index + 1:]:
            
            # Update the result variable with the current length
            result_variable = substring_length
            
            # Exit the inner loop since we found a repeating substring
            break

    # Check if a repeating substring was found and break the outer loop if so
    if result_variable != 0:
        break

# Output the length of the longest repeating substring found
print(result_variable)

# END
