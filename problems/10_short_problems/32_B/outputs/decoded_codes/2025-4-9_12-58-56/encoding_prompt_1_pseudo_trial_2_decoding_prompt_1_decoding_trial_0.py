# BEGIN

# Read input from the standard input and remove any extra spaces or newlines
stringValue = input().strip()

# Initialize a variable to keep track of the current position in the string
currentIndex = 0

# Initialize an empty string to store the final answer
numericString = ""

# Continue processing the string until we've examined all its characters
while currentIndex < len(stringValue):

    # If the current character is a period ('.')
    if stringValue[currentIndex] == '.':
        # Append '0' to our numeric string
        numericString += '0'
        # Move to the next character
        currentIndex += 1

    # If the next character is also a period ('.')
    elif (currentIndex + 1 < len(stringValue)) and (stringValue[currentIndex + 1] == '.'):
        # Append '1' to our numeric string
        numericString += '1'
        # Skip the next character and move forward
        currentIndex += 2

    # For all other cases
    else:
        # Append '2' to our numeric string
        numericString += '2'
        # Skip the next character and move forward
        currentIndex += 2

# Output the final numeric string
print(numericString)

# END
