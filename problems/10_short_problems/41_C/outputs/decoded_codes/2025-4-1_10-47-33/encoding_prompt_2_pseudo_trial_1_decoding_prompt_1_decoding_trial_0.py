userInput = input().strip()


userInput = userInput.replace("dot", ".").replace("at", "@")


if userInput.startswith('.'):
    userInput = "dot" + userInput[1:]


counter = 0
charList = []
length = 0  # Ignored, can be omitted


if userInput.startswith('@'):
    userInput = "at" + userInput[1:]


for currentChar in userInput:
    if currentChar == '@':
        if counter > 0:
            charList.append("at")
            counter = 1
        else:
            charList.append("@")
            counter = 1
    else:
        charList.append(currentChar)


finalResult = ''.join(charList)


if finalResult.endswith('.'):
    finalResult = finalResult[:-1] + "dot"


print(finalResult)


userInput = input().strip()  # Read input and strip spaces

userInput = userInput.replace("dot", ".").replace("at", "@")  # Replace substrings

if userInput.startswith('.'):  # Check beginning character
    userInput = "dot" + userInput[1:]

counter = 0  # Initialize counter
charList = []  # Create an empty list for processed characters

if userInput.startswith('@'):  # Check for starting character
    userInput = "at" + userInput[1:]

for currentChar in userInput:  # Process each character
    if currentChar == '@':
        if counter > 0:
            charList.append("at")
            counter = 1
        else:
            charList.append("@")
            counter = 1
    else:
        charList.append(currentChar)

finalResult = ''.join(charList)  # Join characters into a string

if finalResult.endswith('.'):  # Check ending character
    finalResult = finalResult[:-1] + "dot"

print(finalResult)  # Output the result
