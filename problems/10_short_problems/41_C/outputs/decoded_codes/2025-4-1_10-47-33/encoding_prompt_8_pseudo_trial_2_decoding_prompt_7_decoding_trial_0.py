# Main function to format an email-like string
def format_email_string():
    # Step 1: Read input from user and remove surrounding whitespace
    emailString = input().strip()

    # Step 2: Replace keywords "dot" with "." and "at" with "@"
    emailString = emailString.replace("dot", ".").replace("at", "@")

    # Step 3: Handle leading period
    if emailString.startswith('.'):
        emailString = "dot" + emailString[1:]

    # Step 4: Check for leading at symbol
    if emailString.startswith('@'):
        emailString = "at" + emailString[1:]

    # Step 5: Prepare for conversion
    counter = 0  # Counter for handling multiple "at" occurrences
    formattedCharacters = []  # List to store the processed characters

    # Step 6: Process each character in emailString
    for character in emailString:
        if character == '@':
            if counter > 0:
                # If the previous character was also "@", replace with "at"
                formattedCharacters.append("at")
            else:
                # First occurrence of "@"
                formattedCharacters.append("@")
            counter = 1  # Set counter to indicate we've added an "@"
        else:
            # Append non-"@" characters
            formattedCharacters.append(character)
            counter = 0  # Reset counter as we have a non-"@" character

    # Step 7: Join characters into a single string
    finalString = ''.join(formattedCharacters)

    # Step 8: Handle trailing period
    if finalString.endswith('.'):
        finalString = finalString[:-1] + "dot"

    # Step 9: Output the result
    print(finalString)

# Call the function to execute the formatting
format_email_string()
