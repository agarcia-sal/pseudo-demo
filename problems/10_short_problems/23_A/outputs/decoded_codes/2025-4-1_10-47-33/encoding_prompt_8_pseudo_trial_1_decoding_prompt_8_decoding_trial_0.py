def longest_repeated_substring():
    # Read a line of input and remove the trailing newline character
    input_line = input().rstrip()
    length_of_input = len(input_line)
    longest_repeated_length = 0

    # Loop through all possible substring lengths from 1 to (length of input)
    for substring_length in range(1, length_of_input):
        # Loop through all starting positions of the substring in the input
        for start_index in range(length_of_input - substring_length + 1):
            # Extract the current substring based on the start_index and substring_length
            current_substring = input_line[start_index:start_index + substring_length]
            
            # Check if the current substring appears again in the input beyond its starting position
            if current_substring in input_line[start_index + 1:]:
                # If it does, update the length of the longest repeated substring found
                longest_repeated_length = substring_length
                break  # Found a repeated substring of this length, break inner loop
        else:
            continue  # Continue with the outer loop if no break occurred
        break  # Break outer loop since we found a repeated substring of this length

    # Output the length of the longest repeated substring
    print(longest_repeated_length)

# To test the function, you could call:
# longest_repeated_substring()
