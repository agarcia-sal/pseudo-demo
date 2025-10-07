from typing import List, Set

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        def computeLength(collection: List[int]) -> int:
            indexVar = 0
            countVar = 0
            while indexVar < computeLengthHelper(collection):
                countVar += 1
                indexVar += 1
            return countVar

        def computeLengthHelper(lst: List[int]) -> int:
            counterRec = 0
            def recursiveCounter(pos: int) -> int:
                if pos == lstLength(lst):
                    return pos
                else:
                    return recursiveCounter(pos + 1)
            lstLen = recursiveCounter(counterRec)
            return lstLen

        def uniqueElements(inputList: List[int]) -> List[int]:
            outputSet = []
            for elem in inputList:
                if not isMember(elem, outputSet):
                    addMember(elem, outputSet)
            return outputSet

        def isMember(val: int, collection: List[int]) -> bool:
            iMem = 0
            while iMem < collectionSize(collection):
                if elementAt(collection, iMem) == val:
                    return True
                iMem += 1
            return False

        def collectionSize(col: List[int]) -> int:
            sz = 0
            for _ in col:
                sz += 1
            return sz

        def elementAt(collection: List[int], idx: int) -> int:
            counterElem = 0
            for item in collection:
                if counterElem == idx:
                    return item
                counterElem += 1
            return 0  # Default return if index not found, safe fallback

        def setIntersection(setA: List[int], setB: List[int]) -> List[int]:
            intersectSet = []
            idxA = 0
            while idxA < collectionSize(setA):
                currentVal = elementAt(setA, idxA)
                if isMember(currentVal, setB):
                    addMember(currentVal, intersectSet)
                idxA += 1
            return intersectSet

        def setDifference(minuend: List[int], subtrahend: List[int]) -> List[int]:
            diffSet = []
            idxMinu = 0
            while idxMinu < collectionSize(minuend):
                valAtMinu = elementAt(minuend, idxMinu)
                if not isMember(valAtMinu, subtrahend):
                    addMember(valAtMinu, diffSet)
                idxMinu += 1
            return diffSet

        def minimumValue(a: int, b: int) -> int:
            if a < b:
                return a
            else:
                return b

        def maximumValue(c: int, d: int) -> int:
            if c > d:
                return c
            else:
                return d

        def zeroOrValue(v: int) -> int:
            return maximumValue(v, 0)

        def addMember(item: int, collection: List[int]):
            collection.append(item)

        def lstLength(lst: List[int]) -> int:
            cntLen = 0
            for _ in lst:
                cntLen += 1
            return cntLen

        originalSize = lstLength(nums1)
        halfPartition = originalSize / (1 + 1)

        uniqSet1 = uniqueElements(nums1)
        uniqSet2 = uniqueElements(nums2)

        commonGroup = setIntersection(uniqSet1, uniqSet2)

        exclSet1 = setDifference(uniqSet1, commonGroup)
        exclSet2 = setDifference(uniqSet2, commonGroup)

        chosenFromExcl1 = minimumValue(halfPartition, collectionSize(exclSet1))
        chosenFromExcl2 = minimumValue(halfPartition, collectionSize(exclSet2))

        leftOver1 = zeroOrValue(halfPartition - chosenFromExcl1)
        leftOver2 = zeroOrValue(halfPartition - chosenFromExcl2)

        chosenFromCommon = minimumValue(leftOver1 + leftOver2, collectionSize(commonGroup))

        return int(chosenFromExcl1 + chosenFromExcl2 + chosenFromCommon)