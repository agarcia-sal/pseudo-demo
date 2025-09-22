# Read Input
inputString = input()

# Replace Keywords
inputString = inputString.replace("dot", ".")
inputString = inputString.replace("at", "@")

# Handle Special Case for Initial Character
if inputString.startswith("."):
    inputString = "dot" + inputString[1:]

# Initialize Variables
atCount = 0
resultList = []

# Handle Special Case for Email Format
if inputString.startswith("@"):
    inputString = "at" + inputString[1:]

# Process Each Character
for currentChar in inputString:
    if currentChar == "@":
        if atCount > 0:
            resultList.append("at")
            atCount = 1
        else:
            resultList.append("@")
            atCount = 1
    else:
        resultList.append(currentChar)

# Combine Results
outputString = ''.join(resultList)

# Handle Ending Special Case
if outputString.endswith("."):
    outputString = outputString[:-1] + "dot"

# Output Result
print(outputString)
