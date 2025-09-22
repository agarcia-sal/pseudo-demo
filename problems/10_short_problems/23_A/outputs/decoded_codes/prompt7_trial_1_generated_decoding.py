def findLongestRepeatedSubstring(inputLine):
    # Get the length of the input string
    lengthOfInput = len(inputLine)
    # Initialize the length of the longest repeated substring found
    longestRepeatedSubstringLength = 0

    # Loop through all possible lengths of substrings
    for substringLength in range(1, lengthOfInput):
        # Check every starting position for this substring length
        for startingIndex in range(lengthOfInput - substringLength + 1):
            # Get the current substring from the input
            currentSubstring = inputLine[startingIndex:startingIndex + substringLength]
            
            # Check if the current substring exists again in inputLine
            if currentSubstring in inputLine[startingIndex + 1:]:
                # Update the longestRepeatedSubstringLength if a longer one is found
                longestRepeatedSubstringLength = substringLength
                # Break to avoid unnecessary checks once we've found a repeat
                break

    # Return the length of the longest repeated substring found
    return longestRepeatedSubstringLength

# Get user input
inputLine = input()
# Call the function and print the result
result = findLongestRepeatedSubstring(inputLine)
print(result)
