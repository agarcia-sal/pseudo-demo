# Read a line of input and store it in a variable
input_line = input().rstrip()  # Removing the newline character
string_length = len(input_line)
longest_repeated_substring_length = 0

# Loop through all possible substring lengths
for length in range(1, string_length):  # Start from 1 to avoid empty substrings
    # Loop through each starting position for the substring
    for start_position in range(string_length - length + 1):
        # Check if the substring from start_position of the current length exists later in the string
        current_substring = input_line[start_position:start_position + length]
        
        # If the substring is found again in the string after the starting position
        if current_substring in input_line[start_position + length:]:
            # Update the length of the longest repeated substring found
            longest_repeated_substring_length = length
            break  # No need to continue checking for this length

# Output the length of the longest repeated substring found
print(longest_repeated_substring_length)


def find_longest_repeated_substring(input_string):
    if not isinstance(input_string, str):
        raise ValueError("Input must be a string")
    
    input_string = input_string.rstrip()  # Removing potential newline
    string_length = len(input_string)
    longest_repeated_substring_length = 0

    for length in range(1, string_length):
        for start_position in range(string_length - length + 1):
            current_substring = input_string[start_position:start_position + length]
            if current_substring in input_string[start_position + length:]:
                longest_repeated_substring_length = length
                break

    return longest_repeated_substring_length
