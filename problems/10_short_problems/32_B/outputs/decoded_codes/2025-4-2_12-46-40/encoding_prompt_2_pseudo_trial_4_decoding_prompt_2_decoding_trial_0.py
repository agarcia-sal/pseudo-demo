# Step 1: Read input and trim whitespace
input_string = input().strip()

# Step 2: Initialization
currentIndex = 0
outputString = ""

# Step 3: Process Loop
while currentIndex < len(input_string):
    if input_string[currentIndex] == '.':
        # If the current character is a dot
        outputString += '0'
        currentIndex += 1  # Move to the next character
    else:
        # Check the next character
        if currentIndex + 1 < len(input_string) and input_string[currentIndex + 1] == '.':
            # If the next character is a dot
            outputString += '1'
            currentIndex += 2  # Move to the next two characters
        else:
            # If the next character is not a dot
            outputString += '2'
            currentIndex += 2  # Move to the next two characters

# Step 4: Output
print(outputString)
