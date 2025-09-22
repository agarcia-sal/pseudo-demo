# BEGIN

# Read a line of input and remove the last character
line = input()
line = line[:-1]  # Remove the last character (could be a newline)
length_of_line = len(line)
result_value = 0

# Iterate over lengths from 0 to the length_of_line - 1
for length in range(length_of_line):
    # Check each starting position in the line
    for index in range(length_of_line):
        # Check if the substring starting at index of the current length is found later in the line
        if line[index:index + length + 1] in line[index + 1:]:
            result_value = length
            break  # Exit the inner loop

# Output the highest length found that meets the criteria
print(result_value)

# END
