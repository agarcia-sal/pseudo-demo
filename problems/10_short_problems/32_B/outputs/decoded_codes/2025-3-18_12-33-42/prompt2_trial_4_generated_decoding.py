# Input
inputString = input().strip()

# Initialize
currentIndex = 0
resultString = ""

# Process the Input
while currentIndex < len(inputString):
    if inputString[currentIndex] == '.':
        resultString += '0'
        currentIndex += 1
    else:
        if currentIndex + 1 < len(inputString) and inputString[currentIndex + 1] == '.':
            resultString += '1'
            currentIndex += 2
        else:
            resultString += '2'
            currentIndex += 2

# Output
print(resultString)
