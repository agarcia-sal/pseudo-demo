def find_longest_prefix():
    # Read a line of input
    input_string = input().strip()  # Read input and remove any extra whitespaces

    # Get the length of the input string
    string_length = len(input_string)
    
    # Variable to store the length of the longest prefix found
    longest_prefix_length = 0

    # Loop through potential prefix lengths from 1 to string_length
    for current_length in range(1, string_length + 1):
        # Loop through every starting position in the string
        for start_position in range(string_length):
            # Extract the current prefix substring
            prefix_substring = input_string[start_position:start_position + current_length]

            # Ensure the prefix is of the desired length before checking
            if len(prefix_substring) < current_length:
                continue

            # Check if the prefix substring exists again in the string after its position
            if input_string.find(prefix_substring, start_position + 1) != -1:
                # Update the longest prefix length if a match is found
                longest_prefix_length = current_length
                break  # Exit the inner loop if a match is found

    # Output the length of the longest prefix found
    print(longest_prefix_length)

# Call the function to execute
find_longest_prefix()
