def find_longest_repeated_substring(input_string):
    # Helper function to remove trailing newline character from the input string
    def remove_trailing_newline(string):
        return string.rstrip('\n')

    # Helper function to extract a substring
    def substring(string, start_index, length):
        return string[start_index:start_index + length]

    # Helper function to find the index of a substring in a string
    def find(source_string, sub_string):
        return source_string.find(sub_string)

    # Remove the trailing newline character from the input string
    trimmed_string = remove_trailing_newline(input_string)
    
    # Get the length of the trimmed string
    string_length = len(trimmed_string)

    # Initialize the result variable for longest repeated substring length
    longest_repeated_length = 0

    # Loop through possible substring lengths starting from 1 to string_length
    for length_index in range(1, string_length):
        # Loop over each starting index for the substring
        for start_index in range(string_length - length_index):
            # Extract the current substring based on length_index and start_index
            current_substring = substring(trimmed_string, start_index, length_index)

            # Check if the current substring exists later in the string
            if find(trimmed_string[start_index + 1:], current_substring) != -1:
                # If found, update longest_repeated_length with the current length
                longest_repeated_length = length_index
                # Exit the inner loop as we found a repeated substring
                break

    # Return the length of the longest repeated substring found
    return longest_repeated_length

# Example usage (input handling as per instructions)
if __name__ == "__main__":
    input_string = input()
    result = find_longest_repeated_substring(input_string)
    print(result)
