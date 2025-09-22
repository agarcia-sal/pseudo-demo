# BEGIN PROGRAM

# Read a single line of input and remove any whitespace around it
inputString = input().strip()

# Initialize an index to track our current position in the input string
index = 0

# Initialize an empty string to store the result
resultString = ""

# Continue processing until we reach the end of the input string
while index < len(inputString):
    
    # Check the character at the current index
    if inputString[index] == '.':
        # If it is a dot, append '0' to the result
        resultString += '0'
        # Move to the next character
        index += 1
        
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':
        # If the next character is a dot, append '1' to the result
        resultString += '1'
        # Move past the pair of characters
        index += 2
        
    else:
        # If there is no dot in the next character, append '2' to the result
        resultString += '2'
        # Move past the pair of characters
        index += 2

# Output the final translated string
print(resultString)

# END PROGRAM
