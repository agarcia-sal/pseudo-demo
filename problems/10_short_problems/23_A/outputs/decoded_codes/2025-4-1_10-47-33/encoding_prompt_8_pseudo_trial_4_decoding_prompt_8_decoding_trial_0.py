# Step 1: Read input
inputLine = input().strip()

# Step 2: Initialize variables
lengthOfInput = len(inputLine)
maxLength = 0  # To track the length of the longest repeated substring

# Step 3: Check for repeated substrings
for currentLength in range(lengthOfInput):
    for startIndex in range(lengthOfInput):
        substring = inputLine[startIndex:startIndex + currentLength]
        
        # Step 6: Check if the substring appears again after its position
        if inputLine.find(substring, startIndex + 1) != -1:
            maxLength = currentLength  # Update maxLength
            break  # No need to check further for this substring length

# Step 7: Output the result
print(maxLength)
