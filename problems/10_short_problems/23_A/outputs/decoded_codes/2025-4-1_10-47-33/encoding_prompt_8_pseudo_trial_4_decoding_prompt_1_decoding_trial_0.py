# Step 1: Read input
inputLine = input()

# Step 2: Initialize variables
lengthOfInput = len(inputLine)
maxLength = 0  # To track the length of the longest repeated substring

# Step 3: Check for repeated substrings
for currentLength in range(lengthOfInput):  # currentLength from 0 to lengthOfInput - 1
    for startIndex in range(lengthOfInput):  # startIndex from 0 to lengthOfInput - 1
        substring = inputLine[startIndex:startIndex + currentLength]  # Extract substring
        
        # Step 6: Check if the substring appears again after its position
        if inputLine.find(substring, startIndex + 1) != -1:  # Check if found after startIndex
            maxLength = currentLength  # Update maxLength
            break  # No need to check further within this inner loop

# Step 7: Output the result
print(maxLength)
