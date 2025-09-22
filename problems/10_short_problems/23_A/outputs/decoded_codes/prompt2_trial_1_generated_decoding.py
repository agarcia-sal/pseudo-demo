# Step 1: Receive Input
input_line = input().strip()  # Read a line of text and remove the trailing newline
lengthOfLine = len(input_line)  # Determine the length of the input line
resultValue = 0  # Initialize resultValue to zero

# Step 2: Iterate Over Lengths
for currentLength in range(1, lengthOfLine):  # currentLength starts from 1 to lengthOfLine - 1
    for currentIndex in range(lengthOfLine):  # Iterate over each index in the input line
        # Extract a substring starting at currentIndex with length currentLength
        substring = input_line[currentIndex:currentIndex + currentLength]
        
        # Check if this substring appears again in the input line after currentIndex
        if input_line.find(substring, currentIndex + 1) != -1:
            # If found, update resultValue with currentLength
            resultValue = currentLength
            break  # Break out of the inner loop since we found a repeating substring

# Step 3: Output Result
print(resultValue)  # Print the length of the longest repeating substring
