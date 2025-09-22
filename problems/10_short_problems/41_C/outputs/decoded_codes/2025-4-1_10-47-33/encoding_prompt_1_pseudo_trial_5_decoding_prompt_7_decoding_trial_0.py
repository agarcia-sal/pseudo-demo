# Step 1: Read Input
inputString = input()  # Read a line of text from standard input

# Step 2: Replace Keywords
inputString = inputString.replace("dot", ".")  # Replace all occurrences of "dot" with "."
inputString = inputString.replace("at", "@")    # Replace all occurrences of "at" with "@"

# Step 3: Handle Special Case for Initial Character
if inputString and inputString[0] == ".":
    inputString = "dot" + inputString[1:]  # Prepend "dot" if the first character is "."

# Step 4: Initialize Variables
atCount = 0  # Counter for occurrences of "@"
resultList = []  # List to collect processed characters

# Step 5: Handle Special Case for Email Format
if inputString.startswith("@"):
    inputString = "at" + inputString[1:]  # Change first character to "at" if input starts with "@"

# Step 6: Process Each Character
for currentChar in inputString:
    if currentChar == "@":  # Check if the current character is "@"
        if atCount > 0:
            resultList.append("at")  # Append "at" for subsequent occurrences
            atCount = 1  # Update the counter
        else:
            resultList.append("@")  # Append "@" for the first occurrence
            atCount = 1  # Update the counter
    else:
        resultList.append(currentChar)  # Append the character if it's not "@"

# Step 7: Combine Results
outputString = ''.join(resultList)  # Join the list into a single string

# Step 8: Handle Ending Special Case
if outputString and outputString[-1] == ".":
    outputString = outputString[:-1] + "dot"  # Replace last "." with "dot"

# Step 9: Output Result
print(outputString)  # Print the final output string
