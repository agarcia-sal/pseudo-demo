# Read Input
line = input()
line = line[:-1]  # Remove the last character (new line)
lengthOfLine = len(line)

# Initialize Variables
longestRepeatLength = 0

# Outer Loop
for currentLength in range(1, lengthOfLine):  # start from 1 to avoid empty substrings
    # Inner Loop
    for startIndex in range(lengthOfLine - currentLength):  # Adjust end index to avoid overflow
        # Check for Repetition
        substring = line[startIndex:startIndex + currentLength]
        if line.find(substring, startIndex + 1) != -1:  # Check after current startIndex
            longestRepeatLength = currentLength
            break  # No need to continue checking further for this length

# Output the Result
print(longestRepeatLength)
