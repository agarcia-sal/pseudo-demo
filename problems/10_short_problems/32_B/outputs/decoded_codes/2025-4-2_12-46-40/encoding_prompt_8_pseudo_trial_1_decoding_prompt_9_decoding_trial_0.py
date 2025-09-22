# Read Input
inputString = input().strip()  # Read and strip the input string of extra spaces

# Initialize Variables
index = 0  # Counter variable to track the current position in the input string
outputString = ""  # String to accumulate the resulting numeric representation

# Process Input Until End
while index < len(inputString):
    if inputString[index] == '.':  # If the current character is a dot
        outputString += '0'  # Append '0' to the output
        index += 1  # Move to the next character
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':  # If the next character is also a dot
        outputString += '1'  # Append '1' to the output
        index += 2  # Skip to the character after the next
    else:  # If neither condition is met
        outputString += '2'  # Append '2' to the output
        index += 2  # Skip to the character after the next

# Output Result
print(outputString)  # Print the final numeric string representation
