def find_max_repeated_substring_length():
    # Read a line of input
    line = input().strip()
    line_length = len(line)
    result_value = 0

    # Loop through all possible substring lengths from 0 to line_length - 1
    for l in range(line_length):
        # Loop through each index in the line to check for repeated substrings
        for i in range(line_length):
            # Extract a substring of length l starting from current index i
            substring = line[i:i + l]
            # Check if this substring occurs again later in the line
            if substring in line[i + 1:]:
                # Update the result_value to the current length l
                result_value = l
                break  # Break out of the inner loop

    # Output the maximum length of the found repeated substring
    print(result_value)

# Testing the function with different scenarios
if __name__ == "__main__":
    # The function can be called as part of a real test case
    find_max_repeated_substring_length()
