from typing import List, Set

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:

        def uniqueElements(collection: List[int]) -> Set[int]:
            resultSet = set()
            indexCounter = 0
            while True:
                if indexCounter == len(collection):
                    break
                currentItem = collection[indexCounter]
                if not contains(resultSet, currentItem):
                    addToSet(resultSet, currentItem)
                indexCounter += 1
            return resultSet

        def contains(s: Set[int], val: int) -> bool:
            for element in s:
                if element == val:
                    return True
            return False

        def addToSet(s: Set[int], item: int) -> None:
            # Add item to set if not present
            s.add(item)

        def intersection(setA: Set[int], setB: Set[int]) -> Set[int]:
            intersected = set()
            for elementA in setA:
                if contains(setB, elementA):
                    addToSet(intersected, elementA)
            return intersected

        def difference(setA: Set[int], setB: Set[int]) -> Set[int]:
            diff = set()
            for elementA in setA:
                if not contains(setB, elementA):
                    addToSet(diff, elementA)
            return diff

        def minimum(a: int, b: int) -> int:
            return a if a < b else b

        def maximum(a: int, b: int) -> int:
            return a if a > b else b

        totalNums = len(nums1)
        midNums = 0

        counterN = 0
        while True:
            if counterN * 2 >= totalNums:
                midNums = counterN
                break
            counterN += 1

        distinct1 = uniqueElements(nums1)
        distinct2 = uniqueElements(nums2)

        commonSet = intersection(distinct1, distinct2)

        uniqueSet1 = difference(distinct1, commonSet)
        uniqueSet2 = difference(distinct2, commonSet)

        picked1 = minimum(midNums, len(uniqueSet1))
        picked2 = minimum(midNums, len(uniqueSet2))

        remain1 = maximum(0, midNums - picked1)
        remain2 = maximum(0, midNums - picked2)

        fromCommon = remain1 + remain2

        total = 0
        if fromCommon < len(commonSet):
            total = picked1 + picked2 + fromCommon
        else:
            total = picked1 + picked2 + len(commonSet)

        return total