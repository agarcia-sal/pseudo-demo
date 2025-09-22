def find_longest_repeating_substring():
    # Read a line of input from standard input and remove the trailing newline
    line = input().rstrip('\n')
    n = len(line)
    max_length = 0

    # Iterate over possible lengths of substrings
    for length in range(n):
        # Check for each starting position in the line
        for start in range(n):
            # Determine the current substring
            substring = line[start:start + length + 1]
            # Check if the substring exists later in the line
            if substring in line[start + 1:]:
                # Update the maximum length of found repeating substring
                max_length = length + 1  # +1 because range is 0 indexed
                break  # Break the inner loop as substring found

    # Output the maximum length of the found repeating substring
    print(max_length)

# Call the function to execute the process
find_longest_repeating_substring()
