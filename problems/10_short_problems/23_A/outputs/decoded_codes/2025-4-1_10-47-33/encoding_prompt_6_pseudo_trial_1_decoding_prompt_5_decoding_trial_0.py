def find_longest_repeated_substring():
    # Read a line of input from the user and remove the trailing newline character
    line = input().rstrip()
    length_of_line = len(line)
    repeat_length = 0

    # Loop through lengths from 0 to length_of_line - 1
    for length in range(length_of_line):
        # Check for all starting positions of substring of this length
        for start_position in range(length_of_line):
            # Extract the current substring from the line
            current_substring = line[start_position:start_position + length]

            # Check if this substring appears again in line starting from the next character
            if current_substring in line[start_position + 1:]:
                # Update repeat_length to be the current length if a repeat is found
                repeat_length = length
                break  # Break out of inner loop

        # Break out of the outer loop if a repeat has been found
        if repeat_length != 0:
            break

    # Output the longest length of repeated substring found
    print(repeat_length)

# Example of running the function (uncomment the line below to use it)
# find_longest_repeated_substring()
