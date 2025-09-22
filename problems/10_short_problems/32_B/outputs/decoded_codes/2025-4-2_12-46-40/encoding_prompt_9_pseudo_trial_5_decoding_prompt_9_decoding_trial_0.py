# Receive Input
inputString = input().strip()  # Read input from the user and remove whitespace

# Initialize Variables
index = 0  # To track the current position in the input string
outputString = ''  # To store the resulting numeric representation

# Process the Input String
while index < len(inputString):
    if inputString[index] == '.':
        outputString += '0'  # Append '0' if the current character is a single dot
        index += 1  # Move to the next character
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':
        outputString += '1'  # Append '1' if the next character is a dot
        index += 2  # Skip to the character after the next
    else:
        outputString += '2'  # Append '2' for any other character
        index += 2  # Skip to the character after the next

# Output the Result
print(outputString)  # Print the converted numerical representation
