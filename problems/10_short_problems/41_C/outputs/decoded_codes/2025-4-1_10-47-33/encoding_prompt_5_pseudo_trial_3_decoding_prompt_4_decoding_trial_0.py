def process_email_string():
    # Read input from the user
    input_string = input().strip()

    # Replace occurrences of 'dot' with '.' and 'at' with '@'
    input_string = input_string.replace('dot', '.').replace('at', '@')

    # If the first character is a '.', prefix with 'dot'
    if input_string.startswith('.'):
        input_string = 'dot' + input_string[1:]

    # Initialize a counter and an empty list to hold processed characters
    counter = 0
    processed_list = []

    # If the first character is '@', prefix with 'at'
    if input_string.startswith('@'):
        input_string = 'at' + input_string[1:]

    # Iterate through each character in the modified input string
    for character in input_string:
        if character == '@':
            # Handle multiple '@' characters
            if counter > 0:
                processed_list.append('at')
            processed_list.append('@')
            counter += 1
        else:
            processed_list.append(character)

    # Join the processed characters back into a single string
    final_string = ''.join(processed_list)

    # If the last character is a '.', replace with 'dot'
    if final_string.endswith('.'):
        final_string = final_string[:-1] + 'dot'

    # Output the final string
    print(final_string)

# Run the function to process the email string
process_email_string()
