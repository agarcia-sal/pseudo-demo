# Read input from standard input and remove any extra spaces or newline characters
inputString = input().strip()

# Initialize index and output string
index = 0
outputString = ""

# Process the input string while there are still characters remaining
while index < len(inputString):
    
    # Check if the current character is a single dot
    if inputString[index] == '.':
        outputString += '0'
        index += 1  # Move to the next character
    
    # Check if the next character is also a dot
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':
        outputString += '1'
        index += 2  # Move past the pair of dots
    
    # If neither case is met, we have a dot followed by something else
    else:
        outputString += '2'
        index += 2  # Move past the pair of characters

# Output the final result
print(outputString)
