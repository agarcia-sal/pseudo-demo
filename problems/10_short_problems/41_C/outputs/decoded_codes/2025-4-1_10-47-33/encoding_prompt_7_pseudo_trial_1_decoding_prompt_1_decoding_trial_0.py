def convertInputToEmailFormat():
    # Read a line of input and remove leading and trailing whitespace
    inputString = input().strip()
    
    # Replace occurrences of "dot" with "." and "at" with "@" in inputString
    inputString = inputString.replace("dot", ".").replace("at", "@")
    
    # If the first character is a dot, prepend "dot" to the string
    if inputString.startswith('.'):
        inputString = "dot" + inputString[1:]
        
    counter = 0
    conversionList = []
    
    # If the first character is an at symbol, prepend "at" to the string
    if inputString.startswith('@'):
        inputString = "at" + inputString[1:]
        
    # Iterate through each character in the modified inputString
    for character in inputString:
        if character == '@':
            # Check if an '@' was already added
            if counter > 0:
                conversionList.append("at")  # Append "at" if an '@' was already added
                counter = 1  # Track that we've added an '@'
            else:
                conversionList.append("@")
                counter = 1
        else:
            conversionList.append(character)
    
    # Join the list into a single string
    convertedString = ''.join(conversionList)
    
    # If the last character of the converted string is a dot, replace it with "dot"
    if convertedString.endswith('.'):
        convertedString = convertedString[:-1] + "dot"
    
    # Output the final converted string
    print(convertedString)

