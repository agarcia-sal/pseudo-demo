def process_email_string():
    # Read input from the user
    inputString = input().strip()

    # Replace specific words with symbols
    inputString = inputString.replace("dot", ".")
    inputString = inputString.replace("at", "@")

    # If the string starts with a period, prepend "dot"
    if inputString.startswith('.'):
        inputString = "dot" + inputString[1:]

    # Initialize variables for tracking and modification
    countAtSymbol = 0
    modifiedCharacters = []
    
    # If the string starts with "@", prepend "at"
    if inputString.startswith('@'):
        inputString = "at" + inputString[1:]

    # Loop through each character in the modified input string
    for character in inputString:
        # Check if the character is the "at" symbol
        if character == '@':
            # If an "at" symbol has been added before
            if countAtSymbol > 0:
                modifiedCharacters.append("at")
                countAtSymbol = 1  # Reset count
            else:
                modifiedCharacters.append("@")
                countAtSymbol = 1  # Update count
        else:
            # If character is not "at", append it to the list
            modifiedCharacters.append(character)

    # Join the modified characters into a single string
    finalString = ''.join(modifiedCharacters)

    # If the final string ends with a period, replace it with "dot"
    if finalString.endswith('.'):
        finalString = finalString[:-1] + "dot"

    # Output the final processed string
    print(finalString)

# Call the function to execute
process_email_string()
