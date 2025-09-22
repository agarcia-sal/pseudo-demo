# Read input from the user
inputString = input().strip()

# Replace 'dot' with '.' and 'at' with '@'
inputString = inputString.replace("dot", ".").replace("at", "@")

# Check if the first character is a '.' and prepend 'dot' if so
if inputString.startswith('.'):
    inputString = "dot" + inputString[1:]

# Initialize variables
countAt = 0
resultList = []

# Check if the first character is '@' and prepend 'at' if so
if inputString.startswith('@'):
    inputString = "at" + inputString[1:]

# Process each character in the input string
for character in inputString:
    if character == '@':
        if countAt > 0:
            resultList.append("at")
        else:
            resultList.append('@')
        countAt = 1
    else:
        resultList.append(character)
        countAt = 0  # Reset count for non-'@' characters

# Join the result list to form the processed string
processedString = ''.join(resultList)

# Check if the last character is a '.' and replace it with 'dot'
if processedString.endswith('.'):
    processedString = processedString[:-1] + "dot"

# Output the result
print(processedString)
