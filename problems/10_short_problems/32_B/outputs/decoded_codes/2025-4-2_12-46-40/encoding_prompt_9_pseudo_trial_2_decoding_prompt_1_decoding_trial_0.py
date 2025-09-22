# Start Program

# Receive Input:
input_string = input().strip()  # Read the input string from the user, removing whitespace

# Initialize Variables:
currentIndex = 0  # Integer to track position in input string
outputString = ""  # String to store resulting numerical representation

# Process Input String:
while currentIndex < len(input_string):  # While currentIndex is less than the length of the input string
    if input_string[currentIndex] == '.':  # If the character at currentIndex is a dot
        outputString += '0'  # Append '0' to outputString
        currentIndex += 1  # Increment currentIndex by 1
    elif currentIndex + 1 < len(input_string) and input_string[currentIndex + 1] == '.':  # If the next character is a dot
        outputString += '1'  # Append '1' to outputString
        currentIndex += 2  # Increment currentIndex by 2
    else:  # The current character is not a dot and the next character is not a dot
        outputString += '2'  # Append '2' to outputString
        currentIndex += 2  # Increment currentIndex by 2

# Output Result:
print(outputString)  # Print the contents of outputString

# End Program
