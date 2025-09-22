def longest_repeated_substring_length():
    # Step 1: Read input and remove any newline characters
    input_string = input().strip()

    # Step 2: Get the length of the input string
    length_of_input_string = len(input_string)

    # Step 3: Initialize variable for tracking the longest repeated substring length
    longest_repeated_substring_length = 0

    # Step 4: Loop through each possible length of substrings
    for current_length in range(1, length_of_input_string):  # Start from 1 to avoid zero-length substrings
        
        # Step 5: Check each starting position
        for start_position in range(length_of_input_string - current_length + 1):
            # Step 6: Extract the substring
            substring = input_string[start_position:start_position + current_length]
            
            # Step 7: Check for repeated occurrences
            if substring in input_string[start_position + 1:]:
                # Step 8: Update the length of the longest repeated substring found
                longest_repeated_substring_length = current_length
                break  # Break out of the inner loop once a match is found

    # Step 10: Output the result
    print(longest_repeated_substring_length)

# Function call to execute the code
longest_repeated_substring_length()
