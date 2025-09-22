def process_email_input():
    # Read a line of input and remove leading/trailing whitespace
    email_string = input().strip()

    # Replace occurrences of 'dot' with '.' and 'at' with '@'
    email_string = email_string.replace('dot', '.')
    email_string = email_string.replace('at', '@')

    # Check if the email string starts with a '.', prepend 'dot' to it
    if email_string.startswith('.'):
        email_string = 'dot' + email_string[1:]

    co_count = 0  # Counter for '@' occurrences
    modified_characters = []  # List to hold the modified characters

    # Check if the email string starts with an '@', prepend 'at' to it
    if email_string.startswith('@'):
        email_string = 'at' + email_string[1:]

    # Iterate through each character in the email string
    for character in email_string:
        # Check if the character is '@'
        if character == '@':
            if co_count > 0:
                modified_characters.append('at')  # Avoid consecutive '@'
                co_count = 1  # Set counter to indicate we've added an '@'
            else:
                modified_characters.append('@')  # Add first '@'
                co_count = 1  # Set counter to indicate we've added an '@'
        else:
            # Add the character as it is
            modified_characters.append(character)

    # Join the modified characters into a single string
    modified_email_string = ''.join(modified_characters)

    # If the modified email string ends with a '.', replace it with 'dot'
    if modified_email_string.endswith('.'):
        modified_email_string = modified_email_string[:-1] + 'dot'

    # Output the final modified email string
    print(modified_email_string)

# Testing the function with various cases
if __name__ == "__main__":
    # Example test cases
    process_email_input()  # Input cases can be provided during execution    
