# Receive input from the user
inputString = input().strip()  # Read a single line of input and remove surrounding spaces

# Initialize variables
index = 0  # This will track the current position in the input string
outputString = ""  # This will store the decoded result

# Process input string
while index < len(inputString):
    if inputString[index] == '.':
        outputString += '0'  # Append '0' for a single dot
        index += 1  # Move to the next character
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':
        outputString += '1'  # Append '1' for a pair of dots
        index += 2  # Move past this pair of characters
    else:
        outputString += '2'  # Append '2' for any other character
        index += 2  # Move past this pair of characters

# Output result
print(outputString)
