def ConvertInputToBinaryString():
    inputString = input()  # Read input from standard input
    index = 0  # Initialize index
    resultString = ""  # Initialize result string

    while index < len(inputString):  # Loop until the end of the input string
        if inputString[index] == '.':  # Check if the current character is '.'
            resultString += '0'  # Append '0' to resultString
            index += 1  # Increment index by 1
        elif index + 1 < len(inputString) and inputString[index + 1] == '.':  # Check next character is '.'
            resultString += '1'  # Append '1' to resultString
            index += 2  # Increment index by 2
        else:  # If it's neither case
            resultString += '2'  # Append '2' to resultString
            index += 2  # Increment index by 2

    print(resultString)  # Output the result string
