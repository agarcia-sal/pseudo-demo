# 1. Read Input
emailInput = input().strip()

# 2. Replace Substrings
emailInput = emailInput.replace("dot", ".").replace("at", "@")

# 3. Ensure Starting Character Rule
if emailInput.startswith('.'):
    emailInput = "dot" + emailInput

# 4. Initialize State Variables
previousAtCount = 0
outputCharacters = []

# 5. Handle the '@' Character
if emailInput.startswith('@'):
    emailInput = "at" + emailInput[1:]

# 6. Process Each Character in the String
for currentCharacter in emailInput:
    if currentCharacter == '@':
        if previousAtCount > 0:
            outputCharacters.append("at")
            previousAtCount = 1
        else:
            outputCharacters.append('@')
            previousAtCount = 1
    else:
        outputCharacters.append(currentCharacter)

# 7. Form the Final Output String
finalOutput = ''.join(outputCharacters)
if finalOutput.endswith('.'):
    finalOutput = finalOutput[:-1] + "dot"

# 8. Display the Result
print(finalOutput)
