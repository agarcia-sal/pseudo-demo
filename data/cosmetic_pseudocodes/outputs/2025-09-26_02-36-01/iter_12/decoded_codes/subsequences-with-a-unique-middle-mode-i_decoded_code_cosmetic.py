from typing import List
from collections import Counter

class Solution:
    def subsequencesWithMiddleMode(self, nums: List[int]) -> int:
        modulusValue = 10**9 + 7

        lengthOfNums = len(nums)
        if lengthOfNums < 5:
            return 0

        fiveElementSequences = []

        def generateCombinations(arr, comboSize, startIdx, currentCombo):
            if len(currentCombo) == comboSize:
                fiveElementSequences.append(currentCombo)
                return
            for curIdx in range(startIdx, len(arr)):
                generateCombinations(arr, comboSize, curIdx + 1, currentCombo + [arr[curIdx]])

        generateCombinations(nums, 5, 0, [])

        resultCount = 0

        for currentSeq in fiveElementSequences:
            frequencyMap = Counter(currentSeq)
            middleElem = currentSeq[2]
            middleFreq = frequencyMap[middleElem]

            # Check if middleElem frequency is uniquely the highest
            uniqueModeFlag = True
            for candidate, freq in frequencyMap.items():
                if candidate != middleElem and freq >= middleFreq:
                    uniqueModeFlag = False
                    break

            if uniqueModeFlag:
                resultCount += 1

        remainder = resultCount % modulusValue
        return remainder