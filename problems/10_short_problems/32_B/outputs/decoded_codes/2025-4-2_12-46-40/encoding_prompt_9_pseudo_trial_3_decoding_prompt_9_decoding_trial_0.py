# Read a line of input from the user and remove extra spaces
inputString = input().strip()

# Initialize the index variable and output string
index = 0
outputString = ""

# Process the input string based on defined rules
while index < len(inputString):
    if inputString[index] == '.':
        outputString += '0'
        index += 1
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':
        outputString += '1'
        index += 2
    else:
        outputString += '2'
        index += 2

# Print the converted numerical representation
print(outputString)
