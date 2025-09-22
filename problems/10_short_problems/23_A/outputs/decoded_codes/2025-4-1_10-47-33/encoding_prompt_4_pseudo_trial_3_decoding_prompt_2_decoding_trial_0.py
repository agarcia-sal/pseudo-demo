def find_longest_repeated_substring():
    line = input()
    n = len(line)
    longest_repetition_length = 0

    # Loop through possible substring lengths from 0 to n-1
    for length in range(n):
        # Loop through the starting position of the substring
        for start_position in range(n):
            # Extract the substring of the current length
            substring = line[start_position:start_position + length]

            # Check if this substring occurs again in the line
            if substring in line[start_position + 1:]:
                longest_repetition_length = length
                break  # Break out of the inner loop
        else:
            continue  # Continue if the inner loop wasn't broken
        break  # Break the outer loop if inner loop was broken

    # Output the length of the longest repeated substring found
    print(longest_repetition_length)

