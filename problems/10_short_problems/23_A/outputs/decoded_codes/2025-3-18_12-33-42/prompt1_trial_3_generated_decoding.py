# BEGIN

# Read a line of input and remove the last character
line = input()
line = line[:-1]  # Remove last character
length_of_line = len(line)
return_value = 0  # Initialize return value to 0

# Iterate over all possible lengths of substrings
for length in range(length_of_line):  # length from 0 to length_of_line EXCLUSIVE
    # Check each starting position in the line
    for starting_position in range(length_of_line):  # starting_position from 0 to length_of_line EXCLUSIVE
        # Extract the current substring
        current_substring = line[starting_position:starting_position + length]
        
        # Check if the substring appears again in the line after the starting position
        if current_substring in line[starting_position + 1:]:  # Check from starting_position + 1
            # Update the return value with the current length
            return_value = length
            break  # BREAK OUT OF inner loop

# Output the longest length of found repeating substring
print(return_value)

# END
