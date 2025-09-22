def longest_prefix_repeated_substring(input_string):
    # Get the length of the input string
    string_length = len(input_string)

    # Initialize a variable to store the result
    longest_prefix_length = 0

    # Loop through potential prefix lengths from 0 up to string_length
    for current_length in range(string_length):
        # Check every starting position in the string
        for start_position in range(string_length):
            # Get the current prefix substring
            prefix = input_string[start_position:start_position + current_length]
            
            # Avoid checking beyond the string bounds
            if start_position + current_length >= string_length:
                break
            
            # Check if the prefix exists again elsewhere in the string
            if input_string.find(prefix, start_position + 1) != -1:
                # Update the longest prefix length if a match is found
                longest_prefix_length = current_length
                break  # Exit the inner loop if a match is found

    # Output the length of the longest prefix found
    return longest_prefix_length

# Read input
input_string = input()
# Call the function with the input string and print the result
print(longest_prefix_repeated_substring(input_string))
