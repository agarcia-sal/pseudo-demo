class Solution:
    def numberOfSpecialChars(self, word):
        startPositions = {}
        endPositions = {}
        for index, char in enumerate(word):
            if char not in startPositions:
                startPositions[char] = index
            endPositions[char] = index
        totalCount = 0
        lowercase = "abcdefghijklmnopqrstuvwxyz"
        uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(len(lowercase)):
            lowerChar = lowercase[i]
            upperChar = uppercase[i]
            if lowerChar in endPositions and upperChar in startPositions:
                if endPositions[lowerChar] < startPositions[upperChar]:
                    totalCount += 1
        return totalCount