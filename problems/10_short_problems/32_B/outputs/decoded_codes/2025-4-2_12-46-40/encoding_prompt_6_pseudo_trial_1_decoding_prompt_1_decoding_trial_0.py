def ConvertDotNotationToNumber():
    # Read input from the user
    inputString = input()
    
    # Initialize index and output variable
    index = 0
    outputString = ''
    
    # Loop through the entire input string
    while index < len(inputString):
        # Check if the current character is a single dot
        if inputString[index] == '.':
            # Append '0' to the output for a single dot
            outputString += '0'
            # Move to the next character
            index += 1
            
        else:
            # Check the next character
            if index + 1 < len(inputString) and inputString[index + 1] == '.':
                # Append '1' to the output for a pair of dots
                outputString += '1'
                # Move the index forward by 2 characters
                index += 2
            else:
                # Append '2' for a pair where the first is dot and the second is not
                outputString += '2'
                # Move the index forward by 2 characters
                index += 2
    
    # Output the final result
    print(outputString)

