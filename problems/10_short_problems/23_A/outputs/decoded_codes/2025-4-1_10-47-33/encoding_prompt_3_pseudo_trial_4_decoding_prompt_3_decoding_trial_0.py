def find_longest_repeated_substring():
    # Read a line of input, removing the last character (newline)
    line = input().strip()
    line_length = len(line)
    result_value = 0

    # Loop through all possible substring lengths from 0 to line_length - 1
    for l in range(line_length):
        # Loop through each index in the line to check for repeated substrings
        for i in range(line_length):
            if i + l <= line_length:  # Ensure we don't go out of bounds
                substring = line[i:i+l]  # Extract a substring of length l
            
                # Check if this substring occurs again later in the line
                if substring in line[i + 1:]:  # Search from the next index
                    result_value = l  # Update result_value to the current length l
                    break  # Break out of the inner loop

    # Output the maximum length of the found repeated substring
    print(result_value)

# Call the function to run the program
find_longest_repeated_substring()
