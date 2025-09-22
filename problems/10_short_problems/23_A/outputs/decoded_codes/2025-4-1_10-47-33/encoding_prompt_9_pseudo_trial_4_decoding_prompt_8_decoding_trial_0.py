# Start Program

# Receive Input
line = input().strip()
lineLength = len(line)

# Initialize Counter
longestRepeatedSubstringLength = 0

# Iterate Over Possible Substring Lengths
for currentLength in range(1, lineLength):  # Start from 1 to avoid empty substring
    for startIndex in range(lineLength - currentLength):
        substring = line[startIndex:startIndex + currentLength]
        # Check if this substring appears later in the line
        if substring in line[startIndex + currentLength:]:
            longestRepeatedSubstringLength = currentLength
            break  # Found a repeated substring of this length, no need to check further

# Output the Result
print(longestRepeatedSubstringLength)

# End Program
