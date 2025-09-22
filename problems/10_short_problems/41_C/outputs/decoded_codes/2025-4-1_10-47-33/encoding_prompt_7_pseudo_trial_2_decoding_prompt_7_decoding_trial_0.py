def process_input():
    # Read input from standard input
    input_string = input().strip()

    # Replace occurrences of 'dot' with '.' and 'at' with '@'
    input_string = input_string.replace('dot', '.')
    input_string = input_string.replace('at', '@')

    # If the first character is a dot, prefix the string with 'dot'
    if input_string.startswith('.'):
        input_string = 'dot' + input_string[1:]

    # Initialize variables for further processing
    count_at = 0
    updated_characters = []  # List to hold updated characters

    # Check for leading '@' character and prefix with 'at' if present
    if input_string.startswith('@'):
        input_string = 'at' + input_string[1:]

    # Iterate through each character in the input string
    for character in input_string:
        if character == '@':
            # Check if we have already appended one '@'
            if count_at > 0:
                updated_characters.append('at')
                count_at = 1  # Update to indicate we've seen an '@' 
            else:
                updated_characters.append('@')
                count_at = 1  # Update to note we've added an '@' already
        else:
            updated_characters.append(character)

    # Combine the updated character list back into a string
    final_string = ''.join(updated_characters)

    # If the final string ends with a dot, replace it with 'dot'
    if final_string.endswith('.'):
        final_string = final_string[:-1] + 'dot'

    # Print the final processed string
    print(final_string)

# Allow execution when script is run
if __name__ == "__main__":
    process_input()
