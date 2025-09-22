def findLongestRepeatedSubstring(inputString):
    # Initialize the length of the input string
    string_length = len(inputString)
    # Initialize the variable to store the length of the longest repeated substring
    longest_repeated_length = 0
    
    # Loop over each possible length of substring, starting from 1 to string_length
    for current_length in range(1, string_length):
        # Loop over each starting position of the substring
        for starting_index in range(string_length - current_length):
            # Extract the substring
            substring = inputString[starting_index:starting_index + current_length]
            # Check if the substring exists again in the string after the current starting index
            if substring in inputString[starting_index + 1:]:
                # Update longest_repeated_length to current_length, indicating a repeated substring was found
                longest_repeated_length = current_length
                # Exit the inner loop once a repeated substring is found at this length
                break  # Found a repeat, break out of the inner loop
    
    # Return the length of the longest repeated substring found
    return longest_repeated_length

# To test the function, receive input from the user
input_string = input()
result = findLongestRepeatedSubstring(input_string)
print(result)
