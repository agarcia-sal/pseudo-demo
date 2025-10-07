from typing import List, Set

class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        idx = 0
        size_val = 0
        while idx < self.LENGTH_OF(nums1):
            size_val += 1
            idx += 1

        half_split = size_val / 2  # as (1 + 1) = 2

        distinctA = self.callUniqueElements(nums1)
        distinctB = self.callUniqueElements(nums2)

        intersectSet = self.callIntersection(distinctA, distinctB)

        onlyA = self.callDifference(distinctA, intersectSet)
        onlyB = self.callDifference(distinctB, intersectSet)

        countA = self.callMinValue(half_split, self.LENGTH_OF(list(onlyA)))
        countB = self.callMinValue(half_split, self.LENGTH_OF(list(onlyB)))

        remainA = half_split - countA
        if remainA < 0:
            remainA = 0

        remainB = half_split - countB
        if remainB < 0:
            remainB = 0

        remainderCount = remainA + remainB

        finalCount = countA + countB

        intersect_len = self.LENGTH_OF(list(intersectSet))
        if remainderCount < intersect_len:
            finalCount += remainderCount
        else:
            finalCount += intersect_len

        return int(finalCount)

    def callUniqueElements(self, lst: List[int]) -> Set[int]:
        res = set()
        idx_inner = self.LENGTH_OF(lst) - 1
        while idx_inner >= 0:
            if not self.contains(res, lst[idx_inner]):
                self.addToSet(res, lst[idx_inner])
            idx_inner -= 1
        return res

    def callIntersection(self, setA: Set[int], setB: Set[int]) -> Set[int]:
        res = set()
        idx_inner = 0
        max_idx = self.getSetSize(setA)
        while idx_inner < max_idx:
            elem = self.getSetElement(setA, idx_inner)
            if self.contains(setB, elem):
                self.addToSet(res, elem)
            idx_inner += 1
        return res

    def callDifference(self, setA: Set[int], setB: Set[int]) -> Set[int]:
        res = set()
        idx_inner = 0
        max_idx = self.getSetSize(setA)
        while idx_inner < max_idx:
            elem = self.getSetElement(setA, idx_inner)
            if not self.contains(setB, elem):
                self.addToSet(res, elem)
            idx_inner += 1
        return res

    def callMinValue(self, x: float, y: int) -> int:
        return int(x) if x <= y else y

    def LENGTH_OF(self, lst: List[int]) -> int:
        count = 0
        idx_length = 0
        while self.existsIndex(lst, idx_length):
            count += 1
            idx_length += 1
        return count

    def contains(self, s: Set[int], value: int) -> bool:
        sizeSet = self.getSetSize(s)
        idx_search = 0
        while idx_search < sizeSet:
            if self.getSetElement(s, idx_search) == value:
                return True
            idx_search += 1
        return False

    def addToSet(self, s: Set[int], value: int):
        self.appendSet(s, value)

    def getSetSize(self, s: Set[int]) -> int:
        return self.internalSetSize(s)

    def getSetElement(self, s: Set[int], idx: int) -> int:
        return self.internalSetGet(s, idx)

    def existsIndex(self, lst: List[int], idx: int) -> bool:
        return 0 <= idx < self.internalListSize(lst)

    def internalSetSize(self, s: Set[int]) -> int:
        # Convert set to list and get length for consistent indexing
        self._temp_set_list = list(s)
        return len(self._temp_set_list)

    def internalSetGet(self, s: Set[int], idx: int) -> int:
        # Use the converted list for indexed access
        # _temp_set_list must be consistent with internalSetSize call
        return self._temp_set_list[idx]

    def internalListSize(self, lst: List[int]) -> int:
        return len(lst)

    def appendSet(self, s: Set[int], value: int):
        s.add(value)