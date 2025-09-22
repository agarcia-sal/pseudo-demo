def format_email_string():
    # Step 1: Read Input
    email_string = input().strip()

    # Step 2: Replace Keywords
    email_string = email_string.replace("dot", ".").replace("at", "@")

    # Step 3: Handle Leading Period
    if email_string.startswith('.'):
        email_string = "dot" + email_string[1:]

    # Step 4: Check for Leading At Symbol
    if email_string.startswith('@'):
        email_string = "at" + email_string[1:]

    # Step 5: Prepare for Conversion
    counter = 0
    formatted_characters = []

    # Step 6: Process Each Character
    for character in email_string:
        if character == '@':
            if counter > 0:
                formatted_characters.append("at")
                counter = 1
            else:
                formatted_characters.append("@")
                counter = 1
        else:
            formatted_characters.append(character)

    # Step 7: Join Characters into a String
    final_string = ''.join(formatted_characters)

    # Step 8: Handle Trailing Period
    if final_string.endswith('.'):
        final_string = final_string[:-1] + "dot"

    # Step 9: Output the Result
    print(final_string)

# Uncomment below to run the function
# format_email_string()
