# 1. Read Input
line = input().rstrip()  # Reads a line of text and removes the trailing newline character.
lengthOfLine = len(line)  # Store the length of the line.

# 2. Initialize Variables
maxRepeatedLength = 0  # Set the initial maximum repeated length to 0.

# 3. Outer Loop
for currentLength in range(lengthOfLine):  # Loop from 0 to lengthOfLine - 1
    # 3.1 Inner Loop
    for startIndex in range(lengthOfLine):  # Loop over starting indices
        # Extract the substring
        substring = line[startIndex:startIndex + currentLength]
        
        # Check if the substring appears again in the line
        if startIndex + 1 < lengthOfLine and substring in line[startIndex + 1:]:
            maxRepeatedLength = currentLength  # Update maxRepeatedLength
            break  # Break out of the inner loop since we found a repeat.

# 4. Output Result
print(maxRepeatedLength)  # Print the length of the longest repeated substring.
