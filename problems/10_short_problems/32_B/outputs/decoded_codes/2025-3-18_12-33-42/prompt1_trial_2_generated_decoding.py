# BEGIN

# Read input string from standard input and remove any surrounding whitespace
inputString = input().strip()

# Initialize an index for traversing the string
index = 0

# Initialize an empty string to store the result
resultString = ""

# Continue processing while the index is less than the length of the input string
while index < len(inputString):
    # Check if the current character is a dot
    if inputString[index] == '.':
        # Append '0' to the result string
        resultString += '0'
        
        # Move to the next character
        index += 1
        
    # Check if the next character (index + 1) is a dot
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':
        # Append '1' to the result string
        resultString += '1'
        
        # Move the index forward by 2 characters
        index += 2
        
    # If neither of the above conditions are met
    else:
        # Append '2' to the result string
        resultString += '2'
        
        # Move the index forward by 2 characters
        index += 2

# Output the final result string
print(resultString)

# END
