def processInputAddress():
    inputAddress = input().strip()
    
    # Replace specific words with symbols
    inputAddress = inputAddress.replace('dot', '.')
    inputAddress = inputAddress.replace('at', '@')

    # Ensure the address starts with a valid prefix if it begins with a dot
    if inputAddress.startswith('.'):
        inputAddress = 'dot' + inputAddress[1:]

    occurrenceCounter = 0
    outputList = []

    # Process the input address
    if inputAddress.startswith('@'):
        outputList.append('at')
        outputList.append(inputAddress[1:])
    else:
        outputList.append(inputAddress)

    # Loop through each character in the processed input address
    for character in ''.join(outputList):
        if character == '@':
            if occurrenceCounter > 0:
                outputList.append('at')
                occurrenceCounter = 1
            else:
                outputList.append('@')
                occurrenceCounter = 1
        else:
            outputList.append(character)
    
    # Join the list of characters into a single string
    finalAddress = ''.join(outputList)

    # If the final character of the address is '.', replace it with 'dot'
    if finalAddress.endswith('.'):
        finalAddress = finalAddress[:-1] + 'dot'

    # Output the final processed address
    print(finalAddress)
