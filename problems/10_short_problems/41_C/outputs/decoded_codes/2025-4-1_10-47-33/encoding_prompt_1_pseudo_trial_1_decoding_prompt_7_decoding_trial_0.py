# BEGIN

# Read input from user and remove unnecessary whitespace
inputString = input().strip()  # Read input and remove excess whitespace

# Replace occurrences of "dot" with "." and "at" with "@" in inputString
inputString = inputString.replace("dot", ".")
inputString = inputString.replace("at", "@")

# Check if the input starts with a dot and modify accordingly
if inputString.startswith("."):
    inputString = "dot" + inputString[1:]  # Prepend "dot" and skip the first character

# Initialize a counter and an empty list for constructing the output
counter = 0
characterList = []  # List to hold individual characters for final output

# Check if the input starts with an @ and modify accordingly
if inputString.startswith("@"):
    inputString = "at" + inputString[1:]  # Prepend "at" and skip the first character

# Iterate through each character in the input string
for character in inputString:
    # Check for the occurrence of '@' character
    if character == "@":
        if counter > 0:
            # Append "at" to characterList if we already encountered an '@'
            characterList.append("at")
            counter = 1  # Update counter to reflect we've seen '@'
        else:
            # Append "@" to characterList for the first occurrence
            characterList.append("@")
            counter = 1  # Update counter to reflect we've seen '@'
    else:
        # If the character is not '@', simply add it to characterList
        characterList.append(character)

# Join all characters in characterList into a single string
outputString = ''.join(characterList)  # Concatenate all elements in the character list

# Check if the final character is a dot and modify accordingly
if outputString.endswith("."):
    outputString = outputString[:-1] + "dot"  # Replace the last dot with "dot"

# Print the final output
print(outputString)

# END
