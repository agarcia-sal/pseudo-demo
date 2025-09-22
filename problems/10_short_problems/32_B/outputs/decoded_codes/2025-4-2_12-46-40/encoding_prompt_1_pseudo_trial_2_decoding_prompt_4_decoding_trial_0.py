# Read input from the user and remove any leading or trailing whitespace
inputString = input().strip()

# Initialize an index variable to track the current position within the string
index = 0

# Initialize an empty string to build the resulting output
outputString = ""

# Loop while the current index is less than the length of the input string
while index < len(inputString):
    # Check if the current character is a dot
    if inputString[index] == '.':
        # Append '0' to the output string
        outputString += '0'
        # Move to the next character
        index += 1

    # Check if the next character is a dot (only if the current character was not a dot)
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':
        # Append '1' to the output string
        outputString += '1'
        # Skip the next character
        index += 2

    # If neither of the above conditions are met, it must be '00'
    else:
        # Append '2' to the output string
        outputString += '2'
        # Skip the next character
        index += 2

# Output the final result
print(outputString)
