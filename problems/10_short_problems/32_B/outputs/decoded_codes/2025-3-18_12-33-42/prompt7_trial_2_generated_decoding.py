def convertSymbolToNumber():
    # Initialize index to keep track of our position in the input string
    index = 0
    # Initialize an empty string to build our answer
    answerString = ""
    
    # Read the input string from the user
    inputString = input()
    
    # Process each character until we reach the end of the input string
    while index < len(inputString):
        # If the current character is a dot (.)
        if inputString[index] == '.':
            # Append '0' to the answer string
            answerString += '0'
            # Move to the next character
            index += 1
        # If the next character is also a dot (.)
        elif index + 1 < len(inputString) and inputString[index + 1] == '.':
            # Append '1' to the answer string
            answerString += '1'
            # Move past both dots
            index += 2
        else:
            # For any other character or sequence, append '2'
            answerString += '2'
            # Move past this character
            index += 2
    
    # Return the result as a string of numbers
    return answerString

# Example usage (uncomment the following line to test the function after defining it)
# print(convertSymbolToNumber())
