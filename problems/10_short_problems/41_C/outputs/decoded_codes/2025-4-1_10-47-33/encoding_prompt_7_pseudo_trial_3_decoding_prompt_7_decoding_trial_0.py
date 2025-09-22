def processEmailFormat(inputString):
    # Step 1: Read the input string and remove any extra spaces
    emailString = inputString.strip()
    
    # Step 2: Replace occurrences of 'dot' with '.' and 'at' with '@'
    emailString = emailString.replace('dot', '.')
    emailString = emailString.replace('at', '@')
    
    # Step 3: Check if the email starts with a dot and prepend 'dot' if true
    if emailString and emailString[0] == '.':
        emailString = 'dot' + emailString[1:]
    
    # Step 4: Initialize a counter and an empty list to construct the final email format
    counter = 0
    formattedEmailList = []
    
    # Step 5: Check if the email starts with '@' and prepend 'at' if true
    if emailString and emailString[0] == '@':
        emailString = 'at' + emailString[1:]

    # Step 6: Iterate over each character in the email string
    for character in emailString:
        # Step 7: If the character is '@', handle it according to the count
        if character == '@':
            if counter > 0:
                # Add 'at' if multiple '@' symbols are encountered
                formattedEmailList.append('at')
                counter = 1
            else:
                # Add single '@' to the list
                formattedEmailList.append('@')
                counter = 1
        else:
            # Step 8: If the character is not '@', add it to the list
            formattedEmailList.append(character)
    
    # Step 9: Join the list into a single string
    finalEmailString = ''.join(formattedEmailList)
    
    # Step 10: Check if the last character is '.', and replace it with 'dot'
    if finalEmailString and finalEmailString[-1] == '.':
        finalEmailString = finalEmailString[:-1] + 'dot'
    
    # Step 11: Output the final formatted email string
    return finalEmailString

# The function expects a string input to be processed as a valid email format
