def findLongestRepeatedSubstring(inputString):
    lengthOfString = len(inputString)
    longestRepeatedSubstringLength = 0

    for substringLength in range(lengthOfString):
        for startIndex in range(lengthOfString):
            currentSubstring = inputString[startIndex:startIndex + substringLength]
            if inputString.find(currentSubstring, startIndex + 1) != -1:
                longestRepeatedSubstringLength = substringLength
                break  # breaks the inner loop
        # The outer loop continues regardless of inner loop break

    return longestRepeatedSubstringLength

# Driver code
inputString = input()
print(findLongestRepeatedSubstring(inputString))
