def transform_email_format():
    # Read input from the user
    user_input = input()
    
    # Remove leading and trailing whitespace from the input
    user_input = user_input.strip()
    
    # Replace occurrences of 'dot' with '.' and 'at' with '@'
    user_input = user_input.replace("dot", ".")
    user_input = user_input.replace("at", "@")
    
    # If the first character is a '.', prepend 'dot' to the string
    if user_input.startswith('.'):
        user_input = 'dot' + user_input[1:]
    
    # Initialize a counter and a list to hold modified characters
    counter = 0
    modified_characters = []

    # Check if the first character is '@' and if so, prepend 'at'
    if user_input.startswith('@'):
        user_input = 'at' + user_input[1:]

    # Iterate through each character in the modified user_input
    for character in user_input:
        if character == '@':
            # If '@' is found and counter is greater than 0, add 'at' to the list
            if counter > 0:
                modified_characters.append("at")
                counter = 1
            else:
                # If this is the first '@', add it directly to the list
                modified_characters.append('@')
                counter = 1
        else:
            # Add the current character to the list
            modified_characters.append(character)

    # Join all characters in modified_characters into a single string
    modified_string = ''.join(modified_characters)

    # If the last character of the modified string is '.', replace it with 'dot'
    if modified_string.endswith('.'):
        modified_string = modified_string[:-1] + "dot"

    # Output the final transformed string
    print(modified_string)

