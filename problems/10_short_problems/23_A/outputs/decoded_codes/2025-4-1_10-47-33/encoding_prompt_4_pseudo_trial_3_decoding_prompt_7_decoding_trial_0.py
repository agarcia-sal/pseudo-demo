def find_longest_repeated_substring():
    # Read the input string from the user
    line = input()
    n = len(line)  # Get the length of the input line
    longest_repetition_length = 0  # Initialize the length of the longest repetition found

    # Loop through possible substring lengths from 1 to n-1
    for length in range(1, n):  # Start from length 1 to avoid trivial empty substring
        # Loop through the starting position of the substring
        for start_position in range(n - length):  # Ensure we don't go out of bounds
            # Extract the substring of the current length
            substring = line[start_position:start_position + length]
            # Check if this substring occurs again in the line
            if substring in line[start_position + length:]:  # Check in substring after current position
                longest_repetition_length = length  # Update the longest repetition length
                break  # Exit inner loop once a repetition is found

    # Output the length of the longest repeated substring found
    print(longest_repetition_length)

# The function can be called to execute the logic
find_longest_repeated_substring()
