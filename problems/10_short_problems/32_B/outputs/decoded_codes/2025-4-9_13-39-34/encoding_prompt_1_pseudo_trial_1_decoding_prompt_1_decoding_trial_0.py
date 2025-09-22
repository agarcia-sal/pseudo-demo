# 1. Start the program

# 2. Read a line of input from the user and remove any surrounding whitespace
inputString = input().strip()

# 3. Initialize a variable 'index' to 0 to track our position in 'inputString'
index = 0

# 4. Initialize an empty string 'result' to build the output
result = ""

# 5. While the 'index' is less than the length of 'inputString':
while index < len(inputString):
    # a. If the character at 'inputString[index]' is a dot ('.'):
    if inputString[index] == '.':
        # Append '0' to 'result'
        result += '0'
        # Increment 'index' by 1 (move to the next character)
        index += 1
    # b. Else if the character following 'inputString[index]' (that is, 'inputString[index + 1]') is a dot ('.'):
    elif index + 1 < len(inputString) and inputString[index + 1] == '.':
        # Append '1' to 'result'
        result += '1'
        # Increment 'index' by 2 (skip the next character as it is part of this pattern)
        index += 2
    # c. Else:
    else:
        # Append '2' to 'result' (indicating a different pattern)
        result += '2'
        # Increment 'index' by 2 (skip the next character as well)
        index += 2

# 6. After processing the input string, print the 'result'
print(result)

# 7. End the program
