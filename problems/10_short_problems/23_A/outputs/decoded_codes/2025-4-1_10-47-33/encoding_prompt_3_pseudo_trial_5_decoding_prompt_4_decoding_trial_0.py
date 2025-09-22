def main():
    # Read input line from standard input and remove the trailing newline
    input_line = input().strip()
    line_length = len(input_line)
    repeat_index = 0
    
    # Loop over lengths of possible substrings
    for length in range(line_length):
        # Inner loop to check each starting position of the substring
        for start_index in range(line_length):
            # Create a substring of current length starting at start_index
            current_substring = input_line[start_index:start_index + length]
            
            # Check if the substring appears in the rest of the string after start_index
            if current_substring in input_line[start_index + 1:]:
                # Update repeat_index to the current length if a repeat is found
                repeat_index = length
                break  # Break out of inner loop
        
    # Output the highest length of the repeated substring found
    print(repeat_index)

# Call main to execute the function
main()
