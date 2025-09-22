# Step 1: Input
inputString = input().strip()  # Read input and remove leading/trailing whitespace

# Step 2: Initialize Variables
index = 0  # Initialize the index to track the position in the input string
outputString = ""  # Create an empty string to store the result

# Step 3: Process the Input
while index < len(inputString):  # Loop while index is within the length of inputString
    if inputString[index] == '.':  # Check if the current character is a dot
        outputString += '0'  # Append '0' to outputString
        index += 1  # Move index forward by 1 to check the next character
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':  # Check next character for a dot
        outputString += '1'  # Append '1' to outputString
        index += 2  # Move index forward by 2 to skip both current and next character
    else:  # If neither condition is met
        outputString += '2'  # Append '2' to outputString
        index += 2  # Move index forward by 2 to skip both current and next character

# Step 4: Output
print(outputString)  # Print the content of outputString
