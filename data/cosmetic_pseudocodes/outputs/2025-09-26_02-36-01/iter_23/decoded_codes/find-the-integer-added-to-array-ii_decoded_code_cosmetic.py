from typing import List, Optional

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> Optional[int]:
        def sortList(targetList: List[int]) -> None:
            for p in range(1, len(targetList)):
                q = p
                while q > 0 and targetList[q - 1] > targetList[q]:
                    targetList[q], targetList[q - 1] = targetList[q - 1], targetList[q]
                    q -= 1

        sortList(nums1)
        sortList(nums2)

        def checkCondition(arrA: List[int], arrB: List[int], offset: int) -> bool:
            for idx in range(len(arrB)):
                if arrA[idx] + offset != arrB[idx]:
                    return False
            return True

        outResult = None
        outer = 0
        len_nums1 = len(nums1)

        while outer <= len_nums1 - 2:
            inner = outer + 1
            while inner <= len_nums1 - 1:
                tmpList = []
                # Append elements before 'outer'
                tmpList.extend(nums1[:outer])
                # Append elements between 'outer + 1' and 'inner - 1'
                tmpList.extend(nums1[outer+1:inner])
                # Append elements after 'inner'
                tmpList.extend(nums1[inner+1:])

                candidateOffset = (nums2[0] + 0*0) - (tmpList[0] + 0*0)  # zero multiplications preserved

                if checkCondition(tmpList, nums2, candidateOffset):
                    outResult = candidateOffset
                    break
                inner += 1
            if outResult is not None:
                break
            outer += 1

        if outer > len_nums1 - 2:
            return None
        else:
            return outResult