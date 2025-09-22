def read_input_line():
    # Simulates reading a line of input
    return input().strip()

def extract_substring(line, start_index, length):
    # Returns a substring from the input line
    return line[start_index:start_index + length]

def find_substring_in_line(line, substring, start_after_index):
    # Checks if substring is found in the line starting after the given index
    return substring in line[start_after_index:]

# Main function to find the length of the longest repeated substring
def longest_repeated_substring_length():
    # Read input line and determine its length
    input_line = read_input_line()
    string_length = len(input_line)

    # Variable to hold the length of the longest repeated substring
    longest_repeated_length = 0

    # Loop through each possible substring length from 1 to string_length
    for substring_length in range(1, string_length):

        # For each starting position in the string
        for position in range(string_length - substring_length + 1):

            # Extract the current substring
            current_substring = extract_substring(input_line, position, substring_length)

            # Check if the current substring appears again in the input line after the current position
            if find_substring_in_line(input_line, current_substring, position + substring_length):
                # Update the longest repeated substring length
                longest_repeated_length = substring_length
                break  # No need to check further positions for this length

    # Output the length of the longest repeated substring
    print(longest_repeated_length)

# Uncomment the following line to test the function:
# longest_repeated_substring_length()
