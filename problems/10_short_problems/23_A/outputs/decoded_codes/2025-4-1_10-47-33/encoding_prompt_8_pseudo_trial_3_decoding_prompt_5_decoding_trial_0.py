def find_longest_prefix():
    # Read a line of input and strip the newline character
    input_string = input().strip()
    
    # Get the length of the input string
    string_length = len(input_string)
    
    # Initialize a variable to store the length of the longest prefix found
    longest_prefix_length = 0

    # Loop through potential prefix lengths from 0 up to string_length
    for current_length in range(1, string_length):  # start from 1 to avoid empty prefix
        # Check every starting position in the string
        for start_position in range(string_length):
            # Get the current substring for the prefix
            prefix_substring = input_string[start_position:start_position + current_length]
            
            # Check if the substring exists again in the string after the current position
            if (input_string.find(prefix_substring, start_position + 1) != -1):
                # Update the longest prefix length if a match is found
                longest_prefix_length = current_length
                break  # Exit the inner loop if a match is found

    # Output the length of the longest prefix found
    print(longest_prefix_length)

# Uncomment the following line to test the function
# find_longest_prefix()
