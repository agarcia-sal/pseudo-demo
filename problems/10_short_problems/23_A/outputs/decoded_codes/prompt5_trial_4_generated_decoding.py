def findLongestRepeatedSubstringLength():
    # Read the input string from the user
    input_string = input()
    
    # Get the length of the input string
    string_length = len(input_string)
    
    # Variable to keep track of the longest repeated substring length
    max_length = 0

    # Loop through all possible lengths of substrings
    for current_length in range(1, string_length):
        # Loop through all possible starting positions for the substring
        for start_index in range(string_length - current_length):
            # Extract the substring to check
            substring_to_check = input_string[start_index:start_index + current_length]
            
            # Check if the substring appears again in the input string
            if substring_to_check in input_string[start_index + 1:]:
                # Update max_length if a longer repeated substring is found
                max_length = current_length
                break  # Exit the inner loop as we found a valid substring

    # Return the length of the longest repeated substring
    return max_length
