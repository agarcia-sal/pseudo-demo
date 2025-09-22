def main():
    # Read input from the user and remove surrounding whitespace
    userInput = input().strip()

    # Replace all occurrences of 'dot' with '.' in the input
    userInput = userInput.replace('dot', '.')

    # Replace all occurrences of 'at' with '@' in the input
    userInput = userInput.replace('at', '@')

    # If the first character is a '.', prepend 'dot' to the input
    if userInput and userInput[0] == '.':
        userInput = 'dot' + userInput[1:]
    
    # Initialize a counter for 'at' occurrences
    counter = 0
    modifiedList = []
    
    # If the first character is an '@', prepend 'at' to the input
    if userInput and userInput[0] == '@':
        userInput = 'at' + userInput[1:]

    # Iterate over each character in modified userInput
    for character in userInput:
        if character == '@':
            # If this is not the first occurrence of '@'
            if counter > 0:
                modifiedList.append('at')
                counter = 1
            else:
                modifiedList.append('@')
                counter = 1
        else:
            # If the character is not '@', just add it to the list
            modifiedList.append(character)

    # Join all parts in modifiedList back into a single string
    finalOutput = ''.join(modifiedList)

    # If the last character of finalOutput is a '.', replace it with 'dot'
    if finalOutput and finalOutput[-1] == '.':
        finalOutput = finalOutput[:-1] + 'dot'

    # Output the final result
    print(finalOutput)

# Call the main function
main()
