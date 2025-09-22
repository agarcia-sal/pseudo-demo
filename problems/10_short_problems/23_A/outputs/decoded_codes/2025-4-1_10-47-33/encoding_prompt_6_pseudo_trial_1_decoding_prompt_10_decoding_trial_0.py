def find_longest_repeated_substring():
    # Read a line of input from the user and remove the trailing newline character
    line = input().rstrip()  # Use rstrip to remove the last character if it's a newline
    length_of_line = len(line)
    repeat_length = 0

    # Loop through lengths from 0 to length_of_line - 1
    for length in range(length_of_line):
        # Check for all starting positions of substring of this length
        for start_position in range(length_of_line):
            # Extract the current substring from the line
            current_substring = line[start_position:start_position + length + 1]

            # Check if this substring appears again in line starting from the next character
            if current_substring in line[start_position + 1:]:
                # Update repeat_length to be the current length if a repeat is found
                repeat_length = length + 1  # +1 for length since it's 0 indexed
                break  # Found a repeat, break out of the inner loop

        # Break out of the outer loop if a repeat has been found
        if repeat_length != 0:
            break

    # Output the longest length of repeated substring found
    print(repeat_length)

# Call the function to execute it
find_longest_repeated_substring()
