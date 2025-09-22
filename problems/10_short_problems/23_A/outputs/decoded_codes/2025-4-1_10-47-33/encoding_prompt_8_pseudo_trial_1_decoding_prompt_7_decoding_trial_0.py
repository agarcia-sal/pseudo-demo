# Function to find the length of the longest repeated substring
def longest_repeated_substring_length():
    # Read a line of input and strip newline characters
    input_line = input().strip()
    # Get the length of the input
    length_of_input = len(input_line)
    # Initialize the longest repeated length
    longest_repeated_length = 0

    # Loop through all possible substring lengths from 1 to (length of input)
    for substring_length in range(1, length_of_input):
        # Set to keep track of substrings we have seen
        seen_substrings = set()
        # Loop through all starting positions of the substring in the input
        for start_index in range(length_of_input - substring_length + 1):
            # Extract the current substring based on the start_index and substring_length
            current_substring = input_line[start_index:start_index + substring_length]
            # Check if the current substring has been seen already
            if current_substring in seen_substrings:
                # If it has, update the longest repeated length found
                longest_repeated_length = substring_length
            else:
                # Store the substring in the set
                seen_substrings.add(current_substring)

    # Output the length of the longest repeated substring
    print(longest_repeated_length)

# Call the function to execute
longest_repeated_substring_length()
