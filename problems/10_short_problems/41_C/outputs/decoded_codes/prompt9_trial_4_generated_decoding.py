# Step 1: Receive input
inputString = input().strip()  # Read input and remove extra spaces

# Step 2: Replace keywords
inputString = inputString.replace("dot", ".")  # Replace "dot" with "."
inputString = inputString.replace("at", "@")    # Replace "at" with "@"

# Step 3: Check starting character
if inputString.startswith("."):
    inputString = "dot" + inputString[1:]  # Prepend "dot" if it starts with "."

# Step 4: Initialize variables
countAt = 0  # Count of "@" occurrences
resultList = []  # List to build the final result

# Step 5: Check and correct starting character
if inputString.startswith("@"):
    inputString = "at" + inputString[1:]  # Prepend "at" if it starts with "@"

# Step 6: Process each character
for character in inputString:
    if character == "@":
        if countAt > 0:
            resultList.append("at")  # Append "at" if multiple "@" are found
            countAt = 1  # Set counter to 1 to track the latest encounter
        else:
            resultList.append("@")  # Append "@" for the first occurrence
            countAt = 1  # Increment the count
    else:
        resultList.append(character)  # Append non "@" characters

# Step 7: Combine the list into a final output string
finalOutput = ''.join(resultList)

# Step 8: Fix ending character
if finalOutput.endswith("."):
    finalOutput = finalOutput[:-1] + "dot"  # Replace trailing "." with "dot"

# Step 9: Output the result
print(finalOutput)
