def transformInputString(inputString):
    # Step 1: Read the input and perform initial replacements
    processedString = inputString.replace('dot', '.').replace('at', '@')
    
    # Step 2: Ensure the string starts correctly
    if processedString and processedString[0] == '.':
        processedString = 'dot' + processedString
    
    # Step 3: Initialize variables for processing
    countAtSymbols = 0
    transformedCharacters = []
    
    # Step 4: Check for initial '@' and adjust if necessary
    if processedString and processedString[0] == '@':
        processedString = 'at' + processedString

    # Step 5: Process each character in the string
    for character in processedString:
        if character == '@':
            if countAtSymbols > 0:
                transformedCharacters.append('at')
                countAtSymbols = 1 
            else:
                transformedCharacters.append('@')
                countAtSymbols = 1
        else:
            transformedCharacters.append(character)
    
    # Step 6: Combine transformed characters into a single string
    finalString = ''.join(transformedCharacters)
    
    # Step 7: Adjust the ending of the final string if necessary
    if finalString and finalString[-1] == '.':
        finalString = finalString[:-1] + 'dot'
    
    # Step 8: Return the transformed string
    return finalString

# Main execution starts here
input_str = input()
result = transformInputString(input_str)
print(result)
