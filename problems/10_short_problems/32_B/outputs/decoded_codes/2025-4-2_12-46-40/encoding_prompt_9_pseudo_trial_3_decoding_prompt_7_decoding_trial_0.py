# Step 1: Initialize Input
inputString = input().strip()  # Read user input and remove any extra spaces

# Step 2: Setup Variables
index = 0  # To track the current position in the input string
outputString = ""  # To store the final result as a string

# Step 3: Process Input String
while index < len(inputString):  # Loop until we've processed the entire input string
    if inputString[index] == '.':  # Check if the current character is '.'
        outputString += '0'  # Add '0' to the output string
        index += 1  # Move to the next character
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':  # Check the next character
        outputString += '1'  # Add '1' to the output string
        index += 2  # Move two characters ahead
    else:  # If the conditions for '.' or '..' are not met
        outputString += '2'  # Add '2' to the output string
        index += 2  # Move two characters ahead

# Step 4: Output Result
print(outputString)  # Print the final converted numerical representation
