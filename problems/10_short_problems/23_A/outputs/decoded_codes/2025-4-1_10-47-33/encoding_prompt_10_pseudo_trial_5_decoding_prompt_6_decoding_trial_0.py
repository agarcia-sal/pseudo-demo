# Import functionality to read standard input
input_line = input().strip()  # Read input and remove any trailing newline characters

# Set variable 'n' to the length of the input line
length_of_input = len(input_line)

# Initialize variable 'result_value' to 0. This will hold the result.
result_value = 0

# Loop through each length 'l' from 0 to length_of_input - 1
for substring_length in range(length_of_input):
    # Loop through each index 'i' from 0 to length_of_input - 1
    for index in range(length_of_input):
        # Extract the substring from input_line starting at index 'i' with length 'l'
        substring = input_line[index:index + substring_length]

        # Check if this substring appears again in input_line starting from index 'i + 1'
        if substring in input_line[index + 1:]:
            # If the substring is found, set 'result_value' to the value of 'l'
            result_value = substring_length
            
            # Break out of the inner loop as we found a match
            break

# Print the value of 'result_value', which is the final result
print(result_value)
