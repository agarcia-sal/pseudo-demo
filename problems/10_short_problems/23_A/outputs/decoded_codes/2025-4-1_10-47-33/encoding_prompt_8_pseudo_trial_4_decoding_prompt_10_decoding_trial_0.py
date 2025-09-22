def longest_repeated_substring():
    # Step 1: Read input
    input_line = input().strip()
    
    # Step 2: Initialize variables
    length_of_input = len(input_line)
    max_length = 0  # To track the length of the longest repeated substring

    # Step 3: Check for repeated substrings
    for current_length in range(length_of_input):  # current_length from 0 to length_of_input - 1
        for start_index in range(length_of_input):  # startIndex from 0 to length_of_input - 1
            if start_index + current_length > length_of_input:
                break  # Avoids substring extraction that exceeds the string length
            
            # Step 5: Extract substring
            substring = input_line[start_index:start_index + current_length]
            
            # Step 6: Check if the substring appears again after its position
            if substring in input_line[start_index + 1:]:  # Look for substring from the next character
                max_length = current_length  # Update maxLength
                break  # Exit the inner loop since we found a repeating substring

    # Step 7: Output the result
    print(max_length)

# Calling the function to execute
longest_repeated_substring()
