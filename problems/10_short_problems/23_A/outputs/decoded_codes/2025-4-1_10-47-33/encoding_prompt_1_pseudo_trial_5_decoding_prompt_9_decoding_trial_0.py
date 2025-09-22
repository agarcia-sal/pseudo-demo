# Read the input line and remove trailing newline character
line = input().strip()
lengthOfLine = len(line)

# Initialize variable to store the maximum length of repeated substring
maxRepeatedLength = 0

# Outer loop for current substring lengths
for currentLength in range(1, lengthOfLine):  # Start from 1 to ignore empty substring
    # Inner loop for starting index of the substring
    for startIndex in range(lengthOfLine - currentLength + 1):  # Adjust range to avoid overflow
        # Extract the substring
        substring = line[startIndex:startIndex + currentLength]
        # Check if this substring appears again in the line
        if substring in line[startIndex + currentLength:]:  # Search in the remaining part of the line
            maxRepeatedLength = currentLength  # Update maximum length of repeated substring
            break  # Break out of inner loop as we found a repeat

# Output the result, the length of the longest repeated substring
print(maxRepeatedLength)
