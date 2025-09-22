# Begin program

# Read input string from standard input
stringInput = input().strip()  # Remove whitespace from stringInput

# Initialize variables
currentIndex = 0
resultString = ''  # An empty string

# Process the input string
while currentIndex < len(stringInput):  # While currentIndex is less than the length of stringInput
    if stringInput[currentIndex] == '.':  # If character at currentIndex is '.'
        resultString += '0'  # Append '0' for a single dot
        currentIndex += 1  # Increment currentIndex by 1
    elif currentIndex + 1 < len(stringInput) and stringInput[currentIndex + 1] == '.':  # Check for two consecutive dots
        resultString += '1'  # Append '1' for two consecutive dots
        currentIndex += 2  # Increment currentIndex by 2
    else:  # Any other situation (dot followed by a different character)
        resultString += '2'  # Append '2' for any other two characters
        currentIndex += 2  # Increment currentIndex by 2

# Output the result
print(resultString)

# End program
