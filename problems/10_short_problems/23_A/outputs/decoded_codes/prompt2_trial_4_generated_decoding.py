# Step 1: Input
inputLine = input().rstrip('\n')

# Step 2: Determine the length
lengthOfLine = len(inputLine)

# Step 3: Initialize result variable
longestRepeatedSubstringLength = 0

# Step 4: Outer loop
for currentLength in range(1, lengthOfLine):  # Changed to 1 to avoid empty substring
    # Step 4.1: Inner loop
    for startingIndex in range(lengthOfLine - currentLength + 1):  # Adjust to avoid out of bounds
        # Step 4.2: Check for repetition
        substring = inputLine[startingIndex:startingIndex + currentLength]
        # Check for the substring in the remaining part of inputLine
        if inputLine.find(substring, startingIndex + 1) != -1:  # Find after the current starting index
            # Step 4.3: Update the result
            longestRepeatedSubstringLength = currentLength
            break  # Exit the inner loop early

# Step 5: Output
print(longestRepeatedSubstringLength)
