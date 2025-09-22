def ConvertInputToBinaryString():
    inputString = input()
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

    print(resultString)

# Testing the function with various input scenarios
if __name__ == "__main__":
    ConvertInputToBinaryString()
