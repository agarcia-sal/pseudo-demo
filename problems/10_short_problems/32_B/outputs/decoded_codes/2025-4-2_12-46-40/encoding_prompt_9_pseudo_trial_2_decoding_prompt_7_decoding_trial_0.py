# Start Program

# Receive Input:
input_string = input().strip()  # Read the input string and remove any unnecessary whitespace

# Initialize Variables:
currentIndex = 0  # To track the current position within the input string
outputString = ""  # To store the resulting numerical representation

# Process Input String:
while currentIndex < len(input_string):  # Continue until the end of the input string
    if input_string[currentIndex] == '.':  # Check if the current character is a dot
        outputString += '0'  # Append '0' to outputString
        currentIndex += 1  # Move to the next character
    elif currentIndex + 1 < len(input_string) and input_string[currentIndex + 1] == '.':
        outputString += '1'  # Current character is not a dot but next is a dot
        currentIndex += 2  # Move past the current and next character
    else:
        outputString += '2'  # Current character is not a dot, and next character is also not a dot
        currentIndex += 2  # Move past the current and next character

# Output Result:
print(outputString)  # Print the contents of outputString

# End Program
