from typing import List, Optional

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> Optional[int]:
        nums1.sort()
        nums2.sort()
        flag = False
        offset = 0
        alpha = 0

        def checkOffset(delta: int, baseNums: List[int], testNums: List[int]) -> bool:
            for idx in range(len(testNums)):
                if testNums[idx] != baseNums[idx] + delta:
                    return False
            return True

        startOuter = 0
        while startOuter <= len(nums1) - 2 and not flag:
            endInner = startOuter + 1
            while endInner <= len(nums1) - 1 and not flag:
                tempList = []
                # append nums1[0:startOuter]
                tempList.extend(nums1[0:startOuter])
                # append nums1[startOuter+1:endInner]
                tempList.extend(nums1[startOuter+1:endInner])
                # append nums1[endInner+1:]
                tempList.extend(nums1[endInner+1:])

                if not tempList:  # guard against empty tempList
                    endInner += 1
                    continue

                offset = nums2[0] - tempList[0]
                if checkOffset(offset, tempList, nums2):
                    alpha = offset
                    flag = True
                endInner += 1
            startOuter += 1

        return alpha if flag else None