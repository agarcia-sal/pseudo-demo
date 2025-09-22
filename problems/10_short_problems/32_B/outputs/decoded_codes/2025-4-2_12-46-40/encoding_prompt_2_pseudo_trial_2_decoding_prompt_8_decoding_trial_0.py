# Step 1: Read input
input_string = input()

# Step 2: Initialize Variables
currentIndex = 0
outputString = ""

# Step 3: Processing Loop
while currentIndex < len(input_string):
    if input_string[currentIndex] == '.':
        outputString += '0'
        currentIndex += 1
    elif (currentIndex + 1 < len(input_string)) and (input_string[currentIndex + 1] == '.'):
        outputString += '1'
        currentIndex += 2
    else:
        outputString += '2'
        currentIndex += 2

# Step 4: Output the result
print(outputString)


def process_encoded_string(input_string):
    currentIndex = 0
    outputString = ""

    while currentIndex < len(input_string):
        if input_string[currentIndex] == '.':
            outputString += '0'
            currentIndex += 1
        elif (currentIndex + 1 < len(input_string)) and (input_string[currentIndex + 1] == '.'):
            outputString += '1'
            currentIndex += 2
        else:
            outputString += '2'
            currentIndex += 2

    return outputString

# Main Execution
input_string = input()
print(process_encoded_string(input_string))
