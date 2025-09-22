def find_max_repeated_substring_length():
    # Read input and remove trailing newline character
    line = input().rstrip()
    length_of_line = len(line)  # Store the length of the input line

    max_repeated_length = 0  # Initialize the maximum repeated length

    # Outer loop for each possible substring length
    for current_length in range(1, length_of_line):  # Start from length 1 to length_of_line - 1
        for start_index in range(length_of_line):
            if start_index + current_length <= length_of_line:  # Ensure substring is within bounds
                # Extract the substring
                substring = line[start_index:start_index + current_length]
                # Check for the substring after its current position
                if substring in line[start_index + 1:]:
                    max_repeated_length = current_length  # Update max repeated length
                    break  # Break if a repeat is found

    # Output the result
    print(max_repeated_length)

# Call the function to execute
find_max_repeated_substring_length()
