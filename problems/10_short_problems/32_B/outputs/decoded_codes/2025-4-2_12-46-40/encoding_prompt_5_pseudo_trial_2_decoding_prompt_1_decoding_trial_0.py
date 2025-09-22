def convertSymbolsToNumbers():
    # Step 1: Read input from the user
    sequenceOfCharacters = input()
    
    # Step 2: Initialize an index and an empty result string
    currentIndex = 0
    resultString = ""
    
    # Step 3: Process the input sequence until the end
    while currentIndex < len(sequenceOfCharacters):
        # Step 4: Check the current character
        if sequenceOfCharacters[currentIndex] == '.':
            # If it's a dot, convert to '0'
            resultString += '0'
            currentIndex += 1
        elif currentIndex + 1 < len(sequenceOfCharacters) and sequenceOfCharacters[currentIndex + 1] == '.':
            # If the next character is a dot, convert to '1'
            resultString += '1'
            currentIndex += 2
        else:
            # If neither is a dot, convert to '2'
            resultString += '2'
            currentIndex += 2
            
    # Step 5: Output the result
    print(resultString)
