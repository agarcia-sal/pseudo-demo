def process_input():
    # Read input from standard input
    raw_input = input().strip()  # Remove whitespace from the beginning and end of the input
    modified_input = raw_input.replace('dot', '.').replace('at', '@')  # Replace 'dot' with '.' and 'at' with '@'

    # Handle case where input starts with a dot
    if modified_input.startswith('.'):
        modified_input = 'dot' + modified_input[1:]

    # Initialize counter and list to store characters
    at_counter = 0
    character_list = []

    # Handle case where input starts with an at symbol
    if modified_input.startswith('@'):
        modified_input = 'at' + modified_input[1:]

    # Iterate over each character in the modified input
    for char in modified_input:
        if char == '@':
            # Check if we've seen an '@' before and update the list accordingly
            if at_counter > 0:
                character_list.append('at')
            else:
                character_list.append('@')
            at_counter = 1  # Set the counter indicating we've seen an '@'
        else:
            # Append the character to the list
            character_list.append(char)

    # Join list into a single string
    final_string = ''.join(character_list)

    # Check if the last character is a dot and handle it
    if final_string.endswith('.'):
        final_string = final_string[:-1] + 'dot'

    # Output the final result
    print(final_string)

# Call the function to execute the program
process_input()
