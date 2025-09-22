# Read a line of input from the user and remove any leading or trailing spaces.
inputString = input().strip()

# Replace occurrences of "dot" with "."
inputString = inputString.replace("dot", ".")

# Replace occurrences of "at" with "@"
inputString = inputString.replace("at", "@")

# Check if the first character is a "."
if inputString.startswith("."):
    # If true, prepend "dot" to the string (keeping the rest of the string).
    inputString = "dot" + inputString[1:]

# Initialize a counter for "at" occurrences 
counter = 0

# Create an empty list to hold the modified characters
charactersList = []

# Loop through each character in the modified input string 
for character in inputString:
    # If the character is "@"
    if character == "@":
        # Check if we've encountered "@" before
        if counter > 0:
            # If true, append "at" to the charactersList
            charactersList.append("at")
            counter = 1 
        else:
            # If false, append "@" to the charactersList
            charactersList.append("@")
            counter = 1
    else:
        # If it's not "@", append the character to the charactersList
        charactersList.append(character)

# Join the characters in the list to form a new string
modifiedString = ''.join(charactersList)

# Check if the last character in the modified string is "."
if modifiedString.endswith("."):
    # If true, remove the last character and append "dot" to the end
    modifiedString = modifiedString[:-1] + "dot"

# Output the final modified string
print(modifiedString)
