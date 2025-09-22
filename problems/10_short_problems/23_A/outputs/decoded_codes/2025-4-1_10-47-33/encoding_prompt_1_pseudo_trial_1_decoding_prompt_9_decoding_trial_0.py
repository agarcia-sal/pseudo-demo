# Read a line of input and remove any trailing newline character
input_line = input().strip()
lengthOfInput = len(input_line)  # Determine the length of the input line
longestRepeatedSubstringLength = 0  # Initialize variable to store the length of the longest repeated substring

# For each possible length of substring from 1 to lengthOfInput (0 would yield no substring)
for currentLength in range(1, lengthOfInput):
    # For each starting index for the substring
    for startIndex in range(lengthOfInput):
        # Extract the substring from the input line
        currentSubstring = input_line[startIndex:startIndex + currentLength]
        
        # Check if the substring appears again in the input line after the current start index
        if currentSubstring in input_line[startIndex + 1:]:
            longestRepeatedSubstringLength = currentLength  # Update the longest length found
            break  # Exit inner loop to check the next length

# Print the result - the length of the longest repeated substring found
print(longestRepeatedSubstringLength)
