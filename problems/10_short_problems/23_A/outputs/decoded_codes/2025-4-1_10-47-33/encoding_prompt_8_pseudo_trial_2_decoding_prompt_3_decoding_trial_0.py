def find_longest_repeated_substring():
    # Read input from standard input
    line = input()[:-1]  # Exclude the last character as per the pseudocode

    # Initialize variables
    length_of_line = len(line)
    longest_repeated_length = 0

    # Outer loop for each potential substring length
    for current_length in range(1, length_of_line):  # Starts from 1 to avoid the empty substring
        # Inner loop for each possible starting position in the string
        for start_index in range(length_of_line - current_length + 1):
            # Extract the substring
            substring = line[start_index:start_index + current_length]

            # Check for repetition
            if substring in line[start_index + 1:]:  # Search in the remaining part of the line
                longest_repeated_length = current_length
                break  # Break inner loop since we found a repeated substring

    # Output result
    print(longest_repeated_length)

# Call the function to execute
find_longest_repeated_substring()
