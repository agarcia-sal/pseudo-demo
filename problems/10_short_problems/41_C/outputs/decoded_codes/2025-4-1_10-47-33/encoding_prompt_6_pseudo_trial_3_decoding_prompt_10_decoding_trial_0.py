def process_input():
    # Read a line of input and remove any surrounding whitespace
    input_line = input().strip()

    # Replace occurrences of 'dot' with '.' and 'at' with '@'
    input_line = input_line.replace('dot', '.').replace('at', '@')

    # If the modified input starts with a '.', prepend 'dot' to it
    if input_line.startswith('.'):
        input_line = 'dot' + input_line

    # Initialize a count for consecutive '@' symbols and a list for output characters
    consecutive_at_count = 0
    output_characters = []

    # If the modified input starts with '@', prepend 'at' to it
    if input_line.startswith('@'):
        input_line = 'at' + input_line

    # Iterate through each character in the modified input
    for character in input_line:
        if character == '@':
            # If consecutive '@', append 'at' to the output list
            if consecutive_at_count > 0:
                output_characters.append('at')
                consecutive_at_count = 1  # Count consecutive '@'
            else:
                output_characters.append('@')
                consecutive_at_count = 1  # Count first '@'
        else:
            # If it is not '@', append the character to the list
            output_characters.append(character)
        
        # Reset consecutive count if the character is not '@'
        if character != '@':
            consecutive_at_count = 0

    # Join all characters in the output list into a final string
    modified_text = ''.join(output_characters)

    # If the last character in the modified text is '.', replace it with 'dot'
    if modified_text.endswith('.'):
        modified_text = modified_text[:-1] + 'dot'

    # Print the final modified text
    print(modified_text)

# Example usage:
process_input()
