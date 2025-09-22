# Step 1: Initialize Input
inputString = input().strip()  # Read a line of input from the user

# Step 2: Setup Variables
index = 0
outputString = ""

# Step 3: Process Input String
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

# Step 4: Output Result
print(outputString)  # Print the final numerical representation
