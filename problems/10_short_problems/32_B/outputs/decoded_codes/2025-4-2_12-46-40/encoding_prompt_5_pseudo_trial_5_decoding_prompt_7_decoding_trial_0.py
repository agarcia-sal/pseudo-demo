# Step 1: Receive Input
inputString = input().strip()  # Read input and remove surrounding spaces

# Step 2: Initialize Variables
index = 0  # To track the current position in the input string
outputString = ""  # To store the decoded result

# Step 3: Process Input String
while index < len(inputString):  # Continue until the end of the string
    if inputString[index] == '.':  # Check if the current character is a dot
        outputString += '0'  # Append '0' to outputString
        index += 1  # Move to the next character
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':  # Check next character
        outputString += '1'  # Append '1' to outputString
        index += 2  # Move past this pair of characters
    else:
        outputString += '2'  # Append '2' to outputString for other characters
        index += 2  # Move past this pair of characters

# Step 4: Output Result
print(outputString)  # Print the final decoded output
