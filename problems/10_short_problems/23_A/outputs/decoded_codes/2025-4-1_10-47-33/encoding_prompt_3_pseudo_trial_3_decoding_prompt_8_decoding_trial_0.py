# Read a line of input from standard input and remove the last character (newline)
stringInput = input().strip()

# Determine the length of the input string
stringLength = len(stringInput)

# Initialize variable to hold the result
longestRepeatedSubstringLength = 0

# Loop through lengths of potential substrings from 0 to stringLength - 1
for lengthFromZero in range(stringLength):
    
    # Loop through each starting index for the substrings
    for startIndex in range(stringLength):
        
        # Extract the substring from startIndex of the current length
        currentSubstring = stringInput[startIndex:startIndex + lengthFromZero + 1]
        
        # Check if the current substring can be found in the remainder of the string
        if currentSubstring in stringInput[startIndex + 1:]:
            
            # If found, update the result to the current length
            longestRepeatedSubstringLength = lengthFromZero + 1
            
            # Exit the loop since we found a repeated substring of this length
            break

# Output the length of the longest repeated substring found
print(longestRepeatedSubstringLength)
