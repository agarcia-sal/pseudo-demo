from typing import List

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        def sizeOfCollection(collection: List[int]) -> int:
            counter = 0
            index = 0
            while index < len(collection):
                counter += 1
                index += 1
            return counter

        def smallest(a: int, b: int) -> int:
            if a < b:
                return a
            else:
                return b

        def largest(a: int, b: int) -> int:
            if a > b:
                return a
            else:
                return b

        def contains(collection: List[int], item: int) -> bool:
            idx = 0
            while idx < len(collection):
                if collection[idx] == item:
                    return True
                idx += 1
            return False

        def uniqueElements(inputList: List[int]) -> List[int]:
            seen = []
            iterator = 0
            while iterator < len(inputList):
                element = inputList[iterator]
                if not contains(seen, element):
                    seen.append(element)
                iterator += 1
            return seen

        def intersection(collection1: List[int], collection2: List[int]) -> List[int]:
            result = []
            pos = 0
            while pos < len(collection1):
                elem = collection1[pos]
                if contains(collection2, elem) and not contains(result, elem):
                    result.append(elem)
                pos += 1
            return result

        def difference(setA: List[int], setB: List[int]) -> List[int]:
            resultSet = []
            counter = 0
            while counter < len(setA):
                item = setA[counter]
                if not contains(setB, item):
                    resultSet.append(item)
                counter += 1
            return resultSet

        sizeNums1 = sizeOfCollection(nums1)
        halfSize = sizeNums1 // 2

        distinctNums1 = uniqueElements(nums1)
        distinctNums2 = uniqueElements(nums2)

        intersectNums = intersection(distinctNums1, distinctNums2)

        diffNums1 = difference(distinctNums1, intersectNums)
        diffNums2 = difference(distinctNums2, intersectNums)

        countDiff1 = smallest(halfSize, sizeOfCollection(diffNums1))
        countDiff2 = smallest(halfSize, sizeOfCollection(diffNums2))

        remaining1 = largest(0, halfSize - countDiff1)
        remaining2 = largest(0, halfSize - countDiff2)

        extraFromCommon = remaining1 + remaining2

        totalChosen = countDiff1 + countDiff2 + smallest(extraFromCommon, sizeOfCollection(intersectNums))

        return totalChosen