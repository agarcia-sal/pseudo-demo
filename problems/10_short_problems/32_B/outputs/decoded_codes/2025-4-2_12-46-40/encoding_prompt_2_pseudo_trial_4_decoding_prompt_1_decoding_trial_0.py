# Step 1: Input
inputString = input().strip()

# Step 2: Initialization
currentIndex = 0
outputString = ""

# Step 3: Process Loop
while currentIndex < len(inputString):
    if inputString[currentIndex] == '.':
        outputString += '0'
        currentIndex += 1
    else:
        if currentIndex + 1 < len(inputString) and inputString[currentIndex + 1] == '.':
            outputString += '1'
            currentIndex += 2
        else:
            outputString += '2'
            currentIndex += 2

# Step 4: Output
print(outputString)
