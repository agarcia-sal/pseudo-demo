def find_longest_repeated_substring():
    # Read a line of input from the user and remove the last character
    input_string = input().strip()  # Assuming we want to read an entire line from the user
    input_length = len(input_string)
    result_value = 0
    
    # Iterate through each possible length of substrings
    for substring_length in range(1, input_length):  # Start from 1 to avoid the empty substring case
        # Check each starting position for the substring of the given length
        for start_index in range(input_length - substring_length + 1):
            # Extract the substring from the current starting position
            substring = input_string[start_index:start_index + substring_length]
            
            # Check if the substring can be found later in the string
            if input_string.find(substring, start_index + 1) != -1:
                # Update the result_value to the current substring length
                result_value = substring_length
                break  # Exit the inner loop once a match is found
        
    # Output the maximum length of the found substring
    print(result_value)

# Call the function to execute
find_longest_repeated_substring()
