# BEGIN

# Step 1: Read a line of input and remove leading/trailing white spaces
inputLine = input().strip()

# Step 2: Replace all occurrences of "dot" with "." and "at" with "@"
updatedString = inputLine.replace("dot", ".").replace("at", "@")

# Step 3: Check if the first character is "."
if updatedString.startswith("."):
    # Prepend "dot" to the updatedString (excluding the first character)
    updatedString = "dot" + updatedString[1:]

# Step 4: Initialize a counter for "at" occurrences and an empty list to store characters
countAtSymbols = 0
characterList = []

# Step 5: Check if the first character is "@"
if updatedString.startswith("@"):
    # Prepend "at" to the updatedString (excluding the first character)
    updatedString = "at" + updatedString[1:]

# Step 6: Iterate through each character in the updatedString
for character in updatedString:
    if character == "@":
        # If this is not the first occurrence of "at"
        if countAtSymbols > 0:
            # Append "at" to the character list
            characterList.append("at")
            # Update the counter to indicate "at" has been handled
            countAtSymbols = 1
        else:
            # First occurrence of "@", just append it
            characterList.append("@")
            # Update the counter
            countAtSymbols = 1
    else:
        # For any other character, simply add it to the character list
        characterList.append(character)

# Step 7: Join the characters in the list into a single string
finalString = ''.join(characterList)

# Step 8: Check if the last character is "."
if finalString.endswith("."):
    # Replace the last character with "dot"
    finalString = finalString[:-1] + "dot"

# Step 9: Output the final modified string
print(finalString)

# END
