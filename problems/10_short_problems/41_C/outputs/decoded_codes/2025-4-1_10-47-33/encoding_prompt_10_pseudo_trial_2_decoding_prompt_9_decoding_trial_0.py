# Read Input: 
inputString = input().strip()  # Remove leading and trailing whitespace

# Replace Substrings:
inputString = inputString.replace("dot", ".")  # Replace "dot" with "."
inputString = inputString.replace("at", "@")    # Replace "at" with "@"

# Check Starting Character:
if inputString and inputString[0] == '.':
    inputString = "dot" + inputString[1:]  # Prepend "dot" if first character is '.'

# Initialize Variables:
countAt = 0  # Track occurrences of '@'
resultList = []  # List to hold processed characters
length = 0  # Initialize length (not used later)

# Handle Starting Character for '@':
if inputString and inputString[0] == '@':
    inputString = "at" + inputString[1:]  # Prepend "at" if first character is '@'

# Process Each Character:
for character in inputString:
    if character == '@':
        if countAt > 0:
            resultList.append("at")  # Append "at" if there's already an '@'
            countAt = 1  # Set count to 1
        else:
            resultList.append('@')  # Append '@'
            countAt = 1  # Set count to 1
    else:
        resultList.append(character)  # Append the character to the result list

# Join Result:
processedString = ''.join(resultList)  # Join elements to form final string

# Check Ending Character:
if processedString and processedString[-1] == '.':
    processedString = processedString[:-1] + "dot"  # Replace last character with "dot"

# Output the Result:
print(processedString)  # Print the processed string
