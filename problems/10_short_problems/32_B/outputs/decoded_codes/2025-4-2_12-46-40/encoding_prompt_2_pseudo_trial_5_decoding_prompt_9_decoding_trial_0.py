# Begin Program

# Read Input
inputString = input().strip()  # Accept input and strip leading/trailing spaces

# Initialize Variables
index = 0  # To keep track of our current position in inputString
outputString = ""  # To build our resulting output

# Process Input
while index < len(inputString):  # Loop until we reach the end of the input string
    if inputString[index] == '.':  # Check if the current character is a period
        outputString += '0'  # Append '0' to the output string
        index += 1  # Move to the next character
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':  # Check next character if within bounds
        outputString += '1'  # Append '1' to the output string
        index += 2  # Skip both current and next characters
    else:
        outputString += '2'  # Append '2' to the output string
        index += 2  # Skip both current and next characters

# Output Result
print(outputString)  # Print the resulting output string

# End Program
