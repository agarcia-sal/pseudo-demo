# BEGIN

# Read a line of input and remove any whitespace
inputString = input().strip()

# Initialize index and result string
index = 0
result = ''

# Loop until the end of the input string is reached
while index < len(inputString):

    # Check if the current character is a single dot
    if inputString[index] == '.':
        result += '0'
        index += 1
    else:
        # Check the next character to determine the value to append
        if index + 1 < len(inputString) and inputString[index + 1] == '.':
            result += '1'
            index += 2
        else:
            result += '2'
            index += 2

# Output the final result
print(result)

# END
