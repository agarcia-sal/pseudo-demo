# Start the program

# Read a line of input and remove any leading or trailing whitespace
inputString = input().strip()

# Initialize index variable and result string
currentIndex = 0
result = ""

# While loop to process the input string
while currentIndex < len(inputString):
    if inputString[currentIndex] == '.':
        # If the character is a dot, append '0' to result
        result += '0'
        currentIndex += 1
    elif currentIndex + 1 < len(inputString) and inputString[currentIndex + 1] == '.':
        # If the next character is a dot, append '1' to result
        result += '1'
        currentIndex += 2
    else:
        # Otherwise, append '2' to result
        result += '2'
        currentIndex += 2

# Output the value of result
print(result)

# End the program
