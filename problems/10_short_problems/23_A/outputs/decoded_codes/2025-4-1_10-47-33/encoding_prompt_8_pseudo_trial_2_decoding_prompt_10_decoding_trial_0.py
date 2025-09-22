def find_longest_repeated_substring():
    # Read input and remove the last character
    input_line = input()[:-1]  
    length_of_line = len(input_line)
    longest_repeated_length = 0  # Initialize the tracker for longest repeating substring length

    # Outer loop for each possible substring length from 0 to length_of_line - 1
    for current_length in range(1, length_of_line):  # Start from 1 to find non-empty substrings
        # Inner loop for each possible starting position in the string
        for start_index in range(length_of_line - current_length + 1):
            # Extract the substring
            substring = input_line[start_index:start_index + current_length]

            # Check for repetition
            if input_line.find(substring, start_index + 1) != -1:  # Find substring after its position
                longest_repeated_length = current_length  # Update the longest found repetition
                break  # No need to check more substrings of this length

    # Output the result
    print(longest_repeated_length)

# Call the function to execute
find_longest_repeated_substring()
