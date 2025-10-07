from typing import List

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        def lengthOf(collection: List[int]) -> int:
            count = 0
            def recurse(idx: int) -> int:
                nonlocal count
                if idx == len(collection):
                    return count
                else:
                    count += 1
                    return recurse(idx + 1)
            return recurse(0)

        def uniqueElements(inputList: List[int]) -> List[int]:
            uniqueList: List[int] = []
            def contains(coll: List[int], elem: int) -> bool:
                present = False
                def check(index: int) -> bool:
                    nonlocal present
                    if index == len(coll):
                        return present
                    else:
                        present = present or (coll[index] == elem)
                        return check(index + 1)
                return check(0)

            def addIfUnique(idx: int) -> None:
                nonlocal uniqueList
                if idx == len(inputList):
                    return
                else:
                    if not contains(uniqueList, inputList[idx]):
                        uniqueList = uniqueList + [inputList[idx]]
                    addIfUnique(idx + 1)
            addIfUnique(0)
            return uniqueList

        def intersection(listA: List[int], listB: List[int]) -> List[int]:
            interList: List[int] = []
            def existsInListB(value: int) -> bool:
                found = False
                def search(j: int) -> bool:
                    nonlocal found
                    if j == len(listB):
                        return found
                    else:
                        found = found or (listB[j] == value)
                        return search(j + 1)
                return search(0)

            def buildInter(idx: int) -> None:
                nonlocal interList
                if idx == len(listA):
                    return
                else:
                    if existsInListB(listA[idx]) and not (listA[idx] in interList):
                        interList = interList + [listA[idx]]
                    buildInter(idx + 1)
            buildInter(0)
            return interList

        def difference(fromList: List[int], withoutList: List[int]) -> List[int]:
            diffList: List[int] = []
            def isInWithout(val: int) -> bool:
                included = False
                def checkK(k: int) -> bool:
                    nonlocal included
                    if k == len(withoutList):
                        return included
                    else:
                        included = included or (withoutList[k] == val)
                        return checkK(k + 1)
                return checkK(0)

            def buildDiff(i: int) -> None:
                nonlocal diffList
                if i == len(fromList):
                    return
                else:
                    if not isInWithout(fromList[i]):
                        diffList = diffList + [fromList[i]]
                    buildDiff(i + 1)
            buildDiff(0)
            return diffList

        def minVal(a: int, b: int) -> int:
            return a if a < b else b

        def maxVal(a: int, b: int) -> int:
            return a if a > b else b

        totalLength = lengthOf(nums1)
        halfLength = totalLength // 2

        uniqueNums1 = uniqueElements(nums1)
        uniqueNums2 = uniqueElements(nums2)

        commonElements = intersection(uniqueNums1, uniqueNums2)
        uniqueSet1 = difference(uniqueNums1, commonElements)
        uniqueSet2 = difference(uniqueNums2, commonElements)

        take1 = minVal(halfLength, lengthOf(uniqueSet1))
        take2 = minVal(halfLength, lengthOf(uniqueSet2))

        remain1 = maxVal(0, halfLength - take1)
        remain2 = maxVal(0, halfLength - take2)
        takeCommonRaw = remain1 + remain2
        takeCommon = minVal(takeCommonRaw, lengthOf(commonElements))

        finalAnswer = take1 + take2 + takeCommon

        return finalAnswer