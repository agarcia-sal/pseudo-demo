# Start Program

# Receive Input
line = input().rstrip()  # Read a line of text and remove trailing newline
lineLength = len(line)    # Store the length of the line

# Initialize Counter
longestRepeatedSubstringLength = 0  # Variable to keep track of the longest repeated substring length

# Iterate Over Possible Substring Lengths
for currentLength in range(1, lineLength):  # Iterating from 1 to lineLength - 1 (substrings of at least length 1)
    for startIndex in range(lineLength - currentLength + 1):  # Ensure we don't go out of bounds
        substring = line[startIndex:startIndex + currentLength]  # Extract substring
        # Check if this substring appears later in the line
        if substring in line[startIndex + currentLength:]:  # Check after the current starting position
            longestRepeatedSubstringLength = currentLength  # Update the longest length found
            break  # Exit the inner loop, as we found a repeat

# Output the Result
print(longestRepeatedSubstringLength)

# End Program
