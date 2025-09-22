def find_longest_repeated_substring():
    # Read a line of input and remove the trailing newline character
    line = input().strip()
    n = len(line)
    longest_repeated_length = 0

    # Iterate through possible lengths of substrings
    for length in range(n):  # length goes from 0 to n-1
        for start_index in range(n - length):  # Adjust range to ensure valid substring extraction
            # Extract the substring
            substring = line[start_index:start_index + length + 1]  # +1 to include the character at start_index + length

            # Check if the substring occurs again after the current index
            if substring in line[start_index + 1:]:
                longest_repeated_length = length + 1  # Set the length of the longest found substring
                break  # Found a repeated substring, exit inner loop

    # Output the length of the longest repeated substring
    print(longest_repeated_length)

# Call the function to execute
find_longest_repeated_substring()
