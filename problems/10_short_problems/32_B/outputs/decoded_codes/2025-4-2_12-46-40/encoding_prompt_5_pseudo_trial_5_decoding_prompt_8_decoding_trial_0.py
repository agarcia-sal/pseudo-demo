# Receive Input
inputString = input().strip()

# Initialize Variables
index = 0
outputString = ""

# Process Input String
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

# Output Result
print(outputString)
