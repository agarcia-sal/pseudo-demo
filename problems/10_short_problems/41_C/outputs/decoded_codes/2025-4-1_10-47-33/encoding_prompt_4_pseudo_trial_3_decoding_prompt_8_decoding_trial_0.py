def process_input():
    # Read input from standard input
    userInput = input()
    userInput = userInput.replace(" ", "").replace("dot", ".").replace("at", "@")
    
    # Ensure input does not start with a '.'
    if userInput.startswith('.'):
        userInput = 'dot' + userInput[1:]
    
    # Initialize variables
    occurrenceCounter = 0
    modifiedCharacters = []
    
    # Ensure input does not start with an '@'
    if userInput.startswith('@'):
        userInput = 'at' + userInput[2:]
    
    # Process each character in the userInput
    for character in userInput:
        if character == '@':
            if occurrenceCounter > 0:
                modifiedCharacters.append('at')
                occurrenceCounter = 1
            else:
                modifiedCharacters.append('@')
                occurrenceCounter = 1
        else:
            modifiedCharacters.append(character)

    # Join modified characters into a single string
    modifiedOutput = ''.join(modifiedCharacters)
    
    # Ensure output does not end with a '.'
    if modifiedOutput.endswith('.'):
        modifiedOutput = modifiedOutput[:-1] + 'dot'
    
    # Print the final modified output
    print(modifiedOutput)

# Call the function to execute the code
process_input()
