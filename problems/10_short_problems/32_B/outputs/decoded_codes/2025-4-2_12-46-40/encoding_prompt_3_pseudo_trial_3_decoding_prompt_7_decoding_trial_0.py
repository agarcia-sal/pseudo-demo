# Begin main program
# Read input string from standard input
receivedString = input()

# Initialize index for string traversal
currentIndex = 0
# Initialize an empty string to store the result
resultString = ''

# Loop through the input string while the current index is within bounds
while currentIndex < len(receivedString):
    # Check if the current character is a dot (.)
    if receivedString[currentIndex] == '.':
        # Append '0' to the result string
        resultString += '0'
        # Move to the next character
        currentIndex += 1

    # Check if the next character exists and is a dot (.)
    elif currentIndex + 1 < len(receivedString) and receivedString[currentIndex + 1] == '.':
        # Append '1' to the result string
        resultString += '1'
        # Move the index forward by two characters
        currentIndex += 2

    # Otherwise, process the character as a different case
    else:
        # Append '2' to the result string
        resultString += '2'
        # Move the index forward by two characters
        currentIndex += 2

# Output the final result string
print(resultString)
