# Initialize Program
inputLine = input().strip()
length = len(inputLine)
result = 0

# Main Loop
for subLength in range(length):
    for startIndex in range(length):
        substring = inputLine[startIndex:startIndex + subLength]
        if inputLine.find(substring, startIndex + 1) != -1:
            result = subLength
            break  # Move to the next substring length

# Output the Result
print(result)
