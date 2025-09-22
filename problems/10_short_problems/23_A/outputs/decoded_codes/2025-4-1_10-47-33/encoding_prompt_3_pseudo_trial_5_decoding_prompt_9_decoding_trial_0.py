def main():
    # Read input line from standard input and remove the trailing newline
    input_line = input().strip()  # Remove whitespace characters including newline
    line_length = len(input_line)
    repeat_index = 0  # Initialize variable to hold the length of the longest repeating substring

    # Loop over lengths of possible substrings
    for length in range(0, line_length):
        # Inner loop to check each starting position of the substring
        for start_index in range(0, line_length):
            # Create a substring of current length starting at start_index
            current_substring = input_line[start_index:start_index + length]

            # Check if the substring appears in the rest of the string after start_index
            if input_line.find(current_substring, start_index + 1) != -1:
                # Update repeat_index to the current length if a repeat is found
                repeat_index = length
                break  # Break out of inner loop

    # Output the highest length of the repeated substring found
    print(repeat_index)

# Run the main function
main()
