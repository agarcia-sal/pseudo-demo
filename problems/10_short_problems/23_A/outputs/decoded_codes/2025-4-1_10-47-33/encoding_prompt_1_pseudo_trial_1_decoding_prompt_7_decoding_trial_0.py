# Step 1: Read a line of input and remove any trailing newline character.
input_line = input().strip()

# Step 2: Determine the length of the input line 
lengthOfInput = len(input_line)

# Step 3: Initialize the longest repeated substring length to 0.
longestRepeatedSubstringLength = 0

# Step 4: For each possible length of substring from 0 to lengthOfInput - 1
for currentLength in range(lengthOfInput):
    # Step 4a: For each starting position from 0 to lengthOfInput - 1
    for startIndex in range(lengthOfInput):
        # Step 4i: Extract the current substring
        currentSubstring = input_line[startIndex:startIndex + currentLength]

        # Only check if the substring length is valid
        if len(currentSubstring) == currentLength:
            # Step 4ii: Check for occurrence of currentSubstring after startIndex
            if input_line.find(currentSubstring, startIndex + 1) != -1:
                # Step 4iii: Update the longestRepeatedSubstringLength
                longestRepeatedSubstringLength = currentLength
                # Exit the inner loop to check the next currentLength
                break

# Step 5: Output the length of the longest repeated substring
print(longestRepeatedSubstringLength)
