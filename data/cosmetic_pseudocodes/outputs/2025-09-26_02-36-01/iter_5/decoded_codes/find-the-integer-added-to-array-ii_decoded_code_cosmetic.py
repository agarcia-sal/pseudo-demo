from typing import List, Optional

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> Optional[int]:
        def quickSort(L: List[int], left: int, right: int) -> None:
            if left < right:
                pivotIndex = left
                pivotValue = L[pivotIndex]
                i = left + 1
                j = right
                while i <= j:
                    while i <= right and L[i] <= pivotValue:
                        i += 1
                    while j > left and L[j] >= pivotValue:
                        j -= 1
                    if i < j:
                        L[i], L[j] = L[j], L[i]
                # After loop ends, swap pivot with L[j]
                L[pivotIndex], L[j] = L[j], L[pivotIndex]
                quickSort(L, left, j - 1)
                quickSort(L, j + 1, right)

        def sort(L: List[int]) -> None:
            if L:
                quickSort(L, 0, len(L) - 1)

        sort(nums1)
        sort(nums2)

        def buildNewList(origList: List[int], skipStart: int, skipEnd: int) -> List[int]:
            resultingList = []
            def recurAdd(pos: int) -> None:
                if pos >= len(origList):
                    return
                if not (skipStart <= pos <= skipEnd):
                    resultingList.append(origList[pos])
                recurAdd(pos + 1)
            recurAdd(0)
            return resultingList

        def nestedLoop(a: List[int], b: List[int]) -> Optional[int]:
            def outerLoop(i: int) -> Optional[int]:
                if i > len(a) - 2:
                    return None
                def innerLoop(j: int) -> Optional[int]:
                    if j > len(a) - 1:
                        return outerLoop(i + 1)

                    filtered = buildNewList(a, i, j)
                    if not filtered:
                        return innerLoop(j + 1)
                    delta = b[0] - filtered[0]

                    def verifyCondition(idx: int) -> bool:
                        if idx >= len(b):
                            return True
                        if idx >= len(filtered):
                            return False
                        if filtered[idx] + delta == b[idx]:
                            return verifyCondition(idx + 1)
                        else:
                            return False

                    if verifyCondition(0):
                        return delta
                    else:
                        return innerLoop(j + 1)
                return innerLoop(i + 1)
            return outerLoop(0)

        result = nestedLoop(nums1, nums2)
        return result