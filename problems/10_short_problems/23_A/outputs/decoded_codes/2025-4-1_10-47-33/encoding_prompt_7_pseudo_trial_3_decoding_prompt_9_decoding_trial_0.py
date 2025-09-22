def remove_trailing_newline(string):
    return string.rstrip('\n')  # Removes trailing newline character

def length(string):
    return len(string)  # Returns the number of characters in the string

def substring(string, start_index, length):
    return string[start_index:start_index + length]  # Extracts the substring

def find(source_string, sub_string):
    return source_string.find(sub_string)  # Returns the index of substring, or -1 if not found

def find_longest_repeated_substring(input_string):
    # Remove the trailing newline character from the input string
    trimmed_string = remove_trailing_newline(input_string)

    # Get the length of the trimmed string
    string_length = length(trimmed_string)

    # Initialize the result variable for longest repeated substring length
    longest_repeated_length = 0

    # Loop through possible substring lengths starting from 1 to string_length
    for length_index in range(1, string_length):  # Length of substring must be at least 1
        # Loop over each starting index for the substring
        for start_index in range(0, string_length - length_index + 1):
            # Extract the current substring based on length_index and start_index
            current_substring = substring(trimmed_string, start_index, length_index)

            # Check if the current substring exists later in the string
            if find(trimmed_string, current_substring) != -1:
                # If found, update longest_repeated_length with the current length
                longest_repeated_length = length_index
                # Exit the inner loop as we found a repeated substring
                break

    # Return the length of the longest repeated substring found
    return longest_repeated_length

# Example usage
input_string = input()  # Take input from the user
result = find_longest_repeated_substring(input_string)
print(result)  # Output the length of the longest repeated substring
