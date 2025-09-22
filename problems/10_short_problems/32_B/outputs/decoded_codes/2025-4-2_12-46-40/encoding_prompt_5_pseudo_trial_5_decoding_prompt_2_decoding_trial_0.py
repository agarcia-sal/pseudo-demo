# Step 1: Receive Input
inputString = input().strip()  # Read input and remove surrounding spaces

# Step 2: Initialize Variables
index = 0
outputString = ""

# Step 3: Process Input String
while index < len(inputString):
    if inputString[index] == '.':
        outputString += '0'  # Append '0' for a single dot
        index += 1  # Move to the next character
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':
        outputString += '1'  # Append '1' for a pair of dots
        index += 2  # Move past this pair of dots
    else:
        outputString += '2'  # Append '2' for two non-dot characters
        index += 2  # Move past this pair of characters

# Step 4: Output Result
print(outputString)
