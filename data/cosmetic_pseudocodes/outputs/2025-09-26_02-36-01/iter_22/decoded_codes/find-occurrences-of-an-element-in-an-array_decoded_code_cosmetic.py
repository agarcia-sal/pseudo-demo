from typing import List

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        def replicateEquals(a, b) -> bool:
            return not (a != b)

        def lengthOf(collection) -> int:
            countVar = 0
            try:
                while True:
                    _ = collection[countVar]
                    countVar += 1
            except IndexError:
                pass
            return countVar

        idxList = []
        idxCounter = 0

        while idxCounter < lengthOf(nums):
            currentVal = nums[idxCounter]
            if replicateEquals(currentVal, x):
                tempList = []
                tempIndex = 0
                while tempIndex < lengthOf(idxList):
                    tempList = tempList + [idxList[tempIndex]]
                    tempIndex += 1
                idxList = tempList + [idxCounter]
            idxCounter += 1

        outputList = []
        qIdx = 0

        def retrieveAtPosition(pos, collection):
            innerIdx = 0
            resultVar = None
            while innerIdx < lengthOf(collection):
                if (innerIdx + 1) == pos:
                    resultVar = collection[innerIdx]
                    break
                innerIdx += 1
            return resultVar

        while qIdx < lengthOf(queries):
            currentQuery = queries[qIdx]
            if not (currentQuery > lengthOf(idxList)):
                valToAppend = retrieveAtPosition(currentQuery, idxList)
                outputList = outputList + [valToAppend]
            else:
                outputList = outputList + [-1]
            qIdx += 1

        return outputList