# Begin Program

# Read Input
inputString = input().strip()

# Initialize Variables
index = 0
outputString = ""

# Process Input
while index < len(inputString):
    if inputString[index] == '.':
        outputString += '0'
        index += 1  # Move to the next character
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':
        outputString += '1'
        index += 2  # Skip both current and next character
    else:
        outputString += '2'
        index += 2  # Skip both current and next character

# Output Result
print(outputString)

# End Program
