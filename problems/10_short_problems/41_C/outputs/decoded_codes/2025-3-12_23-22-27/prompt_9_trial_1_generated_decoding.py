# Receive Input
inputString = input().strip()  # Read input and remove extra spaces

# Replace Keywords
inputString = inputString.replace("dot", ".")  # Replace "dot" with "."
inputString = inputString.replace("at", "@")    # Replace "at" with "@"

# Check Starting Character
if inputString.startswith("."):
    inputString = "dot" + inputString[1:]  # Prepend "dot" if starts with "."

# Initialize Variables
countAt = 0  # To keep track of "@" occurrences
resultList = []  # To construct the final output

# Check and Correct Starting Character
if inputString.startswith("@"):
    inputString = "at" + inputString[1:]  # Prepend "at" if starts with "@"

# Process Each Character
for character in inputString:
    if character == "@":
        if countAt > 0:  # If "@" has already been added once
            resultList.append("at")  # Append the word "at"
        else:
            resultList.append("@")  # Append the symbol "@"
            countAt += 1  # Increment count of "@" occurrences
    else:
        resultList.append(character)  # Append the character directly

# Combine the List
finalOutput = ''.join(resultList)  # Create a string from the list

# Fix Ending Character
if finalOutput.endswith("."):
    finalOutput = finalOutput[:-1] + "dot"  # Replace final "." with "dot"

# Output the Result
print(finalOutput)  # Print the final output
