def format_email_string():
    # Read input from the standard input and remove trailing spaces
    input_string = input().strip()
    original_string = input_string

    # Replace occurrences of specific text patterns
    original_string = original_string.replace('dot', '.')
    original_string = original_string.replace('at', '@')

    # Ensure proper formatting by prepending 'dot' if the string starts with a dot
    if original_string.startswith('.'):
        original_string = 'dot' + original_string

    # Initialize variables for email formatting
    previous_char = 0    # Track the last occurrence of '@'
    formatted_characters = []  # To store the final characters
    length_to_last_char = 0     # To hold the length of the formatted string

    # Check if the string starts with an '@'
    if original_string.startswith('@'):
        original_string = 'at' + original_string

    # Iterate through each character in the modified string
    for character in original_string:
        # Handling '@' character explicitly
        if character == '@':
            if previous_char > 0:
                # Add 'at' instead of repeated '@'
                formatted_characters.append('at')
            else:
                formatted_characters.append('@')  # Add the '@'
            previous_char = 1  # Mark that '@' was found
        else:
            # Add regular characters to the formatted list
            formatted_characters.append(character)
            previous_char = 0  # Reset because we added a non '@' character

    # Join the formatted characters into a single string
    final_string = ''.join(formatted_characters)

    # Remove the last character if it is a '.' and append 'dot' instead
    if final_string.endswith('.'):
        final_string = final_string[:-1] + 'dot'

    # Print the final formatted string
    print(final_string)

# Call the function to execute
format_email_string()
