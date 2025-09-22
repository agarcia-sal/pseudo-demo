def findLongestRepeatedSubstring(inputString):
    lengthOfInput = len(inputString)
    longestRepeatLength = 0

    for substringLength in range(lengthOfInput):
        for startIndex in range(lengthOfInput):
            currentSubstring = inputString[startIndex:startIndex + substringLength]

            if currentSubstring in inputString[startIndex + 1:]:
                longestRepeatLength = substringLength
                break

    return longestRepeatLength

# To execute the function:
line = input()[:-1]
print(findLongestRepeatedSubstring(line))
