def longest_repeated_substring_length():
    # Read a line of input and remove the trailing newline character
    input_line = input().strip()
    
    # Determine the length of the input line
    n = len(input_line)
    
    # Initialize a variable to hold the result
    repeated_length = 0
    
    # Loop through lengths of substrings from 0 to n-1
    for length in range(n):  # 0 to n-1
        # Check for substrings of the current length
        for start_index in range(n - length):  # Ensure index doesn't go out of bounds
            # Extract a substring from the current start index
            substring = input_line[start_index:start_index + length + 1]
            
            # Check if the substring occurs again later in the string
            if substring in input_line[start_index + 1:]:
                # Update the result with the current length
                repeated_length = length + 1  # +1 because length is zero-based
                break  # Exit inner loop if a repeat is found
                
    # Output the length of the longest repeated substring
    print(repeated_length)

# Run the function
longest_repeated_substring_length()
