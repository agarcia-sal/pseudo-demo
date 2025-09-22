def find_longest_repeated_substring(input_string):
    # Get the length of the input string
    length_of_string = len(input_string)
    
    # Initialize the length of the longest repeated substring
    longest_repeated_substring_length = 0
    
    # Loop over possible substring lengths
    for substring_length in range(1, length_of_string):
        # Loop over the start index for the substring
        for start_index in range(length_of_string):
            # Get the current substring
            current_substring = input_string[start_index:start_index + substring_length]
            
            # Check if the current substring appears again after the start index
            if input_string.find(current_substring, start_index + 1) != -1:
                # Update longest repeated substring length
                longest_repeated_substring_length = substring_length
                break  # No need to check further for this length
            
    return longest_repeated_substring_length

# Driver code to read input and output the result
input_string = input()
print(find_longest_repeated_substring(input_string))
