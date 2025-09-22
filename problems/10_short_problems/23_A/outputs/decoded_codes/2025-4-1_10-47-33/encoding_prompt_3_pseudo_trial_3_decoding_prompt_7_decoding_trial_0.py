# This function finds the length of the longest repeated substring in the given string
def longest_repeated_substring_length():
    # Read a line of input from standard input and remove the last character (newline)
    string_input = input().strip()
    
    # Determine the length of the input string
    string_length = len(string_input)
    
    # Initialize variable to hold the result
    longest_repeated_substring_length = 0
    
    # Loop through lengths of potential substrings from 0 to stringLength - 1
    for length_from_zero in range(string_length):
        # Loop through each starting index for the substrings
        for start_index in range(string_length):
            # Extract the substring from startIndex of the current length
            current_substring = string_input[start_index:start_index + length_from_zero + 1]
            
            # Check if the current substring can be found in the remainder of the string
            if string_input.find(current_substring, start_index + 1) != -1:
                # If found, update the result to the current length
                longest_repeated_substring_length = length_from_zero + 1
                
                # Exit the inner loop since we found a repeated substring of this length
                break
                
        # If a repeated substring of this length has been found, continue to next length
        if longest_repeated_substring_length == length_from_zero + 1:
            continue
            
    # Output the length of the longest repeated substring found
    print(longest_repeated_substring_length)

# Call the function to execute
longest_repeated_substring_length()
