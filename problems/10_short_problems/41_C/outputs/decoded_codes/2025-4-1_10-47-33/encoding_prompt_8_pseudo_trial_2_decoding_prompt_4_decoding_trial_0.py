def format_email_string():
    # Step 1: Read input
    emailString = input().strip()
    
    # Step 2: Replace keywords
    emailString = emailString.replace("dot", ".").replace("at", "@")
    
    # Step 3: Handle leading period
    if emailString.startswith('.'):
        emailString = "dot" + emailString[1:]
    
    # Step 4: Check for leading at symbol
    if emailString.startswith('@'):
        emailString = "at" + emailString[1:]
    
    # Step 5: Prepare for conversion
    counter = 0
    formattedCharacters = []
    
    # Step 6: Process each character
    for character in emailString:
        if character == '@':
            if counter > 0:
                formattedCharacters.append("at")
                counter = 1
            else:
                formattedCharacters.append("@")
                counter = 1
        else:
            formattedCharacters.append(character)
    
    # Step 7: Join characters into a string
    finalString = ''.join(formattedCharacters)
    
    # Step 8: Handle trailing period
    if finalString.endswith('.'):
        finalString = finalString[:-1] + "dot"
    
    # Step 9: Output the result
    print(finalString)

# Call the function to execute
format_email_string()
