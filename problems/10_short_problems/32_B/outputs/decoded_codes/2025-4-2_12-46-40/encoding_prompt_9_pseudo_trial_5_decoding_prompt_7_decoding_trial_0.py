# 1. Receive Input
inputString = input().strip()  # Read input and remove surrounding whitespace

# 2. Initialize Variables
index = 0  # Tracker for the current position in the input string
outputString = ""  # To store the resulting numeric representation

# 3. Process the Input String
while index < len(inputString):  # Loop through the input string while the index is valid
    if inputString[index] == '.':  # Check if the current character is a dot
        outputString += '0'  # Append '0' to outputString
        index += 1  # Move to the next character
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':  # Check the next character
        outputString += '1'  # Append '1' to outputString
        index += 2  # Skip to the character after the next
    else:  # Else, if it's a character that is not a dot or we have a single character
        outputString += '2'  # Append '2' to outputString
        index += 2  # Skip to the character after the next

# 4. Output the Result
print(outputString)  # Print the converted numeric representation
