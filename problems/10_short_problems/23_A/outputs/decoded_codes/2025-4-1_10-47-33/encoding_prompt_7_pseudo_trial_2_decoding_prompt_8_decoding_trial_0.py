def findLongestRepeatedSubstring():
    inputString = input()
    stringLength = len(inputString)
    longestRepetitionLength = 0

    for l in range(stringLength):
        for i in range(stringLength):
            substring = inputString[i:i+l+1]
            if inputString.find(substring, i + 1) != -1:
                longestRepetitionLength = l + 1
                break

    return longestRepetitionLength
