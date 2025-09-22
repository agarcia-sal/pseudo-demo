def read_input():
    """Read input from standard input and return it as a string."""
    return input().strip()  # Remove any trailing newline characters

def find_max_repeating_substring_length(input_line):
    """Find the maximum length of a repeating substring in the input line."""
    length_of_input = len(input_line)
    result_value = 0

    # Loop through possible lengths of substrings
    for substring_length in range(length_of_input):
        # Loop through each starting index of the input string
        for start_index in range(length_of_input):
            # Extract the substring from the input line
            current_substring = input_line[start_index:start_index + substring_length + 1]

            # Check if the substring appears again in the input string after the current starting index
            if input_line.find(current_substring, start_index + 1) != -1:
                result_value = substring_length + 1  # Update with current substring length
                break  # Exit the inner loop as we found a match

    return result_value

# Read the input from user
input_line = read_input()

# Calculate the max length of the repeating substring
result = find_max_repeating_substring_length(input_line)

# Output the result value
print(result)
