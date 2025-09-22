# Begin Program

# Read Input: Accept a line of input from the user and remove spaces
inputString = input().strip()

# Initialize Variables: Set index to 0 and create empty output string
index = 0
outputString = ""

# Process Input: Loop through the input string while the index is less than its length
while index < len(inputString):
    # Check if the current character is a period '.'
    if inputString[index] == '.':
        outputString += '0'  # Append '0' to the output string
        index += 1  # Move to the next character
    # Check if the next character is also a period
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':
        outputString += '1'  # Append '1' to the output string
        index += 2  # Skip both characters
    else:
        outputString += '2'  # Append '2' to the output string
        index += 2  # Skip both characters

# Output Result: Print the value of outputString
print(outputString)

# End Program
