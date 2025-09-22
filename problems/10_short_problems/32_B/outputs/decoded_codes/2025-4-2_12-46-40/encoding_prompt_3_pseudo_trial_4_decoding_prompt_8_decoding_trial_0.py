# Read input string from standard input
stringInput = input().strip()

# Initialize variables
currentIndex = 0
resultString = ""

# Process the input string
while currentIndex < len(stringInput):
    if stringInput[currentIndex] == '.':
        # Append '0' for a single dot
        resultString += '0'
        currentIndex += 1
    elif (currentIndex + 1 < len(stringInput)) and (stringInput[currentIndex + 1] == '.'):
        # Append '1' for two consecutive dots (dot followed by a dot)
        resultString += '1'
        currentIndex += 2
    else:
        # Append '2' for any other two characters (dot followed by a different character)
        resultString += '2'
        currentIndex += 2

# Output the result
print(resultString)


def process_string(stringInput):
    stringInput = stringInput.strip()
    currentIndex = 0
    resultString = ""

    while currentIndex < len(stringInput):
        if stringInput[currentIndex] == '.':
            resultString += '0'
            currentIndex += 1
        elif (currentIndex + 1 < len(stringInput)) and (stringInput[currentIndex + 1] == '.'):
            resultString += '1'
            currentIndex += 2
        else:
            resultString += '2'
            currentIndex += 2

    return resultString

# Read input and call the function
stringInput = input()
result = process_string(stringInput)
print(result)
