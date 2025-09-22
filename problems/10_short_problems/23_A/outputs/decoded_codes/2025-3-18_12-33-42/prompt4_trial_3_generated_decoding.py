def find_longest_repeated_substring_length():
    # Read a line of input
    line = input().strip()
    n = len(line)
    longest_repeated_length = 0

    # Iterate over possible lengths of substrings
    for length in range(1, n):  # starting from 1 since a substring of length 0 is trivial
        # Check for each starting position in the string
        for start_position in range(n - length + 1):
            # Extract the substring of the given length starting from start_position
            substring = line[start_position:start_position + length]

            # Check if this substring appears again in the line
            if substring in line[start_position + length:]:
                longest_repeated_length = length  # Update the longest repeated length
                break  # Exit the inner loop as we found a repetition for this length

    # Output the longest length of the repeated substring found
    print(longest_repeated_length)

# Call the function to execute
find_longest_repeated_substring_length()
