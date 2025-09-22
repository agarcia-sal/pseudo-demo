def find_max_repeated_substring_length():
    # Read a line of input from the user
    input_line = input()
    input_length = len(input_line)
    result_value = 0
    
    # Iterate through each possible length of substrings
    for substring_length in range(input_length):
        # Check each starting position for the substring of given length
        for start_index in range(input_length):
            # Extract the substring from the current starting position
            substring = input_line[start_index:start_index + substring_length + 1]
            
            # Check if the substring can be found later in the string
            if input_line.find(substring, start_index + 1) != -1:
                # Update the result_value to the current substring length
                result_value = substring_length
                break  # Exit the inner loop once a match is found
    
    # Output the maximum length of the found substring
    print(result_value)

# To test the function, you can call it. Uncomment to do so:
# find_max_repeated_substring_length()
