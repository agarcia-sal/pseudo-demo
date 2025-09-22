def process_input():
    # Read input from the user
    inputString = input().strip()

    # Replace specified words with symbols
    inputString = inputString.replace("dot", ".").replace("at", "@")

    # Ensure that the string starts with "dot" if it begins with '.'
    if inputString.startswith('.'):
        inputString = "dot" + inputString[1:]

    # Initialize variables for processing
    consecutiveAtCount = 0
    resultCharacters = []

    # If the string starts with '@', prefix it with "at"
    if inputString.startswith('@'):
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
            consecutiveAtCount = 0  # reset for any non-@ character

    # Join the characters back into a single string
    outputString = ''.join(resultCharacters)

    # If the last character of outputString is '.', replace it with 'dot'
    if outputString.endswith('.'):
        outputString = outputString[:-1] + "dot"

    # Display the final output
    print(outputString)

# Example test cases or unit tests could be written to ensure correctness.
