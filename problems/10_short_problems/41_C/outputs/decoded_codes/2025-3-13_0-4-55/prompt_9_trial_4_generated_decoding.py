# Receive input from the user
inputString = input().strip()  # Remove any extra spaces around the input

# Replace keywords with symbols
inputString = inputString.replace("dot", ".")
inputString = inputString.replace("at", "@")

# Check if the first character is '.'
if inputString.startswith('.'):
    inputString = "dot" + inputString[1:]  # Prepend "dot" and exclude the first character

# Initialize variables
countAt = 0  # To keep track of "@" occurrences
resultList = []  # To construct the final output

# Check if the first character is '@'
if inputString.startswith('@'):
    inputString = "at" + inputString[1:]  # Prepend "at" and exclude the first character

# Process each character in the inputString
for character in inputString:
    if character == "@":
        if countAt > 0:
            resultList.append("at")  # Append "at" if it was already appended
        else:
            resultList.append("@")  # Append the symbol "@" for the first time
        countAt = 1  # Increment count of "at" occurrences
    else:
        resultList.append(character)  # Append the current character

# Combine the list into a final output string
finalOutput = ''.join(resultList)

# Fix the ending character if the last character is '.'
if finalOutput.endswith('.'):
    finalOutput = finalOutput[:-1] + "dot"  # Replace the final '.' with "dot"

# Output the result
print(finalOutput)
