# 1. Start the program
# (No explicit action needed)

# 2. Read a line of input from standard input and remove leading/trailing whitespace
inputString = input().strip()

# 3. Initialize the index variable
currentIndex = 0

# 4. Initialize an empty string variable
result = ""

# 5. While the currentIndex is less than the length of inputString
while currentIndex < len(inputString):
    # If character at currentIndex is a dot
    if inputString[currentIndex] == '.':
        # Append '0' to result
        result += '0'
        # Increment currentIndex by 1
        currentIndex += 1
    # Else If character at currentIndex + 1 is a dot
    elif currentIndex + 1 < len(inputString) and inputString[currentIndex + 1] == '.':
        # Append '1' to result
        result += '1'
        # Increment currentIndex by 2
        currentIndex += 2
    # Else
    else:
        # Append '2' to result
        result += '2'
        # Increment currentIndex by 2
        currentIndex += 2

# 6. Output the value of result
print(result)

# 7. End the program
# (No explicit action needed)
