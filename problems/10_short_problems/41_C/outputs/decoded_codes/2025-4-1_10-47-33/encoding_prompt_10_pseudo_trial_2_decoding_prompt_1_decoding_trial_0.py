# Step 1: Read Input
inputString = input().strip()

# Step 2: Replace Substrings
inputString = inputString.replace("dot", ".")
inputString = inputString.replace("at", "@")

# Step 3: Check Starting Character
if inputString and inputString[0] == '.':
    inputString = "dot" + inputString[1:]

# Step 4: Initialize Variables
countAt = 0
resultList = []
length = 0  # Not used later, but initialized.

# Step 5: Handle Starting Character for '@'
if inputString and inputString[0] == '@':
    inputString = "at" + inputString[1:]

# Step 6: Process Each Character
for character in inputString:
    if character == '@':
        if countAt > 0:
            resultList.append("at")
            countAt = 1
        else:
            resultList.append("@")
            countAt = 1
    else:
        resultList.append(character)

# Step 7: Join Result
processedString = ''.join(resultList)

# Step 8: Check Ending Character
if processedString and processedString[-1] == '.':
    processedString = processedString[:-1] + "dot"

# Step 9: Output the Result
print(processedString)
