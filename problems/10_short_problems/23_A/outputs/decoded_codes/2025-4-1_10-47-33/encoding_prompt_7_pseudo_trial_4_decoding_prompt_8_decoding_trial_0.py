def findLongestRepeatedSubstring(inputString):
    lengthOfString = len(inputString)
    longestRepeatedSubstringLength = 0

    for substringLength in range(1, lengthOfString):  # Start from 1 to avoid empty substring
        for startIndex in range(0, lengthOfString - substringLength + 1):
            currentSubstring = inputString[startIndex:startIndex + substringLength]
            if currentSubstring in inputString[startIndex + 1:]:
                longestRepeatedSubstringLength = substringLength
                break  # Exit inner loop if a repeated substring is found

    return longestRepeatedSubstringLength

# Driver code
inputString = input().strip()  # Read input and remove trailing newline
print(findLongestRepeatedSubstring(inputString))
