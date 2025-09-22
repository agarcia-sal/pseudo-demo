# Read Input
inputString = input().strip()

# Replace Substrings
inputString = inputString.replace("dot", ".")
inputString = inputString.replace("at", "@")

# Check Starting Character
if inputString.startswith('.'):
    inputString = "dot" + inputString[1:]

# Initialize Variables
countAt = 0
resultList = []
length = 0  # Initialized but not used later

# Handle Starting Character for `@`
if inputString.startswith('@'):
    inputString = "at" + inputString[1:]

# Process Each Character
for character in inputString:
    if character == '@':
        if countAt > 0:
            resultList.append("at")
            countAt = 1
        else:
            resultList.append('@')
            countAt = 1
    else:
        resultList.append(character)

# Join Result
processedString = ''.join(resultList)

# Check Ending Character
if processedString.endswith('.'):
    processedString = processedString[:-1] + "dot"

# Output the Result
print(processedString)
