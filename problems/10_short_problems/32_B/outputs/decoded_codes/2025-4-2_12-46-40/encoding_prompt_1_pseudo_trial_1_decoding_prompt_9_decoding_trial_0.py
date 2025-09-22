# Start the program

# Read a line of input from standard input and trim whitespace
inputString = input().strip()

# Initialize an index variable to 0
currentIndex = 0

# Initialize an empty string variable to hold the output
result = ""

# While the currentIndex is less than the length of inputString
while currentIndex < len(inputString):
    # If the character at currentIndex is a dot
    if inputString[currentIndex] == '.':
        # Append '0' to result
        result += '0'
        # Increment currentIndex by 1
        currentIndex += 1
    # Else If the next character is a dot and currentIndex does not exceed length
    elif currentIndex + 1 < len(inputString) and inputString[currentIndex + 1] == '.':
        # Append '1' to result
        result += '1'
        # Increment currentIndex by 2
        currentIndex += 2
    # Else
    else:
        # Append '2' to result
        result += '2'
        # Increment currentIndex by 2
        currentIndex += 2

# Output the value of result
print(result)

# End the program
