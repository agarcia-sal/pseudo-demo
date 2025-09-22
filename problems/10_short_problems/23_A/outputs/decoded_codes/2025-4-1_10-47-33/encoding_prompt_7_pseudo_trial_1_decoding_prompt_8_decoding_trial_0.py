def findLongestRepeatedSubstring(inputString):
    stringLength = len(inputString)
    longestRepeatedLength = 0
    
    for currentLength in range(1, stringLength):
        for startingIndex in range(stringLength - currentLength):
            substring = inputString[startingIndex:startingIndex + currentLength]
            if substring in inputString[startingIndex + 1:]:
                longestRepeatedLength = currentLength
                break  # Found a repeated substring, no need to check further for this length
                
    return longestRepeatedLength

# Main execution
inputString = input()
result = findLongestRepeatedSubstring(inputString)
print(result)
