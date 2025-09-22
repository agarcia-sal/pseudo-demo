def processInput():
    # Read input from standard input
    inputString = input().strip()
    
    # Replace occurrences of 'dot' with '.' and 'at' with '@'
    inputString = inputString.replace('dot', '.')
    inputString = inputString.replace('at', '@')
    
    # If the first character is a dot, prefix the string with 'dot'
    if inputString.startswith('.'):
        inputString = 'dot' + inputString[1:]
    
    # Initialize variables for further processing
    countAt = 0
    updatedCharacters = []
    
    # Check for leading '@' character and prefix with 'at' if present
    if inputString.startswith('@'):
        inputString = 'at' + inputString[1:]
        
    # Iterate through each character in the input string
    for character in inputString:
        if character == '@':
            # Check if we have already appended one '@'
            if countAt > 0:
                updatedCharacters.append('at')
                countAt = 1  # Update to indicate we've seen an '@'
            else:
                updatedCharacters.append('@')
                countAt = 1  # Update to note we've added an '@' already
        else:
            updatedCharacters.append(character)
    
    # Combine the updated character list back into a string
    finalString = ''.join(updatedCharacters)
    
    # If the final string ends with a dot, replace it with 'dot'
    if finalString.endswith('.'):
        finalString = finalString[:-1] + 'dot'
    
    # Print the final processed string
    print(finalString)

# Example test cases
if __name__ == "__main__":
    processInput()
