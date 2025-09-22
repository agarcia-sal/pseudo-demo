# Read the input string from standard input
inputString = input()

# Initialize a variable to keep track of the current position in the string
currentIndex = 0

# Initialize an empty string to hold the output result
outputResult = ''

# Loop through the entire input string until the end is reached
while currentIndex < len(inputString):

    # Check if the current character is a period
    if inputString[currentIndex] == '.':
        # Append '0' to the output result for a single period
        outputResult += '0'
        # Move to the next character
        currentIndex += 1
        
    # Check for a pair of periods
    elif currentIndex + 1 < len(inputString) and inputString[currentIndex + 1] == '.':
        # Append '1' to the output result for two periods
        outputResult += '1'
        # Move past these two characters
        currentIndex += 2
        
    # Handle the case for a period followed by a dash (assumed)
    else:
        # Append '2' to the output result for a period followed by a dash
        outputResult += '2'
        # Move past these two characters
        currentIndex += 2

# Print the resulting output string
print(outputResult)
