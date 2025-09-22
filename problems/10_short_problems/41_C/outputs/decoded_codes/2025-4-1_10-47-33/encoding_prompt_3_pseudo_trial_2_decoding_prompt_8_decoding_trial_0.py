# Step 1: Read Input
emailInput = input().strip()

# Step 2: Replace Substrings
emailInput = emailInput.replace("dot", ".").replace("at", "@")

# Step 3: Ensure Starting Character Rule
if emailInput.startswith('.'):
    emailInput = "dot" + emailInput

# Step 4: Initialize State Variables
previousAtCount = 0
outputCharacters = []

# Step 5: Handle the '@' Character
if emailInput.startswith('@'):
    emailInput = "at" + emailInput[1:]

# Step 6: Process Each Character in the String
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

# Step 7: Form the Final Output String
finalOutput = ''.join(outputCharacters)
if finalOutput.endswith('.'):
    finalOutput = finalOutput[:-1] + "dot"

# Step 8: Display the Result
print(finalOutput)
