def transform_input():
    # Read a line of input and remove any surrounding whitespace
    inputLine = input().strip()
    
    # Replace occurrences of 'dot' with '.' and 'at' with '@'
    inputLine = inputLine.replace('dot', '.').replace('at', '@')
    
    # If the modified input starts with a '.', prepend 'dot' to it
    if inputLine.startswith('.'):
        inputLine = 'dot' + inputLine
    
    # Initialize a count for consecutive '@' symbols and an empty list for characters
    consecutiveAtCount = 0
    outputCharacters = []
    
    # If the modified input starts with '@', prepend 'at' to it
    if inputLine.startswith('@'):
        inputLine = 'at' + inputLine
    
    # Iterate through each character in the modified input
    for character in inputLine:
        
        # Check if the character is '@'
        if character == '@':
            # Append 'at' for the second consecutive '@' and reset count
            if consecutiveAtCount > 0:
                outputCharacters.append('at')
                consecutiveAtCount = 1  # Count this as the second '@'
            else:
                outputCharacters.append('@')
                consecutiveAtCount = 1  # Count the first '@'
        else:
            # If it is not '@', append the character to the output list
            outputCharacters.append(character)
            consecutiveAtCount = 0  # Reset the count for other characters
    
    # Join all characters in the outputCharacters list into a string
    modifiedText = ''.join(outputCharacters)
    
    # If the last character in the modified text is '.', replace it with 'dot'
    if modifiedText.endswith('.'):
        modifiedText = modifiedText[:-1] + 'dot'
    
    # Print the final modified text
    print(modifiedText)

# Call the function to execute the transformation
transform_input()
