# This program processes a string input by replacing certain words with symbols
# and ensuring specific formatting rules are followed.

def process_string():
    # Read input from user
    input_string = input()
    
    # Replace words with symbols
    input_string = input_string.replace('dot', '.')
    input_string = input_string.replace('at', '@')
    
    # Ensure the string starts with 'dot' if it begins with '.'
    if input_string.startswith('.'):
        input_string = 'dot' + input_string[1:]

    # Initialize variables for processing
    count_at_symbol = 0
    processed_characters = []
    
    # Ensure the string starts with 'at' if it begins with '@'
    if input_string.startswith('@'):
        input_string = 'at' + input_string[2:]

    # Process each character in the modified string
    for character in input_string:
        if character == '@':
            # Check if the character '@' appears consecutively
            if count_at_symbol > 0:
                processed_characters.append('at')
            else:
                processed_characters.append('@')
            count_at_symbol = 1
        else:
            processed_characters.append(character)
            count_at_symbol = 0  # Reset count for other characters

    # Join processed characters into a single string
    result_string = ''.join(processed_characters)

    # Replace trailing '.' with 'dot'
    if result_string.endswith('.'):
        result_string = result_string[:-1] + 'dot'

    # Output the final processed string
    print(result_string)

# Example test case
# Input: "dothello at world.."
# Expected output: "hello @ worlddot"
process_string()
