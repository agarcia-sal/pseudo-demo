# Step 1: Read a line of input from the standard input
input_line = input()

# Step 2: Remove the last character from the input line
input_line = input_line[:-1]  # Remove the last character

# Step 3: Determine the length of the line
line_length = len(input_line)

# Step 4: Initialize a variable to store the result
result_value = 0

# Step 5: Iterate through possible substring lengths from 0 to line_length-1
for length in range(line_length):  # length varies from 0 to n-1
    # Step 6: Iterate through each character in the line
    for index in range(line_length):  # index varies from 0 to n-1
        # Step 7: Check if a substring of length 'length' starting at index 'index' can be found elsewhere in the line after index 'index'
        substring = input_line[index:index + length]  # Get the substring
        if input_line.find(substring, index + 1) != -1:  # Find it in the rest of the line
            # Step 8: Update result_value to the current length
            result_value = length
            # Step 9: Exit the inner loop since a match is found
            break

# Step 10: Output the result
print(result_value)
