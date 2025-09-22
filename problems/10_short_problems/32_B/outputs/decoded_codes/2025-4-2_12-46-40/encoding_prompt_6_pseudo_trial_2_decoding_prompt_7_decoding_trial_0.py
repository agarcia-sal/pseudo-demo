# Start of the program

# Read input string from standard input
inputString = input()

# Initialize index to track the position in the input string
index = 0
# Initialize an empty string to build the output
outputString = ""

# Loop through the input string until we reach the end
while index < len(inputString):
    # Check if the current character is '.'
    if inputString[index] == '.':
        # If it's a single dot, append '0' to output
        outputString += '0'
        # Move to the next character
        index += 1
        
    # Check if the next character is also '.', forming the pattern ".."
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':
        # Append '1' to the output
        outputString += '1'
        # Move the index forward by two characters
        index += 2
        
    # Otherwise, handle the case of '.-' or other characters
    else:
        # Append '2' to the output for any other pattern
        outputString += '2'
        # Move the index forward by two characters
        index += 2

# Output the final result
print(outputString)

# End of the program
