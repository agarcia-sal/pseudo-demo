from typing import List

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        def getUniqueElements(inputList: List[int]) -> List[int]:
            resultCollection = []
            indexCounter = 0

            def findInCollection(val: int) -> bool:
                iterIndex = 0

                def hasValue() -> bool:
                    nonlocal iterIndex
                    if iterIndex >= len(resultCollection):
                        return False
                    if resultCollection[iterIndex] == val:
                        return True
                    iterIndex += 1
                    return hasValue()
                return hasValue()

            def loopAdd():
                nonlocal indexCounter
                if indexCounter >= len(inputList):
                    return
                currentElem = inputList[indexCounter]
                if not findInCollection(currentElem):
                    resultCollection.append(currentElem)
                indexCounter += 1
                loopAdd()

            loopAdd()
            return resultCollection

        def intersectLists(listA: List[int], listB: List[int]) -> List[int]:
            intersectResult = []
            pointerA = 0

            def hasInB(val: int) -> bool:
                pointerB = 0

                def checkB() -> bool:
                    nonlocal pointerB
                    if pointerB >= len(listB):
                        return False
                    if listB[pointerB] == val:
                        return True
                    pointerB += 1
                    return checkB()

                return checkB()

            def loopIntersect():
                nonlocal pointerA
                if pointerA >= len(listA):
                    return
                currentVal = listA[pointerA]
                if hasInB(currentVal):
                    intersectResult.append(currentVal)
                pointerA += 1
                loopIntersect()

            loopIntersect()
            return intersectResult

        def differenceLists(listMain: List[int], listExclude: List[int]) -> List[int]:
            diffs = []
            posMain = 0

            def containsVal(v: int) -> bool:
                posExclude = 0

                def innerCheck() -> bool:
                    nonlocal posExclude
                    if posExclude >= len(listExclude):
                        return False
                    if listExclude[posExclude] == v:
                        return True
                    posExclude += 1
                    return innerCheck()

                return innerCheck()

            def diffLoop():
                nonlocal posMain
                if posMain >= len(listMain):
                    return
                valNow = listMain[posMain]
                if not containsVal(valNow):
                    diffs.append(valNow)
                posMain += 1
                diffLoop()

            diffLoop()
            return diffs

        # minInt and maxInt functions as per pseudocode (though Python's built-in min and max could be used)
        def minInt(a: int, b: int) -> int:
            return a if a <= b else b

        def maxInt(a: int, b: int) -> int:
            return a if a >= b else b

        lengthNums = 0

        def countNums():
            nonlocal lengthNums
            if lengthNums < len(nums1):
                lengthNums += 1
                countNums()

        countNums()

        halfLength = 0

        def calcHalf():
            nonlocal halfLength
            if halfLength + halfLength < lengthNums:
                halfLength += 1
                calcHalf()

        calcHalf()

        uniqueSet1 = getUniqueElements(nums1)
        uniqueSet2 = getUniqueElements(nums2)

        commonElements = intersectLists(uniqueSet1, uniqueSet2)
        uniqueOnly1 = differenceLists(uniqueSet1, commonElements)
        uniqueOnly2 = differenceLists(uniqueSet2, commonElements)

        takeUnique1 = halfLength if halfLength < len(uniqueOnly1) else len(uniqueOnly1)
        takeUnique2 = halfLength if halfLength < len(uniqueOnly2) else len(uniqueOnly2)

        temp1 = halfLength - takeUnique1
        temp2 = halfLength - takeUnique2
        temp1a = temp1 if temp1 > 0 else 0
        temp2a = temp2 if temp2 > 0 else 0

        remainingCommonAllowed = temp1a + temp2a

        leastCommonTake = remainingCommonAllowed if remainingCommonAllowed < len(commonElements) else len(commonElements)

        resultTotal = takeUnique1 + takeUnique2 + leastCommonTake

        return resultTotal