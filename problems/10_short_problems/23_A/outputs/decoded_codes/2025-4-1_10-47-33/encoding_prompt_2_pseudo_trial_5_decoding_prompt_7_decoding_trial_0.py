# Step 1: Read the input string
inputString = input().strip()  # Removing the newline character

# Step 2: Determine the length of inputString
lengthOfInputString = len(inputString)

# Step 3: Initialize the variable for longest repeated substring length
longestRepeatedSubstringLength = 0

# Step 4: Loop through each possible length of substrings
for currentLength in range(1, lengthOfInputString): # Starting from length 1 to length-1
    # Step 5: Loop through each starting position for substrings
    for startPosition in range(lengthOfInputString - currentLength + 1):
        # Step 6: Extract the substring
        substring = inputString[startPosition:startPosition + currentLength]

        # Step 7: Check for repeated occurrence
        if substring in inputString[startPosition + 1:]:  # Check in the remaining part of the string
            # Step 8: Update longest repeated substring length
            longestRepeatedSubstringLength = currentLength
            break  # Break out of the inner loop once found

# Step 10: Output the result
print(longestRepeatedSubstringLength)

