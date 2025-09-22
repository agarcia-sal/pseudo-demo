def processInputEmail():
    # Read input from standard input
    inputString = input()
    
    # Remove unnecessary whitespace from inputString
    inputString = inputString.strip()
    
    # Replace occurrences of 'dot' with '.' in inputString
    inputString = inputString.replace('dot', '.')
    # Replace occurrences of 'at' with '@' in inputString
    inputString = inputString.replace('at', '@')
    
    # Check if the first character is '.' and modify if necessary
    if inputString and inputString[0] == '.':
        inputString = 'dot' + inputString[1:]

    counter = 0  # Initialize counter for @ occurrences
    outputCharacters = []  # List to build the final output
    length = len(inputString)

    # Check if the first character is '@' and modify if necessary
    if inputString and inputString[0] == '@':
        outputCharacters.append('at')  # Prepend 'at' to outputCharacters
        counter = 1  # Update counter

    # Iterate through each character in the input string
    for character in inputString:
        if character == '@':
            if counter > 0:
                outputCharacters.append('at')
                counter = 1  # Update counter
            else:
                outputCharacters.append('@')
                counter = 1  # Set counter to indicate we found an '@'
        else:
            outputCharacters.append(character)  # Append character as is

    # Combine characters into a single string
    finalString = ''.join(outputCharacters)

    # Check if the last character is '.', modify if necessary
    if finalString and finalString[-1] == '.':
        finalString = finalString[:-1] + 'dot'  # Remove last '.' and append 'dot'

    # Output the final processed string
    print(finalString)

# Optional: test the function with various cases
if __name__ == "__main__":
    processInputEmail()
