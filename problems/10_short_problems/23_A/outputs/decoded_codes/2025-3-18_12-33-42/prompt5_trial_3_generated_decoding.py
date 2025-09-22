def longest_repeating_substring():
    # Read a single line of input, which is a string
    string_line = input()
    
    # Get the length of the input string
    string_length = len(string_line)
    
    # Initialize a variable to store the length of the longest repeating substring
    longest_repeat_length = 0

    # Loop over possible substring lengths from 1 to the length of the string
    for current_length in range(1, string_length):
        # Loop over each starting position of the substring up to the maximum length
        for start_position in range(string_length - current_length + 1):
            # Define the current substring from start_position with current_length
            current_substring = string_line[start_position:start_position + current_length]
            
            # Check if this substring exists elsewhere in the string
            if current_substring in string_line[start_position + current_length:]:
                # If a repeat is found, update longest_repeat_length and exit the inner loop
                longest_repeat_length = current_length
                break  # Found a repeat, no need to check further for this length

    # Output the length of the longest repeating substring
    print(longest_repeat_length)

# Consider testing the function with various inputs:
# longest_repeating_substring('ababc') should output 2
# longest_repeating_substring('abcd') should output 0
# longest_repeating_substring('aaaaaa') should output 1
