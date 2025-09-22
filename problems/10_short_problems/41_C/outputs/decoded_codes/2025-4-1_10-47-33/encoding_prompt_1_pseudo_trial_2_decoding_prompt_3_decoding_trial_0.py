def process_user_input():
    # Step 1: Read input and strip whitespace
    userInput = input().strip()

    # Step 2: Replace substrings "dot" with "." and "at" with "@"
    userInput = userInput.replace("dot", ".").replace("at", "@")

    # Step 3: Adjust starting character if needed
    if userInput.startswith("."):
        userInput = "dot" + userInput

    # Step 4: Initialize variables
    atCounter = 0
    convertedCharacters = []

    # Step 5: Handle the case for starting with "@"
    if userInput.startswith("@"):
        userInput = "at" + userInput[1:]

    # Step 6: Process each character
    for currentChar in userInput:
        if currentChar == "@":
            if atCounter > 0:
                convertedCharacters.append("at")
            else:
                convertedCharacters.append("@")
            atCounter = 1  # Set counter to indicate we have seen "at"
        else:
            convertedCharacters.append(currentChar)

    # Step 7: Combine converted characters into a single string
    result = ''.join(convertedCharacters)

    # Step 8: Final adjustments for the last character
    if result.endswith("."):
        result = result[:-1] + "dot"

    # Step 9: Output the result
    print(result)

# Call the function to process user input
process_user_input()
