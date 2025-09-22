def findLongestRepeatedSubstring(inputString):
    # Initialize the length of the input string
    stringLength = len(inputString)
    
    # Initialize the variable to store the length of the longest repeated substring
    longestRepeatedLength = 0

    # Loop over each possible length of the substring, starting from 1 to stringLength - 1
    for currentLength in range(1, stringLength):
        # Loop over each starting position of the substring
        for startingIndex in range(stringLength - currentLength): 
            # Get the current substring
            substring = inputString[startingIndex:startingIndex + currentLength]
            # Check if the substring exists again in the string after the current starting index
            if substring in inputString[startingIndex + 1:]:
                # Update longestRepeatedLength to currentLength if a repeated substring was found
                longestRepeatedLength = currentLength
                # Exit the inner loop once a repeated substring is found at this length
                break  # Break out of the inner loop

    # Return the length of the longest repeated substring found
    return longestRepeatedLength

# The expected input is a string read from standard input
inputString = input()
# Calling the function and printing the result
print(findLongestRepeatedSubstring(inputString))
