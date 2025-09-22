def find_longest_repeated_substring():
    # Step 1: Read input and remove trailing newline character
    input_line = input().strip()
    
    # Step 2: Get the length of the input line
    length_of_line = len(input_line)
    
    # Step 3: Initialize variable for length of longest repeated substring
    repeated_substring_length = 0
    
    # Step 4: Check for repeated substrings of varying lengths
    for substring_length in range(1, length_of_line):  # Start from length 1 to length_of_line - 1
        for start_index in range(length_of_line - substring_length):
            # Extract the substring
            substring = input_line[start_index:start_index + substring_length]
            
            # Check if the substring can be found again in the rest of the string
            if substring in input_line[start_index + substring_length:]:
                repeated_substring_length = substring_length  # Update repeated substring length
                break  # Exit the inner loop since we found a repeated substring
        else:
            continue  # This continues the outer loop if the inner loop doesn't break
        
        break  # Exit the outer loop since we found a repeated substring
            
    # Step 5: Output the length of the longest repeated substring
    print(repeated_substring_length)

# Execute the function
find_longest_repeated_substring()
