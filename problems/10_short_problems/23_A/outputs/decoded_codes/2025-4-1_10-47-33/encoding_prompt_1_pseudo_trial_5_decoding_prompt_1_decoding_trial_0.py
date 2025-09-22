# Step 1: Read Input
line = input().rstrip()  # Read a line of text input and remove trailing newline
lengthOfLine = len(line)  # Store the length of this line

# Step 2: Initialize Variables
maxRepeatedLength = 0  # Set maxRepeatedLength to 0

# Step 3: Outer Loop
for currentLength in range(lengthOfLine):  # For each currentLength from 0 to lengthOfLine - 1
    # Step 3: Inner Loop
    for startIndex in range(lengthOfLine):  # For each startIndex from 0 to lengthOfLine - 1
        substring = line[startIndex:startIndex + currentLength]  # Extract substring
        # Check if this substring appears again in line
        if (substring and 
            substring in line[startIndex + 1:]):  # Check if the substring is found again
            maxRepeatedLength = currentLength  # Update maxRepeatedLength
            break  # Break out of the inner loop since we found a repeat

# Step 4: Output Result
print(maxRepeatedLength)  # Print the length of the longest repeated substring
