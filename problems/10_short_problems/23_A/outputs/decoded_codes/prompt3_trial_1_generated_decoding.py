def longest_repeated_substring_length():
    # Read input line from standard input
    input_line = input().strip()
    
    # Determine the length of the input line
    length_of_line = len(input_line)
    
    # Initialize variable to hold the result
    longest_repeated_substring_length = 0

    # Loop through possible substring lengths from 1 to length_of_line
    for substring_length in range(1, length_of_line):
        # Check for repeated substrings of the current length
        found_repeated = False
        
        for start_index in range(length_of_line - substring_length + 1):
            # Extract the substring starting at start_index with length substring_length
            current_substring = input_line[start_index:start_index + substring_length]
            
            # Search for the current_substring in the remainder of the input line
            if input_line.find(current_substring, start_index + 1) != -1:
                # Update the longest repeated substring length
                longest_repeated_substring_length = substring_length
                found_repeated = True
                break  # Exit the inner loop if a repeat is found
        
        # If no repeated substring of this length is found, exit the outer loop
        if not found_repeated:
            break

    # Output the length of the longest repeated substring found
    print(longest_repeated_substring_length)

# Call the function to execute
longest_repeated_substring_length()


# Test with the following sample input:
# Input: "banana"
# Expected output: 3 (for the substring "ana")

# Input: "abcdef"
# Expected output: 0 (no repeated substrings)

# Input: ""
# Expected output: 0 (empty input)

# Input: "abcabc"
# Expected output: 3 (for the substring "abc")
