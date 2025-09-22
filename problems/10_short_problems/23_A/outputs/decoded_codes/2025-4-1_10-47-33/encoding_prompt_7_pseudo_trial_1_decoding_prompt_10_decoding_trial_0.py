def find_longest_repeated_substring(input_string):
    # Initialize the length of the input string
    string_length = len(input_string)
    
    # Variable to store the length of the longest repeated substring found
    longest_repeated_length = 0
    
    # Loop over each possible length of substring
    for current_length in range(1, string_length):  # starting with length 1
        # Loop over each starting position of the substring
        for starting_index in range(string_length - current_length):
            # Extract the current substring
            substring = input_string[starting_index:starting_index + current_length]
            
            # Check if the substring exists again in the string after the current starting index
            if substring in input_string[starting_index + 1:]:
                # Update longest_repeated_length if a repeated substring is found
                longest_repeated_length = current_length
        
        # Optimization: if a substring of length `current_length` was found,
        # we can avoid further checking longer substrings as we want the longest one
        if longest_repeated_length == current_length:
            break  # break if we've found a repeated substring of this length
    
    return longest_repeated_length

# Read input string
input_string = input()

# Calculate and print the length of the longest repeated substring
result = find_longest_repeated_substring(input_string)
print(result)
