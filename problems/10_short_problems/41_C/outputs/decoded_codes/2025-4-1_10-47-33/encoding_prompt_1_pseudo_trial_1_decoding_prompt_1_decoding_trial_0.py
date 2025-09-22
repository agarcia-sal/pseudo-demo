# BEGIN

# Read input from user and remove unnecessary whitespace
inputString = input().strip()
inputString = inputString.replace("dot", ".")
inputString = inputString.replace("at", "@")

# Check if the input starts with a dot and modify accordingly
if inputString[0] == ".":
    inputString = "dot" + inputString[1:]

# Initialize a counter and an empty list for constructing the output
counter = 0
characterList = []

# Check if the input starts with an @ and modify accordingly
if inputString[0] == "@":
    inputString = "at" + inputString[1:]

# Iterate through each character in the input string
for character in inputString:

    # Check for the occurrence of '@' character
    if character == "@":
        if counter > 0:
            # Append "at" to characterList if we already encountered an '@'
            characterList.append("at")
            counter = 1 
        else:
            # Append "@" to characterList for the first occurrence
            characterList.append("@")
            counter = 1
    else:
        # If the character is not '@', simply add it to characterList
        characterList.append(character)

# Join all characters in characterList into a single string
outputString = ''.join(characterList)

# Check if the final character is a dot and modify accordingly
if outputString[-1] == ".":
    outputString = outputString[:-1] + "dot"

# Print the final output
print(outputString)

# END
