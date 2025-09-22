def decodeInput():
    # Read input data from the standard input and strip any extra whitespace
    inputString = input().strip()
    index = 0
    resultString = ""

    # Process the input string until the end is reached
    while index < len(inputString):
        if inputString[index] == '.':
            # If the current character is a '.', append '0' to result
            resultString += '0'
            index += 1
        elif index + 1 < len(inputString) and inputString[index + 1] == '.':
            # If the next character is also '.', append '1' to result
            resultString += '1'
            index += 2
        else:
            # Otherwise, append '2' to result
            resultString += '2'
            index += 2

    # Output the resulting string
    print(resultString)

# Testing cases can be run here to verify functionality.
