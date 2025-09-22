def read_input_line():
    # Read a line of input from standard input and return it without the trailing newline
    return input().strip()

def substring_exists(line, start_position, length):
    # Extract the substring based on the given start position and length
    substring = line[start_position:start_position + length]
    # Check if the substring appears later in the line
    return line.find(substring, start_position + 1) != -1

def longest_repeated_substring_length(line):
    # Determine the length of the input line
    line_length = len(line)
    # Initialize a variable to keep track of the longest repeated substring length
    longest_repeated_length = 0

    # Iterate over all possible substring lengths from 1 to line_length (inclusive)
    for substring_length in range(1, line_length):
        # Check each starting position in the line for the substring of the current length
        for starting_position in range(line_length):
            # Check if the substring exists in the line
            if substring_exists(line, starting_position, substring_length):
                # Update the longest repeated length found
                longest_repeated_length = substring_length
                break  # Exit the inner loop as we found a repeated substring
        else:
            # If we did not break, it means no repeated substrings of this length were found
            continue  # Continue to the next substring length
        break  # If we broke out of the inner loop, we stop checking longer lengths
    
    # Return the length of the longest repeated substring
    return longest_repeated_length

# Main execution
if __name__ == "__main__":
    input_line = read_input_line()
    result = longest_repeated_substring_length(input_line)
    print(result)
