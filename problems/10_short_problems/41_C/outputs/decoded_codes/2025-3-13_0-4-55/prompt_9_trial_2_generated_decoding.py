# Receive Input
inputString = input().strip()  # Read a line of input from the user and remove any extra spaces

# Replace Keywords
inputString = inputString.replace("dot", ".")  # Replace "dot" with "."
inputString = inputString.replace("at", "@")    # Replace "at" with "@"

# Check Starting Character
if inputString.startswith("."):
    inputString = "dot" + inputString[1:]  # Prepend "dot" if the string starts with "."

# Initialize Variables
countAt = 0  # To track occurrences of "@"
resultList = []  # To construct the final output

# Check and Correct Starting Character
if inputString.startswith("@"):
    inputString = "at" + inputString[1:]  # Prepend "at" if the string starts with "@"

# Process Each Character
for character in inputString:
    if character == "@":
        if countAt > 0:
            resultList.append("at")  # Replace repeated "@" with "at"
        else:
            resultList.append("@")  # Append "@" to the resultList
            countAt = 1  # Increment count of "@"
    else:
        resultList.append(character)  # Append other characters as they are

# Combine the List
finalOutput = ''.join(resultList)  # Create a string from the resultList

# Fix Ending Character
if finalOutput.endswith("."):
    finalOutput = finalOutput[:-1] + "dot"  # Replace ending "." with "dot"

# Output the Result
print(finalOutput)  # Print the standardized email-like format
