def longest_repeated_substring():
    # Read a line of input and strip any trailing whitespace (including newlines)
    input_line = input().strip()
    length_of_input = len(input_line)
    longest_repeated_length = 0

    # Loop through all possible substring lengths from 1 to (length_of_input - 1)
    for substring_length in range(1, length_of_input):
        # Loop through all starting positions of the substring in the input
        for start_index in range(length_of_input - substring_length + 1):
            # Extract the current substring based on the start_index and substring_length
            current_substring = input_line[start_index:start_index + substring_length]
            
            # Check if the current substring appears again in the input beyond its starting position
            if current_substring in input_line[start_index + 1:]:
                # If it does, update the length of the longest repeated substring found
                longest_repeated_length = substring_length
                break  # Exit the inner loop as we found a repeat

    # Output the length of the longest repeated substring
    print(longest_repeated_length)

# Call the function to execute
longest_repeated_substring()
