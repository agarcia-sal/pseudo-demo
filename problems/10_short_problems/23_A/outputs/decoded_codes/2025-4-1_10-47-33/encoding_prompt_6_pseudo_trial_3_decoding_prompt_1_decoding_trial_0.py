# Read a line of input from the user
inputLine = input()

# Determine the length of the input line
lengthOfLine = len(inputLine)

# Initialize a variable to hold the result
longestRepeatedSubstringLength = 0

# Loop through possible substring lengths from 0 to lengthOfLine - 1
for substringLength in range(lengthOfLine):
    
    # Loop through each starting position in the input line
    for startIndex in range(lengthOfLine):
        
        # Extract a substring from the input line starting at startIndex with a given length
        currentSubstring = inputLine[startIndex:startIndex + substringLength]

        # Check if the current substring can be found elsewhere in the line after its starting position
        if currentSubstring in inputLine[startIndex + 1:]:
            
            # If found, update the longest repeated substring length
            longestRepeatedSubstringLength = substringLength
            break  # Stop checking other starting indices for this substring length

# Output the length of the longest repeated substring found
print(longestRepeatedSubstringLength)
