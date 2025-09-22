# Begin
# Read a line of input, removing any extra spaces or newlines
inputString = input().strip()

# Initialize variables
index = 0
outputString = ""

# Loop until we reach the end of the input string
while index < len(inputString):
    # Check for the first character
    if inputString[index] == '.':
        # If the character is a dot, append '0' to output
        outputString += '0'
        index += 1
    else:
        # Check the next character without exceeding the string length
        if index + 1 < len(inputString) and inputString[index + 1] == '.':
            # If the next character is also a dot, append '1' to output
            outputString += '1'
            index += 2  # Move past both characters
        else:
            # Append '2' for a different pattern
            outputString += '2'
            index += 2  # Move past both characters

# Output the final converted string
print(outputString)
