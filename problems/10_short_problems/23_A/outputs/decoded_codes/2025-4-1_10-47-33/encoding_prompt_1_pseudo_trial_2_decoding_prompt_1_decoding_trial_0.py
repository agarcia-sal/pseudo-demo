# Step 1: Read a line of input and remove the trailing newline character.
input_line = input().strip()

# Step 2: Determine the length of the input line and store it in a variable `lengthOfLine`.
lengthOfLine = len(input_line)

# Step 3: Initialize a variable `repeatedSubstringLength` to 0.
repeatedSubstringLength = 0

# Step 4: For each possible length `substringLength` from 0 to `lengthOfLine - 1`:
for substringLength in range(lengthOfLine):
    # For each starting index `startIndex` from 0 to `lengthOfLine - 1`:
    for startIndex in range(lengthOfLine):
        # Extract a substring from the input line starting at `startIndex` and of length `substringLength`.
        substring = input_line[startIndex:startIndex + substringLength]
        
        # Check if this substring can be found again later in the input line.
        if substring in input_line[startIndex + substringLength:]:
            # If the substring is found again:
            repeatedSubstringLength = substringLength
            
            # Exit the inner loop (since we found a repeated substring of the current length).
            break

# Step 5: Output the value of `repeatedSubstringLength`.
print(repeatedSubstringLength)
