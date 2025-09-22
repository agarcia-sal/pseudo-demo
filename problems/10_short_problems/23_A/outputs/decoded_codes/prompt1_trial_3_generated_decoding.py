# BEGIN

# Read a line of input and remove the trailing newline character
line = input()
length_of_line = len(line)
repeat_value = 0

# Loop through all possible substring lengths
for l in range(length_of_line):  # Outer loop from 0 to length_of_line - 1

    # Loop through each starting index of the line
    for i in range(length_of_line):  # Inner loop from 0 to length_of_line - 1
        
        # Extract the substring from index i of length l
        substring = line[i:i + l]  # The substring of line starting at index i with length l
        
        # Check if this substring appears again later in the line
        if substring in line[i + 1:]:  # Check in the remainder of the line
            # Update repeat_value if we find a repeating substring
            repeat_value = l
            break  # Exit the inner loop if a repeating substring is found

# END FOR inner loop

# END FOR outer loop

# Output the length of the longest repeating substring found
print(repeat_value)

# END
