# Read Input
inputString = input().strip()  # Read a line of input and remove leading/trailing spaces

# Initialize Variables
index = 0  # Set the counter to 0
result = ""  # Create an empty result string

# Process the Input String
while index < len(inputString):  # Continue while index is less than the length of inputString
    if inputString[index] == '.':  # Check if the current character is a dot
        result += '0'  # Append '0' to result
        index += 1  # Increment index by 1
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':  # Check next character if it exists and is a dot
        result += '1'  # Append '1' to result
        index += 2  # Increment index by 2 to skip the next character
    else:  # Any other combination
        result += '2'  # Append '2' to result
        index += 2  # Increment index by 2 to skip to the character after the next

# Output Result
print(result)  # Print the final result
