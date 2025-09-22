def get_longest_prefix_length():
    # Read a line of input
    input_string = input().strip()
    
    # Get the length of the input string
    string_length = len(input_string)
    
    # Initialize a variable to store the result
    longest_prefix_length = 0

    # Loop through potential prefix lengths from 0 up to string_length - 1
    for current_length in range(string_length):
        # Check every starting position in the string
        for start_position in range(string_length):
            # Extract the substring to check
            substring = input_string[start_position:start_position + current_length]
            
            # Check if the substring exists again elsewhere in the string
            if (substring in input_string[start_position + 1:]):
                # Update the longest prefix length if a match is found
                longest_prefix_length = current_length
                break  # Exit the inner loop if a match is found

    # Output the length of the longest prefix found
    print(longest_prefix_length)

# Invoke the function to execute
get_longest_prefix_length()
