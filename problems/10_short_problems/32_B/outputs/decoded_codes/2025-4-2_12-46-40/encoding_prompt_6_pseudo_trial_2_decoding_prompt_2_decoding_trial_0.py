# Read input string from standard input
inputString = input()

# Initialize index and output variable
index = 0
outputString = ""

# Loop through the input string until the end
while index < len(inputString):
    
    # Check if the current character is '.'
    if inputString[index] == '.':
        # Append '0' to the output
        outputString += '0'
        # Move to the next character
        index += 1
    
    # Check for the pattern ".."
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':
        # Append '1' to the output
        outputString += '1'
        # Move the index forward by two characters
        index += 2
        
    # Otherwise, the pattern is '.-' or another character
    else:
        # Append '2' to the output
        outputString += '2'
        # Move the index forward by two characters
        index += 2

# Output the final result
print(outputString)
