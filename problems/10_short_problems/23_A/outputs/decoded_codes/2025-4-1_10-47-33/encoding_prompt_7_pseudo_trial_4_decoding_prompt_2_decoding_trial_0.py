def findLongestRepeatedSubstring(inputString):
    lengthOfString = len(inputString)
    longestRepeatedSubstringLength = 0

    for substringLength in range(lengthOfString):  # Loop over possible substring lengths
        for startIndex in range(lengthOfString):   # Loop over possible starting indices
            currentSubstring = inputString[startIndex:startIndex + substringLength]  # Get the current substring
            
            # Check if the current substring appears again in the inputString after startIndex
            if inputString.find(currentSubstring, startIndex + 1) != -1:
                longestRepeatedSubstringLength = substringLength  # Update the length of the longest repeated substring
                break  # Exit the inner loop as we found a repeat

    return longestRepeatedSubstringLength  # Return the result


# Driver code
inputString = input().rstrip()  # Read input and remove any trailing newline or space
print(findLongestRepeatedSubstring(inputString))  # Output the result
