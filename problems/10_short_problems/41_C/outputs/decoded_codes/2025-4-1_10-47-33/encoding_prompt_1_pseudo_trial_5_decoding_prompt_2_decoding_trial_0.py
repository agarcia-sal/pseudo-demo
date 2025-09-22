# Step 1: Read Input
inputString = input()

# Step 2: Replace Keywords
inputString = inputString.replace("dot", ".")
inputString = inputString.replace("at", "@")

# Step 3: Handle Special Case for Initial Character
if inputString and inputString[0] == ".":
    inputString = "dot" + inputString[1:]

# Step 4: Initialize Variables
atCount = 0
resultList = []

# Step 5: Handle Special Case for Email Format
if inputString and inputString[0] == "@":
    inputString = "at" + inputString[1:]

# Step 6: Process Each Character
for currentChar in inputString:
    if currentChar == "@":
        if atCount > 0:
            resultList.append("at")
            atCount = 1
        else:
            resultList.append(currentChar)
            atCount = 1
    else:
        resultList.append(currentChar)

# Step 7: Combine Results
outputString = ''.join(resultList)

# Step 8: Handle Ending Special Case
if outputString and outputString[-1] == ".":
    outputString = outputString[:-1] + "dot"

# Step 9: Output Result
print(outputString)
