# Step 1: Read input
input_string = input().strip()

# Step 2: Initialization
currentIndex = 0
outputString = ""

# Step 3: Process Loop
while currentIndex < len(input_string):
    if input_string[currentIndex] == '.':
        outputString += '0'
        currentIndex += 1
    else:
        if currentIndex + 1 < len(input_string) and input_string[currentIndex + 1] == '.':
            outputString += '1'
            currentIndex += 2
        else:
            outputString += '2'
            currentIndex += 2

# Step 4: Output
print(outputString)
