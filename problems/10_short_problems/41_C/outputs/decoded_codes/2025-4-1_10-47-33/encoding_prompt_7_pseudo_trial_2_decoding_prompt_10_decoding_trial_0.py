def process_input():
    # Read input from standard input and strip any surrounding whitespace
    input_string = input().strip()

    # Replace occurrences of 'dot' with '.' and 'at' with '@'
    input_string = input_string.replace('dot', '.').replace('at', '@')

    # Check and prefix with 'dot' if the first character is a '.'
    if input_string.startswith('.'):
        input_string = 'dot' + input_string

    count_at = 0  # Variable to count occurrences of '@'
    updated_characters = []  # List to hold processed characters

    # Check and prefix with 'at' if the first character is '@'
    if input_string.startswith('@'):
        input_string = 'at' + input_string

    # Iterate through each character in the input string
    for character in input_string:
        if character == '@':
            # Check if we've already appended one '@'
            if count_at > 0:
                updated_characters.append('at')
                count_at = 1  # Update to note we've seen an '@'
            else:
                updated_characters.append('@')
                count_at = 1  # Update to note we've added an '@' already
        else:
            updated_characters.append(character)

    # Combine the updated character list back into a string
    final_string = ''.join(updated_characters)

    # If the final string ends with a '.', replace it with 'dot'
    if final_string.endswith('.'):
        final_string = final_string[:-1] + 'dot'

    # Print the final processed string
    print(final_string)

# Call the function to execute
process_input()
