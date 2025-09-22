# BEGIN PROGRAM

# Read input from the standard input and remove trailing spaces
inputString = input().strip()
originalString = inputString

# Replace occurrences in the string
originalString = originalString.replace("dot", ".")
originalString = originalString.replace("at", "@")

# Check if the first character is a dot
if originalString.startswith("."):
    originalString = "dot" + originalString

# Initialize variables to manage email formatting
previousChar = 0    # To track the last occurrence of '@'
formattedCharacters = []  # To hold formatted characters
lengthToLastChar = 0 # To hold the length of the formatted string

# Check if the string starts with an '@'
if originalString.startswith("@"):
    originalString = "at" + originalString

# Iterate through each character in the modified string
for character in originalString:
    # Check if the character is an '@'
    if character == "@":
        if previousChar > 0:
            formattedCharacters.append("at")
            previousChar = 1  # Indicate '@' was found
        else:
            formattedCharacters.append("@")
            previousChar = 1  # Indicate '@' was found
    else:
        formattedCharacters.append(character)

# Join the formatted characters into a single string
finalString = ''.join(formattedCharacters)

# Check if the last character of the formatted string is a dot
if finalString.endswith("."):
    finalString = finalString[:-1] + "dot"

# Print the final formatted string
print(finalString)

# END PROGRAM
