# Step 1: Receive Input
inputLine = input()
inputLine = inputLine[:-1]  # Remove the last character (newline)

# Step 2: Initialize Variables
lengthOfLine = len(inputLine)
resultValue = 0

# Step 3: Loop through PossibleSubstringLengths
for currentLength in range(lengthOfLine):
    for currentIndex in range(lengthOfLine):
        if currentIndex + currentLength < lengthOfLine:  # Ensure substring does not exceed bounds
            substring = inputLine[currentIndex:currentIndex + currentLength + 1]
            # Step 4: Check for Substring Reoccurrence
            if substring in inputLine[currentIndex + 1:]:
                resultValue = currentLength + 1  # Update with length of found substring
                break  # Exit inner loop if a repeating substring is found

# Step 5: Output the Result
print(resultValue)
