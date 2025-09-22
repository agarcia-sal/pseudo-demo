def translateSymbolString(inputString):
    index = 0
    resultString = ""

    while index < len(inputString):
        if inputString[index] == '.':
            resultString += '0'
            index += 1
        elif index + 1 < len(inputString) and inputString[index + 1] == '.':
            resultString += '1'
            index += 2
        else:
            resultString += '2'
            index += 2

    return resultString

# Read input from the standard input stream
input_string = input()

# Call the translate function and print the result
result = translateSymbolString(input_string)
print(result)
