# Function to find the length of the longest repeated substring
def longest_repeated_substring_length():
    # Read a line of input and remove any trailing newline character
    input_line = input().strip()
    # Determine the length of the input line
    length_of_input = len(input_line)
    # Initialize variable to track the longest repeated substring length
    longest_repeated_substring_length = 0

    # Loop through each possible substring length
    for current_length in range(length_of_input):
        # Loop through each possible starting index for the substring
        for start_index in range(length_of_input):
            # Extract the current substring
            current_substring = input_line[start_index:start_index + current_length]
            # Check if this substring appears again in the input
            if current_substring in input_line[start_index + 1:]:
                # Update longest repeated substring length found
                longest_repeated_substring_length = current_length
                # Exit inner loop to check the next current length
                break

    # Print the length of the longest repeated substring found
    print(longest_repeated_substring_length)

# Example test case
# To run this function, just call longest_repeated_substring_length() in your environment.
