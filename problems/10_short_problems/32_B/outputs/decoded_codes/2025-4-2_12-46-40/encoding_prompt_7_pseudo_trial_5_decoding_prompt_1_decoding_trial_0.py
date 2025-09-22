def ConvertInputToBinaryString():
    inputString = input()  # Read input as a string
    index = 0              # Initialize index as 0
    resultString = ""      # Initialize resultString as an empty string

    while index < len(inputString):  # Iterate while index is less than the length of inputString
        if inputString[index] == '.':  # Check if the character at inputString[index] is '.'
            resultString += '0'         # Append '0' to resultString
            index += 1                  # Increment index by 1
        elif (index + 1) < len(inputString) and inputString[index + 1] == '.':  # Check if next character is '.'
            resultString += '1'          # Append '1' to resultString
            index += 2                   # Increment index by 2
        else:                           # For the case when current character is not '.' and next is not '.'
            resultString += '2'          # Append '2' to resultString
            index += 2                   # Increment index by 2

    print(resultString)  # Print the final resultString
