def processEmailAddress():
    # Read input string and remove leading/trailing whitespace
    inputString = input().strip()
    
    # Replace occurrences of 'dot' with '.' and 'at' with '@'
    inputString = inputString.replace('dot', '.')
    inputString = inputString.replace('at', '@')
    
    # Ensure the email format starts correctly
    if inputString and inputString[0] == '.':
        inputString = 'dot' + inputString[1:]

    # Initialize counter and list for processed characters
    counter = 0
    resultCharacters = []
    
    # Check if the email string starts with '@'
    if inputString and inputString[0] == '@':
        inputString = 'at' + inputString[1:]

    # Iterate through each character in the modified inputString
    for character in inputString:
        if character == '@':
            # If we have seen an '@' before, append 'at' to the result list
            if counter > 0:
                resultCharacters.append('at')
                counter = 1  # Reset counter for the next '@'
            else:
                resultCharacters.append('@')
                counter = 1  # Set counter indicating we've now seen an '@'
        else:
            # Append the current character to the result list
            resultCharacters.append(character)
    
    # Join the processed characters into a single string
    outputString = ''.join(resultCharacters)
    
    # If the output string ends with '.', replace it with 'dot'
    if outputString and outputString[-1] == '.':
        outputString = outputString[:-1] + 'dot'
    
    # Print the final processed email address
    print(outputString)

# Example usage (uncomment to test):
# processEmailAddress()
