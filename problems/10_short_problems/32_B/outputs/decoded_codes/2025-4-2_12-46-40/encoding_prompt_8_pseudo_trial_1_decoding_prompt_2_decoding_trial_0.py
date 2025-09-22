# Read Input
inputString = input().strip()  # Obtain input and remove extra spaces

# Initialize Variables
index = 0  # Counter to track current position in the input string
outputString = ""  # String to accumulate the result

# Process Input Until End
while index < len(inputString):
    if inputString[index] == '.':  # If the current character is a dot
        outputString += '0'  # Append '0' to outputString
        index += 1  # Move to the next character
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':  # If the next character is a dot
        outputString += '1'  # Append '1' to outputString
        index += 2  # Skip to the character after the next
    else:  # No dots found in the conditions above
        outputString += '2'  # Append '2' to outputString
        index += 2  # Skip to the character after the next

# Output Result
print(outputString)  # Print the final outputString
