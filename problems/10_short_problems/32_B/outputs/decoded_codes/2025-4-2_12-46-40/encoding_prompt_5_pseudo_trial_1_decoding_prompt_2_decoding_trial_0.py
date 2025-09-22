# Accept input string from the user
inputString = input().strip()

# Initialize an index variable and an empty result string
index = 0
resultString = ''

# Loop through the characters in the input string
while index < len(inputString):
    
    # Check if the current character is a dot
    if inputString[index] == '.':
        # Append '0' to the result string
        resultString += '0'
        index += 1
        
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':
        # Append '1' to the result string
        resultString += '1'
        index += 2
        
    else:
        # If the next character is not a dot, append '2' to the result string
        resultString += '2'
        index += 2

# Print the final result string
print(resultString)
