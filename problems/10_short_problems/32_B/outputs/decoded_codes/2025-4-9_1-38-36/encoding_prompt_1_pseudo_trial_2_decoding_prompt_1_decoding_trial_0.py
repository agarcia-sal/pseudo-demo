# Step 1: Read Input
inputString = input().strip()

# Step 2: Initialize Variables
index = 0
result = ""

# Step 3: Process Input String
while index < len(inputString):
    if inputString[index] == '.':
        result += '0'
        index += 1
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':
        result += '1'
        index += 2
    else:
        result += '2'
        index += 2

# Step 4: Output Result
print(result)
