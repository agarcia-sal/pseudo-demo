# Step 1: Initialize Input
inputString = input().strip()  # Read input and remove extra spaces

# Step 2: Setup Variables
index = 0  # Initialize index to 0
outputString = ""  # Create an empty string for output

# Step 3: Process Input String
while index < len(inputString):  # Loop until the end of the input string
    if inputString[index] == '.':  # Check if the character at index is '.'
        outputString += '0'  # Add '0' to outputString
        index += 1  # Increment index by 1
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':  # Check for '.'
        outputString += '1'  # Add '1' to outputString
        index += 2  # Increment index by 2
    else:  # If neither condition is met
        outputString += '2'  # Add '2' to outputString
        index += 2  # Increment index by 2

# Step 4: Output Result
print(outputString)  # Print the final output
