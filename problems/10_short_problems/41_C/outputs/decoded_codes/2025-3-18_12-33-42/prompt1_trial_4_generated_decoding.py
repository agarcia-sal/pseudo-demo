# Read Input
inputString = input().strip()

# Replace Keywords
inputString = inputString.replace("dot", ".")
inputString = inputString.replace("at", "@")

# Check Initial Character for Dot
if inputString and inputString[0] == '.':
    inputString = "dot" + inputString[1:]

# Initialize Variables
countAtSign = 0
resultList = []
# length = 0 (this variable will not be used further, so we omit it)

# Check First Character for At
if inputString and inputString[0] == '@':
    inputString = "at" + inputString[1:]

# Process Each Character
for currentChar in inputString:
    if currentChar == '@':
        if countAtSign > 0:
            resultList.append("at")
            countAtSign = 1  # We have encountered another '@'
        else:
            resultList.append('@')
            countAtSign = 1  # This indicates that we have encountered an '@'
    else:
        resultList.append(currentChar)

# Combine and Finalize Output
finalString = ''.join(resultList)

if finalString and finalString[-1] == '.':
    finalString = finalString[:-1] + "dot"

# Display Result
print(finalString)
