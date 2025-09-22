def translateInputToOutput():
    # Read input from standard input and remove any trailing whitespace
    stringInput = input().strip()
    
    # Initialize an index to track position in the input string
    index = 0
    # Initialize an empty string to hold the output result
    outputResult = ''
    
    # While index is within the bounds of the input string
    while index < len(stringInput):
        # If the current character is a dot
        if stringInput[index] == '.':
            # Append '0' to the output result
            outputResult += '0'
            # Move to the next character
            index += 1
        # Else if the next character is also a dot
        elif index + 1 < len(stringInput) and stringInput[index + 1] == '.':
            # Append '1' to the output result
            outputResult += '1'
            # Move to the character after the next
            index += 2
        # Otherwise, the next two characters are different from dots
        else:
            # Append '2' to the output result
            outputResult += '2'
            # Move to the character after the next
            index += 2

    # Output the constructed result string
    print(outputResult)
