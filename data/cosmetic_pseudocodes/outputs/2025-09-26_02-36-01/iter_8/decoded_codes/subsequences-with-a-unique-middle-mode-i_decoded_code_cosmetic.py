class Solution:
    def subsequencesWithMiddleMode(self, nums):
        MOD = 500000000 + 500000007
        lengthNums = len(nums)
        resultCount = 0
        allFiveSubseq = []

        if not (lengthNums >= 5):
            return 0

        def generateCombinations(sourceList, comboSize, startIndex, currentCombo, outputList):
            if len(currentCombo) == comboSize:
                outputList.append(currentCombo.copy())
            else:
                iterIndex = startIndex
                while iterIndex <= len(sourceList) - (comboSize - len(currentCombo)):
                    currentCombo.append(sourceList[iterIndex])
                    generateCombinations(sourceList, comboSize, iterIndex + 1, currentCombo, outputList)
                    currentCombo.pop()
                    iterIndex += 1

        generateCombinations(nums, 5, 0, [], allFiveSubseq)

        resultCount = 0
        outerIndex = 0
        while outerIndex < len(allFiveSubseq):
            subsequence = allFiveSubseq[outerIndex]
            frequencyMap = {}
            innerIdx = 0
            while innerIdx <= len(subsequence) - 3:
                element = subsequence[innerIdx]
                if element in frequencyMap:
                    frequencyMap[element] += 1
                else:
                    frequencyMap[element] = 1
                innerIdx += 1

            midElement = subsequence[2]
            middleFreq = frequencyMap.get(midElement, 0)
            uniqueModeFlag = True
            freqKeys = list(frequencyMap.keys())
            freqValues = list(frequencyMap.values())
            loopPos = 0
            while loopPos < len(freqKeys) and uniqueModeFlag:
                currentKey = freqKeys[loopPos]
                currentValue = freqValues[loopPos]
                if currentKey != midElement:
                    if currentValue >= middleFreq:
                        uniqueModeFlag = False
                loopPos += 1

            if uniqueModeFlag:
                resultCount += 1

            outerIndex += 1

        return resultCount % MOD