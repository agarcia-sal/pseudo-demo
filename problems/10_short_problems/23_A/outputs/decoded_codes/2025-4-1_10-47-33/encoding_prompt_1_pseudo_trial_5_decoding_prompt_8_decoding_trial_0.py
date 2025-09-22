# Read Input
line = input().strip()
lengthOfLine = len(line)

# Initialize Variables
maxRepeatedLength = 0

# Outer Loop
for currentLength in range(1, lengthOfLine):
    foundRepeat = False
    # Inner Loop
    for startIndex in range(lengthOfLine - currentLength):
        substring = line[startIndex:startIndex + currentLength]
        # Check if this substring appears again in line
        if substring in line[startIndex + 1:]:
            maxRepeatedLength = currentLength
            foundRepeat = True
            break
    if foundRepeat:
        # Break outer loop if a repeat was found
        continue

# Output Result
print(maxRepeatedLength)


def find_max_repeated_length(line):
    line = line.strip()
    lengthOfLine = len(line)
    maxRepeatedLength = 0

    for currentLength in range(1, lengthOfLine):
        foundRepeat = False
        for startIndex in range(lengthOfLine - currentLength):
            substring = line[startIndex:startIndex + currentLength]
            if substring in line[startIndex + 1:]:
                maxRepeatedLength = currentLength
                foundRepeat = True
                break
        if foundRepeat:
            continue

    return maxRepeatedLength

# Read Input
line = input()
# Output Result
print(find_max_repeated_length(line))
