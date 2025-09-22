# BEGIN
# Read input from the user
inputString = input().strip()  # Read input line and remove surrounding whitespace

# Replace specified words with symbols
inputString = inputString.replace("dot", ".").replace("at", "@")

# Ensure that the string starts with "dot" if it begins with '.'
if inputString and inputString[0] == '.':
    inputString = "dot" + inputString[1:]

# Initialize variables for processing
consecutiveAtCount = 0
resultCharacters = []  # create an empty list to store result characters

# If the string starts with '@', prefix it with "at"
if inputString and inputString[0] == '@':
    inputString = "at" + inputString[1:]

# Iterate through each character in the inputString
for character in inputString:
    if character == '@':
        if consecutiveAtCount > 0:
            resultCharacters.append("at")
            consecutiveAtCount = 1
        else:
            resultCharacters.append("@")
            consecutiveAtCount = 1
    else:
        resultCharacters.append(character)

# Join the characters back into a single string
outputString = ''.join(resultCharacters)

# If the last character of outputString is '.', replace it with 'dot'
if outputString and outputString[-1] == '.':
    outputString = outputString[:-1] + "dot"

# Display the final output
print(outputString)
# END
