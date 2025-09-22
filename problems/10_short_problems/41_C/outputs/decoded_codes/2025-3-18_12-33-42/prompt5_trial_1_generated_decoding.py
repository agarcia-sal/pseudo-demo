def transform_input_string():
    # Read input from the user
    string_input = input().strip()  # Remove leading and trailing spaces

    # Replace 'dot' with '.' and 'at' with '@'
    string_input = string_input.replace('dot', '.').replace('at', '@')

    # Check if the string starts with a dot
    if string_input.startswith('.'):
        string_input = 'dot' + string_input[1:]  # Prefix 'dot' to the string (excluding first character)

    # Initialize a counter and a list for the transformed characters
    counter = 0
    transformed_characters = []

    # Check if the string starts with '@'
    if string_input.startswith('@'):
        string_input = 'at' + string_input[1:]  # Prefix 'at' to the string (excluding first character)

    # Iterate through each character in the modified string
    for character in string_input:
        # If the character is '@'
        if character == '@':
            # Check if '@' has already been added
            if counter > 0:
                # If so, add 'at' to the transformed list
                transformed_characters.append('at')
                counter = 1
            else:
                # Otherwise, simply add '@'
                transformed_characters.append('@')
                counter = 1
        else:
            # If the character is not '@', simply add it
            transformed_characters.append(character)

    # Join the list of transformed characters back into a single string
    final_string = ''.join(transformed_characters)

    # Check if the final string ends with a dot
    if final_string.endswith('.'):
        # If so, replace the last character with 'dot'
        final_string = final_string[:-1] + 'dot'

    # Output the final transformed string
    print(final_string)

# You can call the function to test the transformation
# transform_input_string()
