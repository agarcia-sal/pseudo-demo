# Read a line of input from standard input and remove the last character
stringLine = input()[:-1]
lengthOfString = len(stringLine)
longestRepeatedSubstringLength = 0

# Iterate over possible lengths of substrings
for substringLength in range(lengthOfString):
    
    # Check for each starting position of the string
    for startingIndex in range(lengthOfString):
        
        # Create a substring of the current length starting from startingIndex
        currentSubstring = stringLine[startingIndex:startingIndex + substringLength]
        
        # Check if the current substring appears again in the string
        if currentSubstring in stringLine[startingIndex + 1:]:
            
            # Update the longest repeated substring length
            longestRepeatedSubstringLength = substringLength
            break  # Break out of inner loop
        
# Output the longest length of the repeated substring found
print(longestRepeatedSubstringLength)
