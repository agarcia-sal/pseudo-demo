def process_input():
    # Read input from standard input
    input_string = input().strip()
    
    # Replace 'dot' with '.' and 'at' with '@'
    input_string = input_string.replace('dot', '.').replace('at', '@')
    
    # If the first character is '.', prepend 'dot'
    if input_string.startswith('.'):
        input_string = 'dot' + input_string[1:]

    # Initialize variables
    count_at = 0
    result_characters = []
    
    # If the first character is '@', prepend 'at'
    if input_string.startswith('@'):
        input_string = 'at' + input_string[1:]

    # Loop through each character in the modified input_string
    for character in input_string:
        if character == '@':
            # If '@' has been encountered before, append 'at' instead of another '@'
            if count_at > 0:
                result_characters.append('at')
                count_at = 1
            else:
                result_characters.append('@')
                count_at = 1
        else:
            # Add non-'@' characters to result
            result_characters.append(character)

    # Join the list of characters to form the final output string
    final_string = ''.join(result_characters)

    # Handle trailing '.' in the final string by replacing it with 'dot'
    if final_string.endswith('.'):
        final_string = final_string[:-1] + 'dot'

    # Print the resulting string
    print(final_string)

# Execute the function
process_input()
