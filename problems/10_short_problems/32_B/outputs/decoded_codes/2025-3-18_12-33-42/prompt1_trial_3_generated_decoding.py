# Step 1: Read Input
inputString = input().strip()

# Step 2: Initialize Variables
index = 0
result = ""

# Step 3: Process the Input String
while index < len(inputString):
    if inputString[index] == '.':
        result += '0'
        index += 1  # Move to the next character
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':
        result += '1'
        index += 2  # Skip the next character
    else:
        result += '2'
        index += 2  # Skip the next character

# Step 4: Output Result
print(result)
