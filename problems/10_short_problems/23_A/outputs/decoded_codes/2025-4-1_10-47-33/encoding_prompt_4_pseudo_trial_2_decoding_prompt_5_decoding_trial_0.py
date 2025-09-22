def read_input_line():
    # Read a line of input from standard input and return it without the newline
    return input().strip()

def substring_exists(line, start_position, length):
    # Extract the substring based on the given start position and length
    substring = line[start_position:start_position + length]
    # Check if the substring appears later in the line
    return line.find(substring, start_position + 1) != -1

def main():
    # Read input line
    input_line = read_input_line()
    # Determine the length of the input line
    line_length = len(input_line)

    # Initialize a variable to keep track of the longest repeated substring length
    longest_repeated_length = 0

    # Iterate over all possible substring lengths from 1 to line_length (0 cannot have repetitions)
    for substring_length in range(1, line_length):
        # Check each starting position in the line for the substring of current length
        for starting_position in range(line_length):
            # Check if the substring from the current starting position of the given length is found later in the string
            if substring_exists(input_line, starting_position, substring_length):
                # Update the longest repeated length found
                longest_repeated_length = substring_length
                break  # Exit the inner loop as we found a repeated substring
        else:
            continue  # Only executed if the inner loop did NOT break
        break  # Break the outer loop if an inner loop break occurs

    # Output the length of the longest repeated substring
    print(longest_repeated_length)

# Call the main function to execute the program
main()
