# Begin by reading a line of input from the user
input_line = input().strip()  # Remove any surrounding whitespace
input_length = len(input_line)  # Get the length of the input string
result_value = 0  # Initialize the variable to store the maximum length of a repeated substring

# Iterate through each possible length of substrings
for substring_length in range(1, input_length):  # Start from 1 since substring length of 0 doesn't make sense
    # Check each starting position for the substring of given length
    for start_index in range(input_length):
        # Ensure we do not exceed the string length when extracting the substring
        if start_index + substring_length <= input_length:
            substring = input_line[start_index:start_index + substring_length]  # Extract the substring
            
            # Check if the substring can be found later in the string
            if input_line.find(substring, start_index + 1) != -1:  # Search for the substring from the next position
                result_value = substring_length  # Update the result_value to the current substring length
                break  # Exit the inner loop once a match is found

# Output the maximum length of the found substring
print(result_value)
