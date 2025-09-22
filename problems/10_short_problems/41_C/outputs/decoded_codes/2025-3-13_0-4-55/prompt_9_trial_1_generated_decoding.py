# Receive Input
inputString = input().strip()  # Read the input and remove extra spaces

# Replace Keywords
inputString = inputString.replace("dot", ".")  # Replace "dot" with "."
inputString = inputString.replace("at", "@")    # Replace "at" with "@"

# Check Starting Character
if inputString.startswith("."):
    inputString = "dot" + inputString[1:]  # Prepend "dot" if it starts with "."

# Initialize Variables
countAt = 0  # To keep track of "@" occurrences
resultList = []  # To construct the final output

# Check and Correct Starting Character
if inputString.startswith("@"):
    inputString = "at" + inputString[1:]  # Prepend "at" if it starts with "@" 

# Process Each Character
for character in inputString:
    if character == "@":
        if countAt > 0:
            resultList.append("at")  # Append "at" if we've seen "@" before
        else:
            resultList.append("@")  # Append "@" symbol
            countAt = 1  # Update the count of "@" occurrences
    else:
        resultList.append(character)  # Append any character that is not "@"

# Combine the List
finalOutput = ''.join(resultList)  # Create a string by joining all elements

# Fix Ending Character
if finalOutput.endswith("."):
    finalOutput = finalOutput[:-1] + "dot"  # Replace ending "." with "dot"

# Output the Result
print(finalOutput)  # Print the final processed output
