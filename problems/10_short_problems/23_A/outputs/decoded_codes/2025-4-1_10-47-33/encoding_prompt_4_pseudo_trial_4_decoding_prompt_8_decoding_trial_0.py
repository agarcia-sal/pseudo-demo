def longest_repeated_substring_length():
    # Read a line of input and remove the trailing newline character
    line = input().strip()
    n = len(line)
    longest_repeated_length = 0

    # Iterate through possible lengths of substrings
    for length in range(n):
        # Check for repeated substrings of the current length
        for start_index in range(n - length):
            # Extract the substring
            substring = line[start_index:start_index + length + 1]

            # Check if the substring occurs again after the current index
            if substring in line[start_index + 1:]:
                longest_repeated_length = length + 1  # Adjust for length calculation
                break  # Exit the inner loop

    # Output the length of the longest repeated substring
    print(longest_repeated_length)

# Call the function to execute
longest_repeated_substring_length()
