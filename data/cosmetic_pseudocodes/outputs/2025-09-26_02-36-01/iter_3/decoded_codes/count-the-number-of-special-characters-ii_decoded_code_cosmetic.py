class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        beginningMap = {}
        endingMap = {}
        positionCounter = 0
        while positionCounter < len(word):
            currentChar = word[positionCounter]
            if currentChar not in beginningMap:
                beginningMap[currentChar] = positionCounter
            endingMap[currentChar] = positionCounter
            positionCounter += 1

        resultCount = 0
        lowerIndex = 0
        upperIndex = 0
        lowercaseSeq = "abcdefghijklmnopqrstuvwxyz"
        uppercaseSeq = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while lowerIndex < len(lowercaseSeq) and upperIndex < len(uppercaseSeq):
            lowerChar = lowercaseSeq[lowerIndex]
            upperChar = uppercaseSeq[upperIndex]

            if (lowerChar in endingMap 
                and upperChar in beginningMap 
                and endingMap[lowerChar] < beginningMap[upperChar]):
                resultCount += 1

            lowerIndex += 1
            upperIndex += 1

        return resultCount