# Step 1: Read a line of input and remove the trailing newline character
input_line = input().strip()

# Step 2: Determine the length of the input line
lengthOfLine = len(input_line)

# Step 3: Initialize the variable for longest repeated substring length
repeatedSubstringLength = 0

# Step 4: Loop through all possible lengths of substrings
for substringLength in range(lengthOfLine):  # Loop from 0 to lengthOfLine - 1
    # Loop through each possible starting index
    for startIndex in range(lengthOfLine - substringLength):  # Ensure we don't go out of bounds
        # Extract the substring
        substring = input_line[startIndex:startIndex + substringLength]
        
        # Check if the substring exists again in the remaining part of the input_line
        if substring in input_line[startIndex + 1:]:  # Look from the next character onwards
            # Update the repeated substring length
            repeatedSubstringLength = substringLength
            
            # Exit the loop as we found a repeated substring of the current length
            break

# Step 5: Output the length of the longest repeated substring
print(repeatedSubstringLength)
