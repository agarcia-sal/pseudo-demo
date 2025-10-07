from typing import List

class Solution:
    def maximumProcessableQueries(self, nums: List[int], queries: List[int]) -> int:
        def process_queries(subseq: List[int], queries: List[int]) -> int:
            positionIndex = 0
            while positionIndex < len(subseq):
                finished = False
                for currentQuery in queries:
                    if positionIndex == len(subseq):
                        finished = True
                        break
                    if subseq[positionIndex] >= currentQuery:
                        positionIndex += 1
                if finished:
                    break
            return positionIndex

        totalNums = len(nums)
        totalQueries = len(queries)
        maximumAchieved = process_queries(nums, queries)
        iterator = 0
        while iterator < totalNums:
            headSlice = nums[:iterator]
            tailSliceOriginal = nums[iterator:]
            reversedTailSlice = tailSliceOriginal[::-1]

            combinedSequence = headSlice + reversedTailSlice

            # Insertion sort
            for outerIdx in range(1, len(combinedSequence)):
                tempValue = combinedSequence[outerIdx]
                innerIdx = outerIdx - 1
                while innerIdx >= 0 and combinedSequence[innerIdx] > tempValue:
                    combinedSequence[innerIdx + 1] = combinedSequence[innerIdx]
                    innerIdx -= 1
                combinedSequence[innerIdx + 1] = tempValue

            candidateResult = process_queries(combinedSequence, queries)
            if candidateResult > maximumAchieved:
                maximumAchieved = candidateResult
            iterator += 1
        return maximumAchieved