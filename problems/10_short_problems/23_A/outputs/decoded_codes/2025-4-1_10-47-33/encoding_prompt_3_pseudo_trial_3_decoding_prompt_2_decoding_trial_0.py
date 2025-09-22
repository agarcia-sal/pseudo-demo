# Begin

# Read a line of input from standard input
stringInput = input()

# Determine the length of the input string
stringLength = len(stringInput)

# Initialize variable to hold the result
longestRepeatedSubstringLength = 0

# Loop through lengths of potential substrings from 0 to stringLength - 1
for lengthFromZero in range(stringLength):  # from 0 to stringLength - 1
    
    # Loop through each starting index for the substrings
    for startIndex in range(stringLength):  # from 0 to stringLength - 1
        
        # Extract the substring from startIndex of the current length
        currentSubstring = stringInput[startIndex:startIndex + lengthFromZero]
        
        # Check if the current substring can be found in the remainder of the string
        if currentSubstring in stringInput[startIndex + 1:]:  # search in the rest of the string
            # If found, update the result to the current length
            longestRepeatedSubstringLength = lengthFromZero
            
            # Exit the loop since we found a repeated substring of this length
            break  # break out of the inner loop

    # The outer loop will continue to check for longer substring lengths

# Output the length of the longest repeated substring found
print(longestRepeatedSubstringLength)

# End
