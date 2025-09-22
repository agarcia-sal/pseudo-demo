def find_max_repeated_substring_length():
    # Read a line of input from standard input
    line = input().strip()
    line_length = len(line)
    result_value = 0  # Initialize result value to 0

    # Loop through all possible substring lengths from 0 to line_length - 1
    for l in range(line_length):
        # Loop through each index in the line to check for repeated substrings
        for i in range(line_length):
            # Extract a substring of length l starting from current index i
            substring = line[i:i+l]
            
            # Check if this substring exists later in the line
            if substring in line[i + 1:]:
                # Update result_value to the current length l
                result_value = l
                break  # Exit inner loop if we found a repeated substring

    # Output the maximum length of the found repeated substring
    print(result_value)

# Call the function to execute
find_max_repeated_substring_length()
