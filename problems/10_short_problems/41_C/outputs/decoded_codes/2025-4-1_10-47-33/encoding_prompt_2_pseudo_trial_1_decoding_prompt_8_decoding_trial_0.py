# Start
# Read Input
userInput = input().strip()

# Replace Substrings
userInput = userInput.replace("dot", ".").replace("at", "@")

# Check Beginning Character
if userInput and userInput[0] == '.':
    userInput = 'dot' + userInput[1:]

# Initialize Variables
counter = 0
charList = []

# Check for Starting Character
if userInput and userInput[0] == '@':
    userInput = 'at' + userInput[1:]

# Process Each Character
for currentChar in userInput:
    if currentChar == '@':
        if counter > 0:
            charList.append("at")
            counter = 1
        else:
            charList.append("@")
            counter = 1
    else:
        charList.append(currentChar)

# Join Characters
finalResult = ''.join(charList)

# Check Ending Character
if finalResult and finalResult[-1] == '.':
    finalResult = finalResult[:-1] + 'dot'

# Output Result
print(finalResult)
# End
