inputString = input().rstrip()
lengthOfInputString = len(inputString)
longestRepeatedSubstringLength = 0

for currentLength in range(1, lengthOfInputString):
    for startPosition in range(lengthOfInputString - currentLength):
        substring = inputString[startPosition:startPosition + currentLength]
        if substring in inputString[startPosition + 1:]:
            longestRepeatedSubstringLength = currentLength
            break

print(longestRepeatedSubstringLength)


def longest_repeated_substring(inputString):
    lengthOfInputString = len(inputString)
    if lengthOfInputString == 0:
        return 0
    
    longestRepeatedSubstringLength = 0
    
    for currentLength in range(1, lengthOfInputString):
        seen_substrings = set()
        for startPosition in range(lengthOfInputString - currentLength + 1):
            substring = inputString[startPosition:startPosition + currentLength]
            if substring in seen_substrings:
                longestRepeatedSubstringLength = currentLength
                break
            seen_substrings.add(substring)
    
    return longestRepeatedSubstringLength

inputString = input().rstrip()
print(longest_repeated_substring(inputString))
