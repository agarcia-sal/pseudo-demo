# Receive Input
inputString = input().strip()  # Read input and remove surrounding spaces

# Replace Keywords
inputString = inputString.replace("dot", ".")
inputString = inputString.replace("at", "@")

# Check Starting Character
if inputString.startswith("."):
    inputString = "dot" + inputString[1:]  # Prepend "dot" if the first character is "."

# Initialize Variables
countAt = 0  # To count occurrences of "@"
resultList = []  # List to construct final output

# Check and Correct Starting Character
if inputString.startswith("@"):
    inputString = "at" + inputString[1:]  # Prepend "at" if the first character is "@"

# Process Each Character
for character in inputString:
    if character == "@":
        if countAt > 0:  # If we've already seen an "@", append "at"
            resultList.append("at")
        else:  # First instance of "@"
            resultList.append("@")
        countAt = 1  # Set count for "at"
    else:
        resultList.append(character)  # Append normal characters

# Combine the List
finalOutput = ''.join(resultList)  # Create final string from list

# Fix Ending Character
if finalOutput.endswith("."):
    finalOutput = finalOutput[:-1] + "dot"  # Replace final "." with "dot"

# Output the Result
print(finalOutput)
