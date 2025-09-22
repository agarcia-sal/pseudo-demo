# Function to find the length of the longest repeated substring in a given text line
def longest_repeated_substring():
    # Receive input from the user
    line = input().rstrip()  # Remove trailing newline character
    line_length = len(line)  # Determine the length of the line

    # Initialize the variable to track the longest repeated substring length
    longest_repeated_substring_length = 0

    # Iterate over possible substring lengths
    for current_length in range(1, line_length):  # Start from length 1 to line_length - 1
        # Check all starting positions for the substring of the current length
        for start_index in range(line_length - current_length):
            # Extract the substring from the line
            substring = line[start_index:start_index + current_length]

            # Check if this substring appears later in the line
            if substring in line[start_index + current_length:]:
                longest_repeated_substring_length = current_length
                break  # Break out of the inner loop if a repeated substring is found

    # Output the result
    print(longest_repeated_substring_length)

# Test the function with different inputs (these lines won't be executed, just for reference)
# Example test cases:
# Input: "banana" -> Output: 3 (substring "ana" appears twice)
# Input: "abcd" -> Output: 0 (no repeated substrings)
# Input: "ababcab" -> Output: 2 (substring "ab" appears twice)
