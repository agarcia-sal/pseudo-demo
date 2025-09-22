def processEmailAddress():
    # Read the input string from standard input and strip whitespace
    inputString = input().strip()

    # Replace occurrences of keywords with corresponding symbols
    inputString = inputString.replace('dot', '.')
    inputString = inputString.replace('at', '@')

    # Check if the string starts with a dot and modify accordingly
    if inputString.startswith('.'):
        inputString = 'dot' + inputString[1:]

    # Initialize a counter and a container for characters
    counter = 0
    characters = []

    # Check if the string starts with '@' and modify accordingly
    if inputString.startswith('@'):
        inputString = 'at' + inputString[1:]

    # Iterate through each character in the inputString
    for character in inputString:
        if character == '@':
            # If we've already added an '@' before, add 'at' instead
            if counter > 0:
                characters.append('at')
                counter = 1
            else:
                characters.append('@')
                counter = 1
        else:
            characters.append(character)

    # Join the characters back into a single string
    outputString = ''.join(characters)

    # If the last character is a '.', replace it with 'dot'
    if outputString.endswith('.'):
        outputString = outputString[:-1] + 'dot'

    # Output the final processed string
    print(outputString)

# Note: Testing can include various inputs such as:
# processEmailAddress() should handle cases like:
# "exampledotcom" -> "example.com"
# "exampleatgmaildotcom" -> "example@gmail.com"
# ".example.com" -> "dotexample.com"
# "@example.com" -> "atexample.com"
# "user@@example.com" -> "user@atexample.com"
# "@@example" -> "atatexample"
