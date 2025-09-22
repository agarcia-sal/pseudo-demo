# Begin by reading input from the user
input_line = input()  # Read input from user
length_of_line = len(input_line)  # Get the length of the input line
result_value = 0  # Initialize the result value to 0

# Iterate over possible substring lengths starting from 0 up to the length of the input line - 1
for length in range(length_of_line):  # `length` will vary from 0 to length_of_line - 1
    # Iterate through each starting index in the input line
    for index in range(length_of_line):  # `index` will vary from 0 to length_of_line - 1
        # Check if the substring from index `index` of length `length` occurs again after `index`
        substring = input_line[index:index + length]  # Extract the substring
        
        # Check if the substring appears later in the string
        if input_line.find(substring, index + 1) != -1:
            # If it exists, update the result_value to the current length
            result_value = length  # Update the result value to the current length
            break  # Break the inner loop since we found a repetition
    
# Output the result value
print(result_value)  # Print the length of the longest repeating substring
