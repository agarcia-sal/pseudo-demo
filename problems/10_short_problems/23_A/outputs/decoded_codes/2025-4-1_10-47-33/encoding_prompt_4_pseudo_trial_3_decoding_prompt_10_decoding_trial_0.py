def find_longest_repeated_substring():
    line = input()  # Read input string from user
    n = len(line)
    longest_repetition_length = 0

    # Loop through possible substring lengths from 1 to n-1
    for length in range(1, n):  # starts from 1 since we want repeated substrings
        # Loop through the starting position of the substring
        for start_position in range(n - length):  # Adjust to prevent overflow
            # Extract the substring of the current length
            substring = line[start_position:start_position + length]
            # Check if this substring occurs again in the line
            if substring in line[start_position + length:]:  # Avoid checking the same part
                longest_repetition_length = length
                break  # Found a repetition, break out of the inner loop
        else:
            continue  # This is executed if the inner loop didn't break
        break  # If we found a repetition, we can break out of the outer loop

    # Output the length of the longest repeated substring found
    print(longest_repetition_length)
