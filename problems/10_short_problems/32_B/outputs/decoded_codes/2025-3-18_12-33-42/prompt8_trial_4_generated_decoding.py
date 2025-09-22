# Start Program
# Initialize program execution.

# Read Input
inputString = input().strip()

# Initialize Variables
index = 0
result = ""

# Process Input Characters
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

# Output the Result
print(result)
