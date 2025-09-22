def processInputEmail():
    # Read input from the user
    emailString = input()
    
    # Clean up the email string by replacing specific words with symbols
    emailString = emailString.replace('dot', '.')
    emailString = emailString.replace('at', '@')
    
    # Ensure the email starts with 'dot' if it begins with a '.'
    if emailString.startswith('.'):
        emailString = 'dot' + emailString
        
    countOfAtSymbols = 0
    resultList = []
    
    # Ensure the email starts with 'at' if it begins with an '@'
    if emailString.startswith('@'):
        emailString = 'at' + emailString

    # Process each character in the email string
    for character in emailString:
        if character == '@':
            if countOfAtSymbols > 0:
                resultList.append('at')
            else:
                resultList.append('@')
                countOfAtSymbols += 1
        else:
            resultList.append(character)
    
    # Join all elements in resultList into a single string
    cleanedEmailString = ''.join(resultList)
    
    # Replace the last character with 'dot' if it is a '.'
    if cleanedEmailString.endswith('.'):
        cleanedEmailString = cleanedEmailString[:-1] + 'dot'
    
    # Output the final cleaned email string
    print(cleanedEmailString)

# For testing purposes, you can call the function to see the output.
processInputEmail()
