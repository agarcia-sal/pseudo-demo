def process_input():
    # Read input from standard input
    input_string = input().strip()

    # Replace occurrences of 'dot' with '.' and 'at' with '@'
    input_string = input_string.replace('dot', '.').replace('at', '@')

    # If the first character is a dot, prefix the string with 'dot'
    if input_string.startswith('.'):
        input_string = 'dot' + input_string

    # Initialize variables for further processing
    count_at = 0
    updated_characters = []

    # Check for leading '@' character and prefix with 'at' if present
    if input_string.startswith('@'):
        input_string = 'at' + input_string

    # Iterate through each character in the input string
    for character in input_string:
        if character == '@':
            # Append 'at' if we've already appended one '@'
            if count_at > 0:
                updated_characters.append('at')
            else:
                updated_characters.append('@')
                count_at = 1  # Note we've added an '@'
        else:
            updated_characters.append(character)

    # Combine the updated character list back into a string
    final_string = ''.join(updated_characters)

    # If the final string ends with a dot, replace it with 'dot'
    if final_string.endswith('.'):
        final_string = final_string[:-1] + 'dot'

    # Print the final processed string
    print(final_string)

# Example usage: Uncomment to run the function
# process_input()
