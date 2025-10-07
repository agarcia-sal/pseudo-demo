from typing import List, Dict

class Solution:
    def subsequencesWithMiddleMode(self, nums: List[int]) -> int:
        magicConst = 10**9 + 7
        lenNums = len(nums)
        if not (lenNums >= 5):
            return 0

        def generateCombs(setList: List[int], pickCount: int) -> List[List[int]]:
            def helper(currIndex: int, chosenSoFar: List[int]) -> List[List[int]]:
                if len(chosenSoFar) == pickCount:
                    return [chosenSoFar]
                if currIndex == len(setList):
                    return []
                # Collect subsequences skipping current element
                skipResults = helper(currIndex + 1, chosenSoFar)
                # Collect subsequences including current element
                takeResults = helper(currIndex + 1, chosenSoFar + [setList[currIndex]])
                return skipResults + takeResults
            return helper(0, [])

        allSubseq = generateCombs(nums, 5)

        resultCounter = 0
        for currentSeq in allSubseq:
            freqMap: Dict[int, int] = {}
            for val in currentSeq:
                freqMap[val] = freqMap.get(val, 0) + 1

            medIdx = 2
            medVal = currentSeq[medIdx]
            medCount = freqMap[medVal]

            isModeUnique = True
            for key in freqMap:
                if key != medVal and freqMap[key] >= medCount:
                    isModeUnique = False
                    break

            if isModeUnique:
                resultCounter += 1

        return resultCounter % magicConst