def process_email_string():
    # Read input from the user
    input_string = input().strip()  # Remove unnecessary spaces from the beginning and end

    # Replace occurrences of 'dot' with '.' and 'at' with '@'
    input_string = input_string.replace('dot', '.').replace('at', '@')

    # If the first character is a period, prefix the string with 'dot'
    if input_string.startswith('.'):
        input_string = 'dot' + input_string[1:]

    # Initialize a counter and an empty list to hold processed characters
    counter = 0
    processed_list = []

    # If the first character is '@', prefix the string with 'at'
    if input_string.startswith('@'):
        input_string = 'at' + input_string[1:]

    # Iterate through each character in the modified input string
    for character in input_string:
        # Check if the character is '@'
        if character == '@':
            # If '@' has been encountered before, append 'at' to the list
            if counter > 0:
                processed_list.append('at')
                counter = 1  # Update counter to indicate that '@' has been encountered
            else:
                # Otherwise, append '@' to the list
                processed_list.append('@')
                counter = 1  # Update counter
        else:
            # For any other character, simply append it to the list
            processed_list.append(character)

    # Join the processed characters back into a single string
    final_string = ''.join(processed_list)

    # If the last character is a period, replace it with 'dot'
    if final_string.endswith('.'):
        final_string = final_string[:-1] + 'dot'

    # Output the final string
    print(final_string)

# Call the function to process the email string
process_email_string()
