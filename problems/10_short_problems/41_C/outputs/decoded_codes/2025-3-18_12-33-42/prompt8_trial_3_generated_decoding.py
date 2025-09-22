# Step 1: Read Input
inputString = input()

# Step 2: Replace Keywords
inputString = inputString.replace("dot", ".")
inputString = inputString.replace("at", "@")

# Step 3: Check Leading Character for "."
if inputString.startswith("."):
    inputString = "dot" + inputString[1:]

# Initialization
counter = 0
characterList = []
length = 0  # This variable is not used further

# Step 5: Check Leading Character for "at"
if inputString.startswith("@"):
    inputString = "at" + inputString[1:]

# Step 6: Process Each Character
for char in inputString:
    if char == "@":
        if counter > 0:
            characterList.append("at")
            counter = 1
        else:
            characterList.append("@")
            counter = 1
    else:
        characterList.append(char)

# Step 7: Join Processed Characters
finalString = ''.join(characterList)

# Step 8: Check Ending Character
if finalString.endswith("."):
    finalString = finalString[:-1] + "dot"

# Step 9: Output Result
print(finalString)
