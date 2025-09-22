def processInputAddress():
    # Read input string from standard input and trim leading/trailing whitespace
    inputAddress = input().strip()

    # Replace occurrences of specific words with symbols
    inputAddress = inputAddress.replace('dot', '.')
    inputAddress = inputAddress.replace('at', '@')

    # Ensure the address starts with a valid prefix if it begins with a dot
    if inputAddress.startswith('.'):
        inputAddress = 'dot' + inputAddress[1:]  # Exclude the leading dot

    # Initialize a counter for occurrences of '@' and a list for building the output
    occurrenceCounter = 0
    outputList = []

    # Process the input address
    # If the address starts with '@', prefix it with 'at'
    if inputAddress.startswith('@'):
        outputList.append('at')  # Add 'at' to output list
        occurrenceCounter += 1

    # Loop through each character in the processed input address
    for character in inputAddress:  
        if character == '@':
            # Check if '@' has already occurred
            if occurrenceCounter > 0:
                outputList.append('at')  # Append 'at' instead of another '@'
            else:
                outputList.append('@')  # Append the first '@'
            occurrenceCounter += 1  # Increase the count of occurrences
        else:
            outputList.append(character)  # Append the current character

    # Join the list of characters into a single string
    finalAddress = ''.join(outputList)

    # If the final character of the address is '.', replace it with 'dot'
    if finalAddress.endswith('.'):
        finalAddress = finalAddress[:-1] + 'dot'  # Replace last character with 'dot'

    # Output the final processed address
    print(finalAddress)

# Example of calling the function (uncomment the line below to test interactively)
# processInputAddress()
