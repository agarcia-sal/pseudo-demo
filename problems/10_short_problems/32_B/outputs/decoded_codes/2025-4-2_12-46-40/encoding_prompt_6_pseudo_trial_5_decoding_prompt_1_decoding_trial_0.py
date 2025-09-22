# Begin
# Read a single line of input
inputString = input()

# Initialize variables
currentIndex = 0
resultString = ''

# Loop until the end of the input string
while currentIndex < len(inputString):
    
    # Check for a '.' character
    if inputString[currentIndex] == '.':
        # Append '0' to the result string
        resultString += '0'
        # Move to the next character
        currentIndex += 1
        
    # Check for two consecutive character patterns
    elif currentIndex + 1 < len(inputString) and inputString[currentIndex + 1] == '.':
        # Append '1' to the result string
        resultString += '1'
        # Skip the next character
        currentIndex += 2
        
    else:
        # Append '2' to the result string
        resultString += '2'
        # Skip the next character
        currentIndex += 2

# Output the final result string
print(resultString)
# End
