# Define the main function to encapsulate the processing logic
def main():
    # Read input from the user and strip surrounding whitespace
    inputString = input().strip()

    # Replace specified words with symbols
    inputString = inputString.replace("dot", ".")
    inputString = inputString.replace("at", "@")

    # Ensure that the string starts with "dot" if it begins with '.'
    if inputString.startswith('.'):
        inputString = "dot" + inputString[1:]

    # Initialize variables for processing
    consecutiveAtCount = 0  # Counter for consecutive '@' characters
    resultCharacters = []    # List to store the resultant characters

    # If the string starts with '@', prefix it with "at"
    if inputString.startswith('@'):
        inputString = "at" + inputString[1:]

    # Iterate through each character in inputString
    for character in inputString:
        if character == '@':
            if consecutiveAtCount > 0:
                # If previously added '@', add 'at' instead
                resultCharacters.append("at")
                consecutiveAtCount = 1
            else:
                # First occurrence of '@'
                resultCharacters.append("@")
                consecutiveAtCount = 1
        else:
            # Append the character to the result list
            resultCharacters.append(character)
            consecutiveAtCount = 0  # Reset counter for consecutive '@'

    # Join the characters back into a single string
    outputString = ''.join(resultCharacters)

    # If the last character of outputString is '.', replace it with 'dot'
    if outputString.endswith('.'):
        outputString = outputString[:-1] + "dot"

    # Display the final output
    print(outputString)

# Execute the main function only if this module is run directly
if __name__ == "__main__":
    main()
