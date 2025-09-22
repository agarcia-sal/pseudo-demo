# Read input from standard input and store in inputString
inputString = input()

# Replace "dot" with "."
inputString = inputString.replace("dot", ".")

# Replace "at" with "@"
inputString = inputString.replace("at", "@")

# Handle special case for the initial character
if inputString and inputString[0] == ".":
    inputString = "dot" + inputString[1:]  # Prepend "dot"

# Initialize variables
atCount = 0  # Counter for occurrences of "@"
resultList = []  # List to collect characters and strings

# Handle special case for email format
if inputString and inputString[0] == "@":
    inputString = "at" + inputString[1:]  # Change first character to "at"

# Process each character in inputString
for currentChar in inputString:
    if currentChar == "@":
        if atCount > 0:
            resultList.append("at")  # Append "at" for further occurrences
            atCount = 1  # Maintain count of the last occurrence
        else:
            resultList.append("@")  # Append "@" for the first occurrence
            atCount = 1  # Set count to indicate first occurrence
    else:
        resultList.append(currentChar)  # Append current character

# Combine results into a single string
outputString = "".join(resultList)

# Handle ending special case
if outputString and outputString[-1] == ".":
    outputString = outputString[:-1] + "dot"  # Replace ending "." with "dot"

# Output the final result
print(outputString)
