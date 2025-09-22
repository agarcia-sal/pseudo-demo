# Start Program

# Receive Input
line = input().rstrip()  # Read a line of text and remove trailing newline
lineLength = len(line)   # Store the length of the line

# Initialize Counter
longestRepeatedSubstringLength = 0  # Keep track of longest repeated substring length

# Iterate Over Possible Substring Lengths
for currentLength in range(1, lineLength):  # Start from 1 as length 0 has no substrings
    # Inner Loop: For each starting position
    for startIndex in range(0, lineLength - currentLength + 1):
        # Extract the substring
        substring = line[startIndex:startIndex + currentLength]
        
        # Check for the existence of the substring later in the line
        if substring in line[startIndex + currentLength:]:
            # If found, update the longest length
            longestRepeatedSubstringLength = currentLength
            break  # Break out of the inner loop

# Output the Result
print(longestRepeatedSubstringLength)

# End Program
