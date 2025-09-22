# Step 1: Start

# Step 2: Read Input
userInput = input().strip()

# Step 3: Replace Substrings
userInput = userInput.replace("dot", ".")
userInput = userInput.replace("at", "@")

# Step 4: Check Beginning Character
if userInput and userInput[0] == '.':
    userInput = "dot" + userInput[1:]  # Remove leading dot

# Step 5: Initialize Variables
counter = 0
charList = []

# Step 6: Check for Starting Character
if userInput and userInput[0] == '@':
    userInput = "at" + userInput[1:]  # Remove leading at

# Step 7: Process Each Character
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

# Step 8: Join Characters
finalResult = ''.join(charList)

# Step 9: Check Ending Character
if finalResult and finalResult[-1] == '.':
    finalResult = finalResult[:-1] + "dot"  # Remove last dot

# Step 10: Output Result
print(finalResult)

# Step 11: End
