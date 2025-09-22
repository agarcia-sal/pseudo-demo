def processInputAddress():
    # Read input string from standard input and remove leading/trailing whitespace
    inputAddress = input().strip()

    # Replace occurrences of specific words with symbols
    inputAddress = inputAddress.replace('dot', '.')
    inputAddress = inputAddress.replace('at', '@')

    # Ensure the address starts with a valid prefix if it begins with a dot
    if inputAddress.startswith('.'):
        inputAddress = 'dot' + inputAddress[1:]

    # Initialize a counter for occurrences of '@' and a list for building the output
    occurrenceCounter = 0
    outputList = []

    # Process the input address
    # If the address starts with '@', prefix it with 'at'
    if inputAddress.startswith('@'):
        inputAddress = 'at' + inputAddress[1:]

    # Loop through each character in the processed input address
    for character in inputAddress:
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

# Function call (optional)
# processInputAddress()
