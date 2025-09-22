def findLongestRepeatedSubstring(inputString):
    # Initialize the length of the input string
    stringLength = len(inputString)
    
    # Initialize the variable to store the length of the longest repeated substring
    longestRepeatedLength = 0
    
    # Loop over each possible length of substring, starting from 0 to stringLength - 1
    for currentLength in range(stringLength):
        # Loop over each starting position of the substring
        for startingIndex in range(stringLength):
            # Check if the substring exists again in the string after the current starting index
            if inputString[startingIndex:startingIndex + currentLength] in inputString[startingIndex + 1:]:
                # Update longestRepeatedLength to currentLength, indicating a repeated substring was found
                longestRepeatedLength = currentLength
                # Exit the inner loop once a repeated substring is found at this length
                break
    
    # Return the length of the longest repeated substring found
    return longestRepeatedLength

# The expected input is a string from standard input (stdin)
# The expected output is the length of the longest repeated substring in that input string
