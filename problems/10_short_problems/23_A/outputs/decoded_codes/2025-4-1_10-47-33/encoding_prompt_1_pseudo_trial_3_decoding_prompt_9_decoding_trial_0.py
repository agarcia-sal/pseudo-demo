# Function to extract a substring from the input string
def extract_substring(input_line, start_index, substring_length):
    return input_line[start_index:start_index + substring_length]

# Main logic to find the maximum length of repeated substrings
input_line = input()  # Read a line of input from the user
input_length = len(input_line)  # Get the length of the input line
result_value = 0  # Initialize the result value for the maximum substring length

# Iterate through each possible length of substrings
for substring_length in range(1, input_length):  # Start from 1 to avoid empty substring
    # Check each starting position for the substring of given length
    for start_index in range(input_length - substring_length):  # Ensure no overflow
        # Extract the substring from the current starting position
        substring = extract_substring(input_line, start_index, substring_length)

        # Check if the substring can be found later in the string
        if substring in input_line[start_index + substring_length:]:
            # Update the result_value to the current substring length
            result_value = substring_length

# Output the maximum length of the found substring
print(result_value)
