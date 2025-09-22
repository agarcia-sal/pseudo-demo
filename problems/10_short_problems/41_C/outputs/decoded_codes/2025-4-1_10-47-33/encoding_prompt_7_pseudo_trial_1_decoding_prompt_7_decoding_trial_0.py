def convertInputToEmailFormat():
    # Read a line of input and remove leading and trailing whitespace
    inputString = input().strip()
    
    # Replace occurrences of "dot" with "." in inputString
    inputString = inputString.replace("dot", ".")
    # Replace occurrences of "at" with "@" in inputString
    inputString = inputString.replace("at", "@")
    
    # If the first character is a dot, prepend "dot" to the string
    if inputString.startswith('.'):
        inputString = "dot" + inputString[1:]
    
    counter = 0  # Counter to track occurrences of '@'
    conversionList = []  # List to hold characters for final conversion
    length = 0  # Variable to hold length, though not used in this case

    # If the first character is an at symbol, prepend "at" to the string
    if inputString.startswith('@'):
        inputString = "at" + inputString[1:]

    # Iterate through each character in the modified inputString
    for character in inputString:
        if character == '@':
            # Check if an '@' was already added
            if counter > 0:
                conversionList.append("at")  # Add "at" if we already added an '@'
                counter = 1  # Track that we've added an '@'
            else:
                conversionList.append("@")  # Just add '@' for the first occurrence
                counter = 1  # Track the first '@'
        else:
            conversionList.append(character)  # Append regular characters

    # Join the list into a single string
    convertedString = ''.join(conversionList)

    # If the last character of the converted string is a dot, replace it with "dot"
    if convertedString.endswith('.'):
        convertedString = convertedString[:-1] + "dot"  # Replace last '.' with 'dot'

    # Output the final converted string
    print(convertedString)

# Example of testing the function
if __name__ == "__main__":
    convertInputToEmailFormat()
