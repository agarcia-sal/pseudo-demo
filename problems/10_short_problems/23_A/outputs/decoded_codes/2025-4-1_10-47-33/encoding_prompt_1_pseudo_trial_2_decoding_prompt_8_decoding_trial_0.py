# Step 1: Read a line of input and remove the trailing newline character.
input_line = input().strip()

# Step 2: Determine the length of the input line and store it in a variable `lengthOfLine`.
lengthOfLine = len(input_line)

# Step 3: Initialize a variable `repeatedSubstringLength` to 0.
repeatedSubstringLength = 0

# Step 4: For each possible length `substringLength` from 1 to `lengthOfLine - 1`
for substringLength in range(1, lengthOfLine):
    # For each starting index `startIndex` from 0 to `lengthOfLine - substringLength`
    for startIndex in range(lengthOfLine - substringLength + 1):
        # Extract a substring from the input line starting at `startIndex` and of length `substringLength`.
        substring = input_line[startIndex:startIndex + substringLength]
        
        # Check if this substring can be found again later in the input line
        if substring in input_line[startIndex + substringLength:]:
            # If the substring is found again:
            repeatedSubstringLength = substringLength
            break  # Exit the inner loop

# Step 5: Output the value of `repeatedSubstringLength`.
print(repeatedSubstringLength)
