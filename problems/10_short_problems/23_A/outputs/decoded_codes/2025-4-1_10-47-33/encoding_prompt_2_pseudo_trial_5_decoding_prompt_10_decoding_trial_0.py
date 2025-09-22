def longest_repeated_substring_length():
    # 1. Read input string and remove the newline character at the end
    input_string = input().strip()
    
    # 2. Determine the length of the input string
    length_of_input_string = len(input_string)
    
    # 3. Initialize the variable for the longest repeated substring length
    longest_repeated_substring_length = 0
    
    # 4. Loop through each possible length of substrings
    for current_length in range(1, length_of_input_string):  # Starting from 1 to avoid empty substrings
        # 5. For each starting position of the substring
        for start_position in range(length_of_input_string - current_length + 1):
            # 6. Extract the substring
            substring = input_string[start_position:start_position + current_length]
            
            # 7. Check if this substring can be found again in the string after its current position
            if substring in input_string[start_position + 1:]:
                # 8. Update the longest repeated substring length
                longest_repeated_substring_length = current_length
                break  # Found a repeated substring, no need to check further for this length
    
    # 10. Output the value of the longest repeated substring length
    print(longest_repeated_substring_length)

# Running the function for testing
longest_repeated_substring_length()
