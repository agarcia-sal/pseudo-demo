# Start of the main program
def main():
    # Read input line from standard input
    input_line = input().strip()  # Remove trailing newline and any extra spaces
    line_length = len(input_line)  # Get the length of the input line
    repeat_index = 0  # Initialize repeat_index to store the length of longest repeating substring

    # Loop over lengths of possible substrings
    for length in range(1, line_length):  # Starting from 1 to avoid empty substring
        # Inner loop to check each starting position of the substring
        for start_index in range(line_length - length):  # Ensure start_index + length is valid
            # Create a substring of current length starting at start_index
            current_substring = input_line[start_index:start_index + length]
            
            # Check if the substring appears in the rest of the string after start_index
            if current_substring in input_line[start_index + length:]:
                # Update repeat_index to the current length if a repeat is found
                repeat_index = length  # Store the length of the substring found
                break  # Exit inner loop if we found a repeating substring

    # Output the highest length of the repeated substring found
    print(repeat_index)

# Execute the main function
main()
