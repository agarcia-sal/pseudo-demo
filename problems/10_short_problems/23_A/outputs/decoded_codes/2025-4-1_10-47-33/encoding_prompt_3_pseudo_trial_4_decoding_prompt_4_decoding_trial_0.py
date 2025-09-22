def find_longest_repeated_substring():
    # Read a line of input, removing the last character (newline)
    line = input().strip()
    line_length = len(line)
    result_value = 0

    # Loop through all possible substring lengths from 0 to line_length - 1
    for length in range(line_length):
        # Loop through each index in the line to check for repeated substrings
        for index in range(line_length):
            # Extract a substring of the current length starting from the current index
            substring = line[index:index + length]
            
            # Check if this substring occurs again later in the line
            if substring in line[index + 1:]:
                # Update the result_value to the current length
                result_value = length
                break  # Exit the inner loop if a repeat is found
                
    # Output the maximum length of the found repeated substring
    print(result_value)

# Call the function to execute the code
find_longest_repeated_substring()
