def find_longest_repeated_substring(input_string):
    # Remove the trailing newline character from the input string
    trimmed_string = remove_trailing_newline(input_string)
    
    # Get the length of the trimmed string
    string_length = length(trimmed_string)
    
    # Initialize the result variable for longest repeated substring length
    longest_repeated_length = 0

    # Loop through possible substring lengths starting from 0 to string_length - 1
    for length_index in range(string_length):
        # Loop over each starting index for the substring
        for start_index in range(string_length):
            # Extract the current substring based on length_index and start_index
            current_substring = substring(trimmed_string, start_index, length_index)

            # Check if the current substring exists later in the string
            if find(trimmed_string, current_substring) != -1:
                # If found, update longest_repeated_length with the current length
                longest_repeated_length = length_index
                # Exit the inner loop as we found a repeated substring
                break
        # Note: The inner loop will be exited if a match is found

    # Return the length of the longest repeated substring found
    return longest_repeated_length

def remove_trailing_newline(string):
    return string.rstrip('\n')

def length(string):
    return len(string)

def substring(string, start_index, length):
    return string[start_index:start_index + length]

def find(source_string, sub_string):
    # Return the index of sub_string in source_string, or -1 if not found
    return source_string.find(sub_string)

# Usage example - input handling can be outside this function
input_string = input()
result = find_longest_repeated_substring(input_string)
print(result)
