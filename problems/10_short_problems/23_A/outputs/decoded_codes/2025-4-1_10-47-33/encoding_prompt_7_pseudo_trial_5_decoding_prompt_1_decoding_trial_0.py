def findLongestRepeatedSubstring(inputString):
    lengthOfInput = len(inputString)
    longestRepeatLength = 0

    for substringLength in range(lengthOfInput):  # 0 to lengthOfInput - 1
        for startIndex in range(lengthOfInput):  # 0 to lengthOfInput - 1
            currentSubstring = inputString[startIndex:startIndex + substringLength]
            
            if currentSubstring in inputString[startIndex + 1:]:
                longestRepeatLength = substringLength
                break  # Break out of the inner loop
            
    return longestRepeatLength

# To execute the function:
line = input()[:-1]  # Read input without the last character
print(findLongestRepeatedSubstring(line))
