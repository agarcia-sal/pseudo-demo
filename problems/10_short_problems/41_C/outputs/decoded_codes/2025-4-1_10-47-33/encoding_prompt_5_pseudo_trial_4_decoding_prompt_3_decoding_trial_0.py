def process_email_string():
    # Read input from the user and remove leading/trailing spaces
    input_string = input().strip()

    # Replace specific words with symbols
    input_string = input_string.replace("dot", ".").replace("at", "@")

    # If the string starts with a period, prepend "dot" to the remaining string
    if input_string.startswith('.'):
        input_string = 'dot' + input_string[1:]

    # Initialize variables for tracking and modification
    count_at_symbol = 0
    modified_characters = []
    
    # If the string starts with "@", prepend "at" to the remaining string
    if input_string.startswith('@'):
        input_string = 'at' + input_string[1:]

    # Loop through each character in the modified input string
    for character in input_string:
        # Check if the character is the "at" symbol
        if character == '@':
            if count_at_symbol > 0:
                modified_characters.append("at")
                count_at_symbol = 1  # Reset count
            else:
                modified_characters.append('@')
                count_at_symbol = 1  # Update count
        else:
            # If character is not "at", append it to the list
            modified_characters.append(character)

    # Join the modified characters into a single string
    final_string = ''.join(modified_characters)

    # If the final string ends with a period, replace it with "dot"
    if final_string.endswith('.'):
        final_string = final_string[:-1] + "dot"

    # Output the final processed string
    print(final_string)

# Call the function to execute the process
process_email_string()
