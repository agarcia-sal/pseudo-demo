# Step 1: Receive Input
inputString = input().strip()

# Step 2: Initialize Variables
index = 0
outputString = ""

# Step 3: Process the Input String
while index < len(inputString):
    if inputString[index] == '.':
        outputString += '0'
        index += 1
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':
        outputString += '1'
        index += 2
    else:
        outputString += '2'
        index += 2

# Step 4: Output the Result
print(outputString)
