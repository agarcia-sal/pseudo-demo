# Step 1: Read input
inputString = input().strip()

# Step 2: Determine the length of inputString
lengthOfInputString = len(inputString)

# Step 3: Initialize longestRepeatedSubstringLength
longestRepeatedSubstringLength = 0

# Step 4: Loop through each possible length of substrings
for currentLength in range(1, lengthOfInputString):  # start from 1 to avoid empty substring
    # Step 5: Loop through each substring starting position
    for startPosition in range(lengthOfInputString - currentLength + 1):
        # Step 6: Extract the substring
        substring = inputString[startPosition:startPosition + currentLength]
        
        # Step 7: Check if this substring exists from startPosition + 1
        if substring in inputString[startPosition + 1:]:
            # Step 8: Update longestRepeatedSubstringLength
            longestRepeatedSubstringLength = currentLength
            break  # Exit inner loop once a repeating substring is found

# Step 10: Output the result
print(longestRepeatedSubstringLength)
