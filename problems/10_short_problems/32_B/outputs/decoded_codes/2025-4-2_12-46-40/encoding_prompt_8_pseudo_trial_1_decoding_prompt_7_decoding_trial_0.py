# Read Input
inputString = input().strip()  # Obtain input string and remove extra spaces

# Initialize Variables
index = 0  # Set counter variable for current position in the string
outputString = ""  # Create an empty string to accumulate the result

# Process Input Until End
while index < len(inputString):  # Continue processing until the end of the string
    if inputString[index] == '.':  # If the current character is a dot
        outputString += '0'  # Append '0' to outputString
        index += 1  # Move to the next character
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':  # If the next character is also a dot
        outputString += '1'  # Append '1' to outputString
        index += 2  # Skip to the character after the next
    else:  # If no dots are found in the above conditions
        outputString += '2'  # Append '2' to outputString
        index += 2  # Skip to the character after the next

# Output Result
print(outputString)  # Print the final translated numeric representation
