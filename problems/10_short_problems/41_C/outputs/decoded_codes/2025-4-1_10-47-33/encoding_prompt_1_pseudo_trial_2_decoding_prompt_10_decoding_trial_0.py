def process_input():
    # Step 1: Read and clean input
    userInput = input().strip()

    # Step 2: Replace substrings "dot" with "." and "at" with "@"
    userInput = userInput.replace("dot", ".").replace("at", "@")

    # Step 3: Adjust starting character if necessary
    if userInput.startswith("."):
        userInput = "dot" + userInput

    # Step 4: Initialize variables
    atCounter = 0
    convertedCharacters = []

    # Step 5: Handle starting character if it's "@"
    if userInput.startswith("@"):
        userInput = "at" + userInput[1:]

    # Step 6: Process each character in the input
    for currentChar in userInput:
        if currentChar == "@":
            if atCounter > 0:
                convertedCharacters.append("at")
                atCounter = 1
            else:
                convertedCharacters.append("@")
                atCounter = 1
        else:
            convertedCharacters.append(currentChar)

    # Step 7: Combine converted characters into a single string
    result = ''.join(convertedCharacters)

    # Step 8: Final adjustments for the last character
    if result.endswith('.'):
        result = result[:-1] + 'dot'

    # Step 9: Output the result
    print(result)

# Invoke the function to run the logic
process_input()
