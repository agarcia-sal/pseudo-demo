# 1. Read Input
inputString = input()

# 2. Replace Keywords
inputString = inputString.replace("dot", ".")
inputString = inputString.replace("at", "@")

# 3. Handle Special Case for Initial Character
if inputString.startswith("."):
    inputString = "dot" + inputString[1:]

# 4. Initialize Variables
atCount = 0
resultList = []

# 5. Handle Special Case for Email Format
if inputString.startswith("@"):
    inputString = "at" + inputString[1:]

# 6. Process Each Character
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

# 7. Combine Results
outputString = ''.join(resultList)

# 8. Handle Ending Special Case
if outputString.endswith("."):
    outputString = outputString[:-1] + "dot"

# 9. Output Result
print(outputString)
