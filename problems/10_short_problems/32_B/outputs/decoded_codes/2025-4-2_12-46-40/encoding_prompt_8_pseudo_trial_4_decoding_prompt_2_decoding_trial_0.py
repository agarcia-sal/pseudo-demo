# Read Input
input_string = input().strip()

# Initialize Variables
currentPosition = 0
result = ""

# Process the Input
while currentPosition < len(input_string):
    if input_string[currentPosition] == '.':
        result += '0'
        currentPosition += 1
    else:
        if currentPosition + 1 < len(input_string) and input_string[currentPosition + 1] == '.':
            result += '1'
            currentPosition += 2
        else:
            result += '2'
            currentPosition += 2

# Output the Result
print(result)
