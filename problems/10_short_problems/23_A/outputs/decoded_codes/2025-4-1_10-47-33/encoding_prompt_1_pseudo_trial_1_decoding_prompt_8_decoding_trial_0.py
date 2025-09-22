# Step 1: Read a line of input and remove any trailing newline character.
inputLine = input().strip()

# Step 2: Determine the length of the input line and store it in a variable called lengthOfInput.
lengthOfInput = len(inputLine)

# Step 3: Initialize a variable longestRepeatedSubstringLength to 0.
longestRepeatedSubstringLength = 0

# Step 4: For each possible length currentLength from 1 to lengthOfInput
for currentLength in range(1, lengthOfInput):
    # Step 4a: For each position startIndex from 0 to lengthOfInput - currentLength
    for startIndex in range(lengthOfInput - currentLength + 1):
        # Step 4ai: Extract a substring currentSubstring
        currentSubstring = inputLine[startIndex:startIndex + currentLength]
        
        # Step 4aii: Check if this currentSubstring appears again in the input line after the position startIndex
        if currentSubstring in inputLine[startIndex + currentLength:]:
            # Step 4aiii: If currentSubstring is found, update longestRepeatedSubstringLength
            longestRepeatedSubstringLength = currentLength
            break  # Exit the inner loop to check the next currentLength

# Step 5: Print the value of longestRepeatedSubstringLength
print(longestRepeatedSubstringLength)
