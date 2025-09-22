def find_max_repeating_substring_length():
    # Read a line of input from the standard input
    line_of_text = input().strip()  # Removing any surrounding white space including new lines
    line_length = len(line_of_text)   # Length of the input line
    
    # Initialize a variable to store the maximum length of the substring found
    max_length = 0

    # Loop over possible lengths of substrings from 1 to line_length (not 0)
    for length in range(1, line_length + 1):
        # Loop over each starting position in the string
        for start_position in range(line_length - length + 1):
            # Extract the substring from start_position of the current length
            current_substring = line_of_text[start_position:start_position + length]

            # Check if this substring appears later in the line_of_text
            if current_substring in line_of_text[start_position + length:]:
                # If found, update max_length with the current length
                max_length = length
                # Exit the inner loop, as one match is enough
                break

    # Output the maximum length of the found substring
    print(max_length)

# To test the implementation you could call find_max_repeating_substring_length() in an interactive Python environment.

