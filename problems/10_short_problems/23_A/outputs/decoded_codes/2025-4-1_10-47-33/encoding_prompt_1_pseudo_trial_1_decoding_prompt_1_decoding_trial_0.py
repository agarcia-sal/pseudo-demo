# Step 1: Read a line of input and remove any trailing newline character.
input_line = input().strip()

# Step 2: Determine the length of the input line and store it in a variable called `lengthOfInput`.
lengthOfInput = len(input_line)

# Step 3: Initialize a variable `longestRepeatedSubstringLength` to 0.
longestRepeatedSubstringLength = 0

# Step 4: For each possible length `currentLength` from 0 to `lengthOfInput - 1`:
for currentLength in range(lengthOfInput):
    # Step 4a: For each position `startIndex` from 0 to `lengthOfInput - 1`:
    for startIndex in range(lengthOfInput):
        # Step 4ai: Extract a substring `currentSubstring` from the input line starting at `startIndex` with the length `currentLength`.
        currentSubstring = input_line[startIndex:startIndex + currentLength]
        
        # Step 4aii: Check if this `currentSubstring` appears again in the input line after the position `startIndex`.
        if currentSubstring and currentSubstring in input_line[startIndex + 1:]:
            # Step 4aiii: If `currentSubstring` is found at some position greater than `startIndex`:
            # Step 4aiv: Update `longestRepeatedSubstringLength` to `currentLength`.
            longestRepeatedSubstringLength = currentLength
            # Step 4av: Exit the inner loop to check the next `currentLength`.
            break

# Step 5: Print the value of `longestRepeatedSubstringLength` which represents the length of the longest repeated substring found in the input line.
print(longestRepeatedSubstringLength)
