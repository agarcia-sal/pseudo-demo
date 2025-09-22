# Function to find the length of the longest substring that appears at least twice
def longest_repeated_substring():
    # Read input string from the user
    input_string = input().strip()
    # Store the length of the input string
    string_length = len(input_string)
    # Variable to keep track of the maximum length of repeated substring found
    longest_repeated_substring_length = 0

    # Iterate over possible substring lengths
    for current_length in range(1, string_length):  # start from 1 to avoid empty substring
        # Iterate over starting positions for substrings
        for start_position in range(string_length - current_length):
            # Extract the substring from the current start position with specified length
            substring = input_string[start_position:start_position + current_length]
            # Check if this substring appears again in the remainder of the string
            if substring in input_string[start_position + current_length:]:
                # Update longest repeated substring length if a repeat is found
                longest_repeated_substring_length = current_length
                break  # Exit the inner loop since we found a repeated substring

    # Output the length of the longest repeated substring
    print(longest_repeated_substring_length)

# Call the function to execute
longest_repeated_substring()
