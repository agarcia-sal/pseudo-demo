# Step 1: Input
inputString = input()

# Step 2: Initialize Variables
currentIndex = 0
outputString = ""

# Step 3: Processing Loop
while currentIndex < len(inputString):
    if inputString[currentIndex] == '.':
        outputString += '0'
        currentIndex += 1
    elif currentIndex + 1 < len(inputString) and inputString[currentIndex + 1] == '.':
        outputString += '1'
        currentIndex += 2
    else:
        outputString += '2'
        currentIndex += 2

# Step 4: Output
print(outputString)
