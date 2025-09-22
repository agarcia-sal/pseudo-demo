# 1. Start the Program

# 2. Read Input:
inputString = input().strip()

# 3. Initialize Variables:
index = 0
result = ""

# 4. Process the Input String:
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

# 5. Output the Result:
print(result)

# 6. End of Program
