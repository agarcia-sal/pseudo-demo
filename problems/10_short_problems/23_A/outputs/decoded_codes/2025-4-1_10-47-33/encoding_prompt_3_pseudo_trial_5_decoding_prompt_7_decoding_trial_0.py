def main():
    # Read input line from standard input and remove the trailing newline
    input_line = input().strip()
    line_length = len(input_line)
    repeat_index = 0  # Variable to store the length of the longest repeating substring

    # Loop over lengths of possible substrings
    for length in range(1, line_length):  # Start from length 1 to avoid empty substring
        # Inner loop to check each starting position of the substring
        for start_index in range(line_length):
            # Check if a substring would be valid based on length and starting index
            if start_index + length <= line_length:
                # Create a substring of current length starting at start_index
                current_substring = input_line[start_index:start_index + length]
                
                # Check if the substring appears in the rest of the string after startIndex
                if current_substring in input_line[start_index + 1:]:
                    # Update repeatIndex to the current length if a repeat is found
                    repeat_index = length
                    break  # Break out of inner loop since we found a repeat

    # Output the highest length of the repeated substring found
    print(repeat_index)

if __name__ == "__main__":
    main()
