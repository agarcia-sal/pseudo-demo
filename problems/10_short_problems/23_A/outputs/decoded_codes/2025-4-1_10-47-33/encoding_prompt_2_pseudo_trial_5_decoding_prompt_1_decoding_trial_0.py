# Step 1: Start by reading a single line of input
inputString = input().strip()  # Remove the newline character at the end

# Step 2: Determine the length of inputString
lengthOfInputString = len(inputString)

# Step 3: Initialize the variable for longest repeated substring length
longestRepeatedSubstringLength = 0

# Step 4: Loop through each possible length of substrings
for currentLength in range(1, lengthOfInputString):  # Starting from 1 to lengthOfInputString - 1
    # Step 5: Loop through each substring starting position
    for startPosition in range(lengthOfInputString - currentLength + 1):  
        # Step 6: Extract the substring
        substring = inputString[startPosition:startPosition + currentLength]
        
        # Step 7: Check if this substring can be found within inputString
        if substring in inputString[startPosition + 1:]:  # Look for a repeated occurrence
            # Step 8: If the substring is found, update the longest length
            longestRepeatedSubstringLength = currentLength
            break  # Step 8 - break out of the inner loop

# Step 9: Continue with the outer loop until all lengths have been checked

# Step 10: Output the value of longestRepeatedSubstringLength
print(longestRepeatedSubstringLength)

# End of pseudocode
