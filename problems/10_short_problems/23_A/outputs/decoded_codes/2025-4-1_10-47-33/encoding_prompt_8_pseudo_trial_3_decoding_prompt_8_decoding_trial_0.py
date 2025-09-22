def longest_prefix_repeating_substring():
    # Read a line of input, excluding the last character (newline)
    input_string = input()
    
    # Get the length of the input string
    string_length = len(input_string)
    
    # Initialize a variable to store the result
    longest_prefix_length = 0

    # Loop through potential prefix lengths from 0 up to string_length
    for current_length in range(string_length):
        
        # Check every starting position in the string
        for start_position in range(string_length):
            
            # Extract the substring from the current starting position
            substring = input_string[start_position:start_position + current_length]
            
            # Check if the substring exists again elsewhere in the string
            if substring and input_string.find(substring, start_position + 1) != -1:
                
                # Update the longest prefix length if a match is found
                longest_prefix_length = current_length
                break  # Exit the inner loop if a match is found

    # Output the length of the longest prefix found
    print(longest_prefix_length)

# Invoke the function to test
longest_prefix_repeating_substring()
