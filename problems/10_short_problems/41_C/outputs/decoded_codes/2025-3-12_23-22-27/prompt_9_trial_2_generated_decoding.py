# Step 1: Receive Input
inputString = input().strip()  # Read input and remove extra spaces

# Step 2: Replace Keywords
inputString = inputString.replace("dot", ".")
inputString = inputString.replace("at", "@")

# Step 3: Check Starting Character
if inputString.startswith("."):
    inputString = "dot" + inputString[1:]  # Prepend "dot" except for the first character

# Step 4: Initialize Variables
countAt = 0
resultList = []  # To construct final output list

# Step 5: Check and Correct Starting Character
if inputString.startswith("@"):
    inputString = "at" + inputString[1:]  # Prepend "at" except for the first character

# Step 6: Process Each Character
for character in inputString:
    if character == "@":
        if countAt > 0:
            resultList.append("at")  # If "at" already occurred, append the word
        else:
            resultList.append("@")  # Append symbol "@" for first occurrence
            countAt = 1
    else:
        resultList.append(character)  # Append other characters as they are

# Step 7: Combine the List
finalOutput = ''.join(resultList)  # Join list to create final string

# Step 8: Fix Ending Character
if finalOutput.endswith("."):
    finalOutput = finalOutput[:-1] + "dot"  # Replace final "." with "dot"

# Step 9: Output the Result
print(finalOutput)
