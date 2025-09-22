def find_longest_repeated_substring():
    # Read the input string from the user
    line = input()
    n = len(line)
    longest_repetition_length = 0

    # Loop through possible substring lengths from 1 to n-1
    for length in range(1, n):
        # Loop through the starting position of the substring
        for start_position in range(n - length):
            # Extract the substring of the current length
            substring = line[start_position:start_position + length]
            # Check if this substring occurs again in the line
            if substring in line[start_position + length:]:
                longest_repetition_length = length
                break  # Found a repetition, exit the inner loop

    # Output the length of the longest repeated substring found
    print(longest_repetition_length)

# Note: No parameters are used for input, as per the requirement.
