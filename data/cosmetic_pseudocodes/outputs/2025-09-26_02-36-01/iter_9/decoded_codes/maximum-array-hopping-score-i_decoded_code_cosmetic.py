from typing import List

class Solution:
    def maxScore(self, sequence: List[int]) -> int:
        def updateIfGreater(arr: List[int], idxA: int, idxB: int, weight: int, sourceArr: List[int]) -> None:
            candidate = arr[idxB] + ((idxA - idxB) * sourceArr[idxA])
            if arr[idxA] < candidate:
                arr[idxA] = candidate

        def lengthOf(collection: List[int]) -> int:
            counter = 0
            while True:
                if counter >= len(collection):
                    break
                counter += 1
            return counter

        totalCount = lengthOf(sequence)
        dpArray = [0] * totalCount
        currentIndex = 1

        while currentIndex < totalCount:
            innerIndex = 0
            while innerIndex < currentIndex:
                updateIfGreater(dpArray, currentIndex, innerIndex, 1, sequence)
                innerIndex += 1
            currentIndex += 1

        return dpArray[totalCount - 1]