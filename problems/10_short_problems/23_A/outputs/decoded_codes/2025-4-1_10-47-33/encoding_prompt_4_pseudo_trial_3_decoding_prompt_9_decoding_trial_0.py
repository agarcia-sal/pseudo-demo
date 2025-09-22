def find_longest_repeated_substring():
    # Read input string
    line = input()
    n = len(line)
    longest_repetition_length = 0

    # Loop through possible substring lengths from 0 to n-1
    for length in range(1, n):  # Start from length 1 to n-1
        # Loop through the starting position of the substring
        for start_position in range(n - length + 1):  # Ensure the substring fits
            # Extract the substring of the current length
            substring = line[start_position:start_position + length]
            # Check if this substring occurs again in the line
            if substring in line[start_position + length:]:  # Check after the current position
                longest_repetition_length = length
                break  # Exit inner loop once a repetition is found

    # Output the length of the longest repeated substring found
    print(longest_repetition_length)
