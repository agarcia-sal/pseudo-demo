# Begin

# Read a line of input and remove leading and trailing spaces
stringInput = input().strip()

# Replace occurrences of 'dot' with '.' and 'at' with '@'
stringInput = stringInput.replace('dot', '.').replace('at', '@')

# If the first character is a dot, prepend 'dot' to the string
if stringInput and stringInput[0] == '.':
    stringInput = 'dot' + stringInput[1:]

# Initialize a counter and an empty list for building the output
countAtSymbols = 0
resultList = []

# Check if first character is '@', if so, prepend 'at' to the string
if stringInput and stringInput[0] == '@':
    stringInput = 'at' + stringInput[1:]

# Iterate through each character in the modified string
for character in stringInput:
    if character == '@':
        # If '@' has been seen before, replace it with 'at', else keep '@'
        if countAtSymbols > 0:
            resultList.append('at')
        else:
            resultList.append('@')
            countAtSymbols = 1
    else:
        # For any other character, append it to the result list
        resultList.append(character)

# Join the list of characters into a single string
outputString = ''.join(resultList)

# If the last character is a dot, replace it with 'dot'
if outputString and outputString[-1] == '.':
    outputString = outputString[:-1] + 'dot'

# Print the final output
print(outputString)

# End
